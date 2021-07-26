import pyttsx3
import datetime
import speech_recognition as s1
import wikipedia
import webbrowser
import os
##pyttsx3 is a voice api by microsoft for text to speech conversion
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
##print all types of voices in computer one male voice and one female voice
##print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am PC Assitant Sir.Please tell me how I help Yyu")
def takeCommand():
    ##It takes microphone input from the user and returns the string output
    r=s1.Recognizer()
    with s1.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :, {query}\n")    
    except Exception as e:
        print(e)
        print("Say that again")
        return "None"  
    return query

if __name__ == "__main__":
    ##speak("Hello Good Afternoon")
    wishMe()
    if 1:
        query=takeCommand().lower()
    ##logic for executing task based on input of user
    if wikipedia in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=2)
        speak("Accodring to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'openstackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'opengithub' in query:
        webbrowser.open("github.com")
    elif 'playmusic' in query:
        music_dir="F:\\Songs"
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'time' in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strtime}")
    elif 'open code' in query:
        codePath="F:\\VSCode-win32-x64-1.45.1\\Code.exe"
        os.startfile(codePath)


