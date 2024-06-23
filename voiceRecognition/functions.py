import datetime
import shutil
import smtplib
import requests
import speech_recognition as sr
import pyttsx3
import wolframalpha

USER_NAME_FILE = "my_Name.txt"

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

def load_user_name():
    try:
        with open(USER_NAME_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "siri"  # Default name if file doesn't exist

def save_user_name(name):
    with open(USER_NAME_FILE, "w") as file:
        file.write(name)


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
    uname = load_user_name()
    if not uname:
        speak("I am your Assistant")
        speak(assname)


def load_user_name():
    try:
        with open(USER_NAME_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

def save_user_name(name):
    with open(USER_NAME_FILE, "w") as file:
        file.write(name)

def username():
    """Function to get the username of the user"""

    uname = load_user_name()
    
    if not uname:  # If the file is empty or does not exist
        speak("What should I call you, sir?")
        uname = takeCommand()
        save_user_name(uname)  # Save the name to file
    else:
        speak(f"Welcome back, Mr. {uname}")

    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))

    speak(f"How can I help you, {uname}")

def weather():
    api_key = "29764ca885604c3ca56121707242306"
    base_url = "http://api.weatherapi.com/v1/current.json"
    
    speak("City name")
    print("City name: ")
    city_name = takeCommand()
    
    complete_url = f"{base_url}?key={api_key}&q={city_name}"
    response = requests.get(complete_url)
    
    if response.status_code == 200:  # Check if API request was successful
        data = response.json()
        
        if "location" in data:
            location = data["location"]["name"]
            current_temperature = data["current"]["temp_c"]
            current_pressure = data["current"]["pressure_mb"]
            current_humidity = data["current"]["humidity"]
            weather_description = data["current"]["condition"]["text"]
            
            print(f"Location: {location}\n"
                  f"Temperature (in Celsius): {current_temperature}\n"
                  f"Atmospheric pressure (in hPa): {current_pressure}\n"
                  f"Humidity (in percentage): {current_humidity}\n"
                  f"Weather description: {weather_description}")
            
            speak(f"Location: {location}, Temperature is {current_temperature} degrees Celsius, "
                  f"pressure is {current_pressure} hPa, humidity is {current_humidity} percent, "
                  f"and the weather description is {weather_description}")
        else:
            speak("City not found")
    else:
        speak("Error fetching weather data")


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

def stop_assistant():
    speak("Assistant is stopping. Thank you for using me.")
    exit()

def sendEmail(to, content):
    """Function to send email"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('damianos.imad@gmail.com', 'Im1!ad2@')
    server.sendmail('damianos.imad@gmail.com', to, content)
    server.close()
