import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak("Good Evening")
    speak("i am sivin. please tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:

        print("say that again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('keshavshukla2525@gmail.com', 'artismypassion')
    server.sendmail('keshavshukla2525@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results =wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir ='D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open pycharm' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'email to keshav' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "keshavshukla2525@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry we can't send send email")



