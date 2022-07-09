import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#This dictionary contains email addresses of your important contacts and is used to send email
Dict = {
    'person1' : 'person1_email@gmail.com',
    'person2' : 'person2_email@gmail.com'
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am voice assistant. How may I help you?")       

def takeCommand():

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your_email@gmail.com', 'your_password') 
    # Your email address and password is to be filled here, which is ommitted as of now due to security reasons

    server.sendmail('your_email@gmail.com', to, content)
    # Your email address is to be filled here, which is ommitted as of now due to security reasons

    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open interviewbit' in query:
            webbrowser.open("interviewbit.com")

        elif 'open overleaf' in query:
            webbrowser.open("overleaf.com")

        elif 'open mandi' in query:
            webbrowser.open("iitmandi.ac.in")

        elif 'play music' in query:
            music_dir = 'VOICE ASSISSTANT/Music'
            songs = os.listdir(music_dir)
            a=random.randint(0,len(songs)) 
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                if 'person1' in query:
                    to = Dict['person1'] #This is the email of the person whom email is to be sent
                    sendEmail(to, content)
                    speak("Email has been sent!")   
                elif 'person2' in query:
                    to = Dict['person2'] #This is the email of the person whom email is to be sent
                    sendEmail(to, content)
                    speak("Email has been sent!")
            except Exception as e:
                speak("Sorry! Unable to do that as of now.")  
        else:
            speak("I don't understand") 