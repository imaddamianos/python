import wolframalpha
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time
import requests
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

from functions import sendEmail, speak, takeCommand, username, wishMe


if __name__ == '__main__':
    # Clear the terminal screen
    clear = lambda: os.system('clear')
    clear()

    wishMe()
    username()
    
    assname = "Jarvis"  # Default assistant name

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "/Users/your_username/Music"  # Update this path
            songs = os.listdir(music_dir)
            print(songs)
            os.system(f"open {os.path.join(music_dir, songs[1])}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send it to?")
                to = input()  # Using input instead of takeCommand
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir?")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Gaurav.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            app_id = "Wolframalpha API id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely you're human.")

        elif "why you came to the world" in query:
            speak("Thanks to Gaurav. Further, it's a secret")

        elif 'power point presentation' in query:
            speak("Opening PowerPoint presentation")
            power = "/Users/your_username/Documents/Presentation/Voice_Assistant.pptx"  # Update this path
            os.system(f"open {power}")

        elif 'is love' in query:
            speak("It is the 7th sense that destroys all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav")

        elif 'change background' in query:
            speak("This feature is not supported on macOS")

        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=YOUR_API_KEY')
                data = json.load(jsonObj)
                i = 1
                speak('Here are some top news from the Times of India')
                print('=============== TIMES OF INDIA ============' + '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'lock window' in query:
            speak("This feature is not supported on macOS")

        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            os.system('sudo shutdown -h now')

        elif 'empty recycle bin' in query:
            speak("This feature is not supported on macOS")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time do you want to stop the assistant from listening to commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Virtual Assistant Camera ", "img.jpg")

        elif "restart" in query:
            os.system('sudo shutdown -r now')

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating is not supported on macOS")

        elif "log off" in query or "sign out" in query:
            speak("Logging out")
            os.system('killall -u $(whoami)')

        elif "write a note" in query:
            speak("What should I write, Sir?")
            note = takeCommand()
            file = open('assistant.txt', 'w')
            speak("Should I include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("assistant.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading the file, please replace this file with the downloaded one")
            url = 'URL_TO_YOUR_UPDATE_FILE'
            r = requests.get(url, stream=True)
            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size=2391975), expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "assistant" in query:
            wishMe()
            speak("Assistant version 1.0 in your service")
            speak(assname)

        elif "weather" in query:
            api_key = "YOUR_API_KEY"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name")
            print("City name: ")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) =" + str(current_pressure) +
                      "\n humidity (in percentage) = " + str(current_humidity) +
                      "\n description = " + str(weather_description))
                speak(f"Temperature is {current_temperature} kelvin, pressure is {current_pressure} hPa, "
                      f"humidity is {current_humidity} percent, and the weather description is {weather_description}")
            else:
                speak("City Not Found")

        elif "send message" in query:
            account_sid = 'ACCOUNT_SID'
            auth_token = 'AUTH_TOKEN'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=takeCommand(),
                from_='Sender_No',
                to='Receiver_No'
            )
            print(message.sid)

        elif "Good Morning" in query:
            speak("A warm " + query)
            speak("How are you, Mister")
            speak(assname)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about that, maybe you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you asked")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
            try:
                speak(next(res.results).text)
            except StopIteration:
                speak("No results")

        # Add more commands here
