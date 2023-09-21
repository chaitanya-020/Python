#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pyttsx3')


# In[8]:


get_ipython().system('pip install SpeechRecognition')


# In[10]:


get_ipython().system('pip install screen-brightness-control')


# In[15]:


get_ipython().system('pip install wikipedia-api')


# In[18]:


get_ipython().system('pip install phonenumbers')


# In[20]:


get_ipython().system('pip install pywhatkit')


# In[23]:


import pyttsx3 
import speech_recognition as sr
import datetime
import screen_brightness_control as src
import wikipediaapi 
import webbrowser
import os
import smtplib
import phonenumbers
import requests
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    speak("I am Jarvis Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 0.8
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
    server.login('chaitanya20022003@gmail.com', 'message')
    server.sendmail('example@gmail.com', to, content)
    server.close()

if __name__ == "_main_":
    wishMe()
    while True:
            speak("please enter password to access Jarvis")
            Name = input("Enter Password : ")
            if Name == 'd':
                speak(' Welcome  Master..., Please tell me how may I help you')
                while True:
                        query = takeCommand().lower()
                        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                        if 'wikipedia' in query:
                            speak('Searching Wikipedia...')
                            query = query.replace("wikipedia", "")
                            results = wikipediaapi.summary(query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")

                        elif 'open google' in query:
                            webbrowser.open("google.com")

                        elif 'open stack overflow' in query:
                            webbrowser.open("stackoverflow.com")

                        elif 'play' in query:
                            song = query.replace('play', '')
                            speak('playing ' + song)
                            pywhatkit.playonyt(song) 

                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%I:%M:%p")
                            speak(f"Sir, the time is {strTime}")

                        elif 'open code' in query:
                            codePath = "C:\\Users\\adith\\AppData\\Local\\Programs\\Microsoft VS code\\code.exe"
                            os.startfile(codePath)

                        elif 'stop' in query:
                            break

                        elif 'send email' in query:
                            try:
                                speak("What should I say?")
                                content = takeCommand()
                                to = "siddhaarth@gmail.com"
                                sendEmail(to, content)
                                speak("Email has been sent!")
                            except Exception as e:
                                print(e)
                                speak("Sorry my friend. I am not able to send this email")

                        elif 'day brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(95, start=0)
                            speak("Brightness is adjusted  , enjoy the day screen light master")

                        elif 'night brightness' in query:
                            src.fade_brightness(0)
                            src.fade_brightness(25, start=0)
                            speak("Brightness is adjusted , Take care,yourself master")

                        elif 'number' in query:
                            speak("enter number master")
                            number=input('enter number')
                            from phonenumbers import geocoder
                            ch_number = phonenumbers.parse(number, "CH")
                            i=geocoder.description_for_number(ch_number, "en")
                            print(i)
                            speak("country"+i)
                            from phonenumbers import carrier
                            service_number = phonenumbers.parse(number, "RO")
                            j=carrier.name_for_number(service_number, "en")
                            print(j)
                            speak("sim "+j)


                        elif 'current location' in query:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            city = data['city']
                            location = data['loc'].split(',')
                            latitude = location[0]
                            longitude = location[1]
                            print("Latitude : ", latitude)
                            speak("Latitude" + latitude)
                            print("Longitude : ", longitude)
                            speak("Longitude" + longitude)
                            print("City : ", city)
                            speak("City" + city)


# In[ ]:




