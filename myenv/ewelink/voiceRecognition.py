import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands and respond
def listen_and_respond():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You: {query}")
        respond_to_query(query)
    except Exception as e:
        print(e)
        speak("I'm sorry, I didn't catch that. Can you repeat?")

# Function to respond based on recognized query
def respond_to_query(query):
    if "hello" in query.lower():
        speak("Hello! How can I help you today?")
    elif "how are you" in query.lower():
        speak("I'm doing great, thanks for asking!")
    elif "bye" in query.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I'm not sure how to respond to that.")

# Main loop to listen continuously
if __name__ == "__main__":
    speak("Hello! How can I assist you?")
    while True:
        listen_and_respond()
