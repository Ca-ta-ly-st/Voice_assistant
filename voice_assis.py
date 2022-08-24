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
    'Person1' : 'person1_email@gmail.com',
    'Person2' : 'person2_email@gmail.com',
    'Person3' : 'person3_email@gmail.com'
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

    server.login('your_email,'your_password') 
    # Your email address and password is to be filled here, which is ommitted as of now due to security reasons

    server.sendmail('your_email', to, content)
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
 
        elif 'bye' in query:
            speak("Bye! Hoping To see you again sir")
            break;

        elif 'open youtube' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening Gmail")
            webbrowser.open("gmail.com")

        elif 'open stackoverflow' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening sTackoverflow")
            webbrowser.open("stackoverflow.com")   

        elif 'open github' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening GiThub")
            webbrowser.open("github.com")

        elif 'open interviewbit' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening InTerviewbiT")
            webbrowser.open("interviewbit.com")

        elif 'open overleaf' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening Overleaf")
            webbrowser.open("overleaf.com")

        elif 'open mandi' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Opening IIT Mandi websiTe")
            webbrowser.open("iitmandi.ac.in")

        elif 'play music' in query:
            if 'please' in query:
                speak("Sure sir")
            speak("Playing music")
            music_dir = 'VOICE ASSISSTANT/Music'
            songs = os.listdir(music_dir)
            a=random.randint(0,len(songs)-1) 
            os.startfile(os.path.join(music_dir, songs[a]))

        elif 'the time' in query:
            if 'please' in query:
                speak("Sure sir")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to' in query:
            if 'please' in query:
                speak("Sure sir")
            try:
                speak("What should I say?")
                content = takeCommand()
                if 'person1' in query:
                    to = Dict['Person1'] #This is the email of the person whom email is to be sent
                    sendEmail(to, content)
                    speak("Email has been sent!")   
                elif 'person2' in query:
                    to = Dict['Person2'] #This is the email of the person whom email is to be sent
                    sendEmail(to, content)
                    speak("Email has been sent!")
                elif 'person3' in query:
                    to = Dict['Person3'] #This is the email of the person whom email is to be sent
                    sendEmail(to, content)
                    speak("Email has been sent!")
                else:
                    speak("Not in the list sir!")
            except Exception as e:
                speak("Sorry! Unable to do that as of now.")  
        elif 'thank you' in query:
            speak("your most welcome")
        else:
            speak("Sorry! I don't understand") 