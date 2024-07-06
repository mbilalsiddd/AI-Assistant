# import pyaudio
# import xsmtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import nltk
import datetime
import os
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from nltk.tokenize import word_tokenize
import smtplib





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "none"
    return query

def process_command(command):
    tokens = word_tokenize(command.lower())
    if "email" in tokens and ("send" in tokens or "open" in tokens):
        return "send_email"
    else:
        return "unknown_command"


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("bs03465284068@gmail.com", "namqnyiqnepthdrn")
    server.sendmail("bs03465284068@gmail.com", to, content)
    server.close()


def repeat():
    speak("Is there anything else, sir?")
    response = takeCommand().lower()

    if "nothing" in response or "no" in response:
        speak("Shutting down. Goodbye, sir.")
        exit()
    else:
        speak("Go ahead, I am on, sir.")



def main_loop():
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            speak(results)
            repeat()
        elif "open w3schools" in query:
            webbrowser.open("https://www.w3schools.com")
            repeat()
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            repeat()
        elif "google chrome" in query:
            webbrowser.open("https://www.google.com")
            repeat()
        elif "open daraz" in query:
            webbrowser.open("https://www.daraz.pk")
            repeat()
        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")
            repeat()
        elif "open react native" in query:
            webbrowser.open("https://reactnative.dev")
            repeat()
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com")
            repeat()
        elif "open github" in query:
            webbrowser.open("https://github.com")
            repeat()
        elif "open chatgpt" in query:
            webbrowser.open("https://chat.openai.com")
            repeat()
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com")
            repeat()
        elif "open mongodb" in query:
            webbrowser.open("https://www.mongodb.com")
            repeat()
        elif "play naat" in query:
         naat_dir = "C:\\Naat"
         naat = os.listdir(naat_dir)
         print(naat)
         os.startfile(os.path.join(naat_dir, naat[0]))
        elif "open code" in query:
         codePath = "C:\\Users\\Mutahir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)
         repeat()
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")
            repeat()
        elif "send email to bilal" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bs03465284068@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent...")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")
            else:
               speak("Command not recognized.")
               repeat()

if __name__ == '__main__':
    speak("I am harvey sir, please tell me how may I help you")
    main_loop()


