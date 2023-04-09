import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell

import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import twilio
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Hello Dear !")

	elif hour>= 12 and hour<18:
		speak("Hello Dear !")

	else:
		speak("Hello Dear !")

	assname =("Doctor Ai")
	speak("I am your AI Doctor")
	speak(assname)
	

def username():
	
	
	
	
	
	speak("How can i Help you,")
	speak("What are you suffering from,")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query



if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
	
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)


		elif 'i am having fever' in query:
			speak("Suffering From common cold and viral fever. Given Medicin is required to take. 1 , Paracetamol 2, Calpol.")


		elif 'fever' in query:
			speak("Suffering From common cold and viral fever. Given Medicin is required to take. 1 , Paracetamol 2, Calpol.")
			


		elif 'what should i eat' in query:
			speak("You should eat , Dal, Roti , Fruits")
			

		elif 'any other suggestions' in query or "good" in query:
			speak("Take rest and avoid to eat cold foods.")


		elif 'Write the prescription' in query:
			

				
				speak('here is your prescription')
				print('''                 UNI HOSPITAL          
Phone : +91 987655432           Email : uni@hospital.com
__________________________________________________________
                   Patient Details             
       Name : hritik      Age : 20     Sex : M    
       Weight : 60        Address : Jalandhar
       Phone : 6206180458          Date : 2023-04-10
       Illness : Fever     Medical History : none
__________________________________________________________
About illness : Suffering From common cold and viral fever. Given Medicin is required to take. 

Medicines Given :
- Paracetamol 
- Calpol 
- Telmikind Am 

Foods to Eat : 
- Dal 
- Roti 
- Fruits 

 Note : Take rest and avoid to eat cold foods. 
            ~~~~ Get Well Soon ~~~~   '''+ '\n')
				
			

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		

		elif "what is prescription of fever" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		
		elif "show prescription" in query:
			speak("Showing prescription")
			file = open("hritik.txt", "r")
			print(file.read())
			speak(file.read(6))


			speak(assname)

	

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		
		elif "what is" in query or "who is" in query:
			
		
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

	