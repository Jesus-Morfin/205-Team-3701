#Courses: CST-205
#Title: Bob Voice Recognition/Search bar
#Abstract: This is a project to use speech Recoginition to search up Youtube video and
#the search bar to search up video.
#Authors:  Javier Dominguez, Ricardo Nunez Lopez, Jesus Morfin
#Date: December 14, 2022

#Who worked on what:
#Ricardo and Javier did the research for the speech recognition did of couple of test
#Jesus worked on the Search bar and Javier tested it functionality

#Sources Below:
#Search Bar Source: https://www.youtube.com/watch?v=8IV7PFFBVZU
#Add delay: https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
#Voice Recognition source:https://www.youtube.com/watch?v=AWvsXxDtEkU 


import pywhatkit as pwt
import speech_recognition as va
import time
import pyttsx3
import pywhatkit
import datetime

#The code between line 26-29 tells the user the option to choose between 1 and 2
print("Hello Welcome to Bob where we are able to search up video using Speech Recognition or Search Bar")
print("Enter 1 to use Bob Speech Recognition")
print("or")
print("Enter 2 to use the Search Bar")

#Line 32 is to add a time delay to have the code above print before asking the user for an input
time.sleep(2.0)
userInput = int(input())

if userInput == 1:
    listener = va.Recognizer()
    myEngine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    def bob_talk(text):
        myEngine.say(text)
        myEngine.runAndWait()
    def take_command():
        try:
            with va.Microphone() as source:
                print("Listening to voice...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'bob' in command:
                    command = command.replace('bob', '')
                    print(command)
        except:
            pass
        return command
    def run_bob():
        #bob runs the command
        command = take_command()
        print(command)
        if 'play' in command:
            mySong = command.replace('play', '')
            bob_talk('playing' + mySong)
            pywhatkit.playonyt(mySong)
    run_bob()

#If the user enters 2 it will take them to the search bar
elif userInput == 2:
    #Line 73 to 75 will have a counter for the amount of video then want to search up.
    count = 0
    print("Enter how many video you want to search up: ")
    videoSearches =int(input())
    #Line 77 will check if the counter is less than zero then give them an invalid input and to enter another number
    if videoSearches <= 0:
        print("Invalid Input please")
        print("Enter a valid input: ")
        time.sleep(2.0)
        videoSearches = int(input())
        #Line 83 will run until count is greater than videoSearches
        while (count < videoSearches):   
            count = count + 1
            searchBar = input("Enter a Title: ")
            searchBar.upper()
            pwt.playonyt(searchBar)
            #Print out what they have searched
            print(f"You have entered: {searchBar}")

    else:
        #Look at line 83 for comment
        while (count < videoSearches):   
            count = count + 1
            searchBar = input("Enter a Title: ")
            searchBar.upper()
            pwt.playonyt(searchBar)
            #Look at line 88 for comment
            print(f"You have entered: {searchBar}")

#Will print an invalid statement and will have to run Powershell again.
else:
    print("Sorry wrong input please try again")
