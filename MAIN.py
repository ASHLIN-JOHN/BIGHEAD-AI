import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("i am big head sir what can i do for you")


def takeCommand():
    # It takes microphone input from the user and returns string output
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
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "big head" in query:
            speak("I am here sir please tell me what can i do ")
        while True:
            query = takeCommand().lower()
            if 'search' in query:
                speak('Searching in my data sir...')
                query = query.replace("wikipedia.Search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("my data says that")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open brain' in query:
                webbrowser.open("google.com")
            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'play music' in query:
                music_dir = 'D:\python learning\learnpythontutorials\AI\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'what is the time now' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'open chrome' in query:
                codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)
            elif 'open word' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
                os.startfile(codePath)
            elif 'open point' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
                os.startfile(codePath)
            elif 'open excel' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
                os.startfile(codePath)
            elif 'open editor' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 2022.lnk"
                os.startfile(codePath)
            elif 'open illustrator' in query:
                codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Illustrator 2022.lnk"
                os.startfile(codePath)
            elif 'send email to ' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "YourfriendEmail@gmail.com"
                    sendEmail = (to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")
            elif 'exit' in query:
                speak("closing sir")
                break
            elif 'close' in query:
                exit()
            elif "thank you" in query:
                speak("it's my pleasure")