import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
from datetime import datetime
import geocoder
from openai import OpenAI

# API KEYS
newsApi = "YOUR_NEWS_API_KEY"
weather_api = "YOUR_WEATHER_API_KEY"


#Speech + Audio setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()
pygame.mixer.init()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# Weather
def get_weather():
    try:
        g = geocoder.ip('me')
        city = g.city

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
        r = requests.get(url)
        data = r.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}")

    except:
        speak("Could not fetch weather.")

# Time & Date
def tell_time_date():
    now = datetime.now()
    speak(now.strftime("The time is %I:%M %p"))
    speak(now.strftime("Today is %A, %d %B %Y"))

# Spotify play in browser
def play_spotify(song):
    url = f"https://open.spotify.com/search/{song}"
    webbrowser.open(url)
    speak(f"Playing {song} on Spotify")

# Command Processor
def processCommand(c):
    c = c.lower().strip()

    # 🌐 Websites
    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open github" in c:
        webbrowser.open("https://github.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    # 🎵 Local music
    elif c.startswith("play"):
        song = " ".join(c.split(" ")[1:]).strip()

        found_song = None
        for key in musicLibrary.music.keys():
            if key.strip().lower() == song.lower():
                found_song = key
                break
        
        if found_song:
            webbrowser.open(musicLibrary.music[found_song])
        else:
            play_spotify(song)

    #  News
    elif "news" in c:
        try:
            url = f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&pageSize=5&apiKey={newsApi}"
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])

                if articles:
                    speak("Here are the latest news updates")
                    for article in articles:
                        speak(article["title"])
                else:
                    speak("No news found at the moment.")

            else:
                speak("News service error.")

        except Exception as e:
            print("News error:", e)
            speak("Unable to fetch news.")

    #  Weather
    elif "weather" in c or "temperature" in c:
        get_weather()

    # 🕒 Time & Date
    elif "time" in c or "date" in c:
        tell_time_date()

    # 🤖 AI fallback
    else:
        ask_ai(c)

#  MAIN LOOP
if __name__ == "__main__":
    speak("Initializing Atlas")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)

            if word.lower() == "atlas":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Atlas active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        except Exception as e:
            print("Error:", e)
          
