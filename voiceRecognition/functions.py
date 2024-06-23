import datetime
import shutil
import smtplib
import speech_recognition as sr
import pyttsx3
import wolframalpha


# Initialize the speech engine
engine = pyttsx3.init('nsss')  # 'nsss' is the driver for macOS

# Get available voices
voices = engine.getProperty('voices')

# Print the available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set the desired voice; you can change the index to use a different voice
engine.setProperty('voice', voices[19].id)

# Optionally, set other properties like volume and rate
engine.setProperty('rate', 175)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)


def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Function to wish the user based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir !")

    assname = "bee"
    speak("I am your Assistant")
    speak(assname)


def username():
    """Function to get the username of the user"""
    speak("What should I call you sir")
    uname = takeCommand()
    # speak("Welcome Mister")
    # speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))

    speak(f" How can I help you, {uname}")

def takeCommand():
    """Function to take commands from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

def calculate(query):
    app_id = "5TE5GW-GPKVAK88PX"  # Replace with your WolframAlpha API ID
    client = wolframalpha.Client(app_id)
    
    try:
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)
    except Exception as e:
        print(e)
        speak("I'm sorry, I couldn't calculate that. Please try again.")


def sendEmail(to, content):
    """Function to send email"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('damianos.imad@gmail.com', 'Im1!ad2@')
    server.sendmail('damianos.imad@gmail.com', to, content)
    server.close()
