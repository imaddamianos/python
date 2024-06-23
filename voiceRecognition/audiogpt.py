import os
import tempfile
import openai
import speech_recognition as sr
import requests
import pyttsx3
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Replace 'your_api_key' with your actual OpenAI API key
openai.api_key = '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'

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Debug: print available Microphones
        print("Available Microphones:", sr.Microphone.list_microphone_names())

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand your voice.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

def generate_chat_gpt_response(prompt):
    full_response = ""
    response = openai.ChatCompletion.create(
        model="whisper-1",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    if not response.get('choices'):
        return "Could not generate a response based on the input provided."

    answer = response['choices'][0]['message']['content']
    full_response += answer

    return full_response

def text_to_speech(text):
    tts = gTTS(text=text, lang='en-gb')  # Change the accent to British English if desired
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        temp_path = f"{fp.name}.mp3"
        tts.save(temp_path)
        os.system(f"afplay {temp_path}")  # macOS specific command to play audio
        os.remove(temp_path)

def send_question_to_server(text):
    try:
        response = requests.post('http://127.0.0.1:5000/ask', json={'text': text})
        return response.json()['response']
    except Exception as e:
        print(f"An error occurred while communicating with the server: {e}")
        return None

if __name__ == "__main__":
    try:
        while True:
            user_input = recognize_speech()
            if user_input is not None:
                response_text = generate_chat_gpt_response(user_input)
                if response_text is not None:
                    print(f"ChatGPT: {response_text}")
                    text_to_speech(response_text)
    except KeyboardInterrupt:
        print("\nExiting the app. Goodbye!")
