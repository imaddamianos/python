import datetime
import shutil
import smtplib
import speech_recognition as sr
import pyttsx3


# Initialize the speech engine
engine = pyttsx3.init('dummy')  # 'nsss' is the driver for macOS

# Get available voices
voices = engine.getProperty('voices')

# Print the available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set the desired voice; you can change the index to use a different voice
engine.setProperty('voice', voices[0].id)

# Optionally, set other properties like volume and rate
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)


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

    assname = "Jarvis 1 point o"
    speak("I am your Assistant")
    speak(assname)


def username():
    """Function to get the username of the user"""
    speak("What should I call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))

    speak("How can I help you, Sir")


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


def sendEmail(to, content):
    """Function to send email"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


# Main function
if __name__ == "__main__":
    wishMe()
    username()
    while True:
        query = takeCommand().lower()

        # Example command: send an email
        if 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "receiver's email id"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        # Add more commands as needed
