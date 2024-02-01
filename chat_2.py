from datetime import datetime as dt
import os, glob, random

chat = True

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date", "date", "tell me date", "please tell me today's date"]
timeIntent = ["time", "what's the time", "tell me time", "time please"]
musicIntent = ["play song", "play music", "please play a song"]

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Today's date :",date.strftime("%d %b, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Current time :",time.strftime("%H:%M:%S, %p"))
    elif msg in musicIntent:
        path = r"D:\Batches\Songs\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        current_song = random.choice(songs)
        os.startfile(current_song)
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand")

