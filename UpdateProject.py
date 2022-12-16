import pywhatkit as pwt
import speech_recognition as va
import time
import pyttsx3
import pywhatkit
import datetime
#Search Bar Source: https://www.youtube.com/watch?v=8IV7PFFBVZU
#Add delay: https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
#Voice Recognition source:https://www.youtube.com/watch?v=AWvsXxDtEkU 


print("Hello Welcome to Bob where we are able to search up video using Speech Recognition or Search Bar")
print("Enter 1 to use Bob Speech Recognition")
print("or")
print("Enter 2 to use the Search Bar")

time.sleep(2.0)
userInput = int(input())

if userInput == 1:
    listener = va.Recognizer()
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    def bob_talk(myMessage):
        myEngine.say(text)
        myEngine.runAndWait()
    def take_command():
        try:
            with va.Microphone() as source:
                print('Say song title and artist')
                print("Listening for voice...")
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
        command = take_command()
        print(command)
        if 'play' in command:
            mySong = command.replace('play', '')
            bob_talk('playing' + mySong)
            pywhatkit.playonyt(mySong)
    run_bob()

elif userInput == 2:
    count = 0
    print("Enter how many video you want to search up: ")
    videoSearches =int(input())

    if videoSearches <= 0:
        print("Invalid Input please")
        print("Enter a valid input: ")
        time.sleep(2.0)
        videoSearches = int(input())
        while (count < videoSearches):   
            count = count + 1
            searchBar = input("Enter a Title: ")
            searchBar.upper()
            pwt.playonyt(searchBar)

            print(f"You have entered: {searchBar}")

    else:
        while (count < videoSearches):   
            count = count + 1
            searchBar = input("Enter a Title: ")
            searchBar.upper()
            pwt.playonyt(searchBar)

            print(f"You have entered: {searchBar}")


else:
    print("Sorry wrong input please try again")