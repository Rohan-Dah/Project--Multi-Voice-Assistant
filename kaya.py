import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
# print(voices[1].id)

def speak(audio): #This is defined to avoid code clotting and repetition of the same code multiple times. We can call this entire code just by calling...
    engine.say(audio)
    engine.runAndWait()

def wishme(): #This is a function used to greet the user by using the datetime module which wishes the user according to the time he is in right now..
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
      
    else:
        speak("Good evening!")
        
    speak("Hello Everyone... I am Kaaya, a multi-voice assistant designed by Mr Rohan. What do you want me to do..")
    
    #engine.setProperty('voice', voices[1].id)
    #speak("And myself Mark.. Whom do you want master Rohan to take your command?? Kaaya... Or myself?")

def takeCommand(): #This is the function which will take the microphone input from the user and will guide Kaya accordingly to return string output...

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return query 

def sendEmail(to, content):

    
wishme()   
while True:
    query = takeCommand().lower()
    #This becomes the logic for search execution...
    if 'wikipedia' in query:
        speak("Going for wikipedia... Master... Just a moment")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")   
        speak("Going for youtube... master... Just a moment")    

    elif 'open google' in query:
        webbrowser.open("google.com")   
        speak("Going for google ... master... Just a moment")        

    elif 'open chrome' in query:
        pathCrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        speak("Opening Chrome Master... Just wait for a moment")
        os.startfile(pathCrome)

    elif 'open Adobe Reader' in query:
        pathReader = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
        speak("Opening Reader Master... Just wait for a moment")
        os.startfile(pathReader)

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Master, the time is {strTime}")
        print("The time is", strTime)  

    elif 'open code' in query:
        pathCode = 'C:\Users\Asus\AppData\Local\Programs\Microsoft VS Code\Code.exe'                  
        speak("Opening VS code, Master... Just a moment")
        os.startfile(pathCode)

    elif 'email to rohan' in query:
        try:
            speak("What should I send?")
            content = takeCommand()
            to = "rohan.dahibhate@mitaoe.ac.in"
            sendEmail(to, content)
            speak("Your mail has been sent, master...!")
        except Exception as e:
            print(e)
            speak("Sorry Master... I am not able to send the mail to your recipent..")            






""

#engine.setProperty('voice', voices[2].id)
#engine.say("Hello everyone...I am kaaya... a multi-voice assistant. Nice meeting you all... Mr Rohan... what can I do for you?")
#engine.runAndWait()
