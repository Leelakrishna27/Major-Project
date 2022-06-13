import cv2
import numpy as npy
import mediapipe as mp
import tensorflow as tf
import pyttsx3
import datetime
import pyaudio
import smtplib
import time
import webbrowser as web
import speech_recognition as sr
import wikipedia
from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
import pywhatkit as kit
from playsound import playsound


def selectVoice():
    print('voice')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[2].id)
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            speak("Good Morning!")
        elif 12 <= hour < 16:
            speak("Good Afternoon")
        elif 16 <= hour < 19:
            speak("Good Afternoon")
        else:
            speak("Good Night")

    def takeCommand():
        # It takes mic input from user and returns string output.
        r = sr.Recognizer()
        # print(filename)
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        '''with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio = r.record(source)
            # recognize (convert from speech to text)'''

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said:", query)

        except Exception:
            # print(e)
            print("Say that again please...")
            # speak("Say that again please...")
            return "None"
        return query

    def sendEmail(tom, conte):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('leelakrishna542@gmail.com', 'jzuwnznxmuodjxbo') #nzicgdwqvdzxhtwa
        server.sendmail('leelakrishna542@gmail.com', tom, conte)
        server.close()

    def ytsong(query):
        query = query.replace("play", "")
        speak('Playing ' + query + 'in youtube')
        kit.playonyt(query)

    def files(query):
        query = query.replace('create', '')
        f = open("C:\\Users\\Leela Krishna\\Documents\\{0}.txt".format(query), "w")
        speak('Please tell the content')
        cont = takeCommand().lower()
        f.write(cont)
        speak('Content saved in the {0} file'.format(query))

    def searchfun(query):
        query = query.replace("search", "")
        speak('Searching ' + query + 'in google')
        kit.search(query)

    def shutdown():
        speak("Yes User, terminating all the processes")
        speak("going offline.Shutting down your computer, See you next time.")
        os.system("sleep -s")

    def sleep():
        speak("OK User, I am going to sleep")
        os.system("shutdown -s")

    if __name__ == "__main__":
        wishMe()
        speak("Hello User.")
        speak("I am Alida. How may I help you?")
        while 1:
            query = takeCommand().lower()
            if 'hello' in query:
                speak("yes how may I help you")
                query = takeCommand().lower()
                # logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                elif 'create' in query:
                    files(query)
                elif 'your name' in query:
                    speak('I\'m Alida, nice to meet you')
                elif 'wish me' in query:
                    wishMe()
                elif 'open youtube' in query:  # youtube
                    web.open("https://www.youtube.com/")
                elif 'play' in query:
                    ytsong(query)
                elif 'search' in query:
                    searchfun(query)
                elif 'open google' in query:  # google
                    web.open("https://www.google.com/?gws_rd=ssl")
                elif 'open stack overflow' in query:  # youtube
                    web.open("https://stackoverflow.com/")
                elif 'open schools' in query:  # google
                    web.open("https://www.w3schools.com/java/")
                elif 'open medicals' in query:  # youtube
                    kit.search("hospitals near me")
                elif 'open github' in query:  # google
                    web.open("https://github.com/")
                elif 'open music' in query:  # music
                    music_dir = 'C:\\Users\\Leela Krishna\\Music'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[1]))
                elif 'open downloads' in query:
                    dir_down = 'C:\\Users\\Leela Krishna\\Downloads'
                    os.startfile(dir_down)
                elif 'open photos' in query:
                    dir_pic = 'C:\\Users\\Leela Krishna\\Pictures'
                    pic = os.listdir(dir_pic)
                    os.startfile(os.path.join(dir_pic, pic[1]))
                elif 'open videos' in query:
                    dir_vid = 'C:\\Users\\Leela Krishna\\Videos\\song videos'
                    vid = os.listdir(dir_vid)
                    os.startfile(os.path.join(dir_vid, vid[0]))
                elif 'open documents' in query:
                    dir_vid = 'C:\\Users\\Leela Krishna\\Documents'
                    # vid = os.listdir(dir_vid)
                    os.startfile(os.path.join(dir_vid))
                elif 'the time' in query:  # time
                    nowtime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"now the time is {nowtime}")
                elif 'open mail' in query:
                    web.open('https://mail.google.com/mail/u/1/#inbox')
                elif 'send email' in query:  # mail
                    try:
                        speak("What should I say")
                        content = takeCommand()
                        to = "leelakrishna542@gmail.com"
                        sendEmail(to, content)
                        speak("Mail has been sent")
                        print("Mail has been sent")
                    except Exception as e:
                        print(e)
                        speak("Sorry leela. Not able to send this mail at the moment")
                elif 'shutdown' in query:  # shutdown
                    shutdown()
                elif 'nothing' in query:
                    speak(' Okay! thats cool')
                elif 'quit' in query:  # quit
                    break
                elif 'sleep' in query:  # sleep
                    sleep()


def selectTranslation():
    root.withdraw()

    print('Gesture')

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[2].id)
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    # Load the gesture recognizer model
    model = load_model('mp_hand_gesture')

    # Load class names
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    print(classNames)

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read each frame from the webcam
        _, frame = cap.read()

        x, y, c = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get hand landmark prediction
        result = hands.process(framergb)

        # print(result)

        className = ''

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                # print(prediction)
                classID = npy.argmax(prediction)
                className = classNames[classID]
        if className.lower() == "rock":
            speak("Yeah, I'm fine")
        elif className.lower() == "stop":
            cap.release()
            cv2.destroyAllWindows()
            root.deiconify()
            break
        elif className.lower() == "call me":
            speak("Please call me")
            className = "Please call me"
        elif className.lower() == "fist":
            speak("lets do this")
            className = "lets do this"
        elif className.lower() == "thumbs up":
            speak("Give me some water")
            className = "Give me some water"
        elif className.lower() == "thumbs down":
            speak("No, it's not right")
            className = "No, it's not right"
        elif className.lower() == "live long":
            speak("are you fine?")
            className = "are you fine?"
        elif className.lower() == "smile":
            speak("smile please")
            className = "smile please"
        elif className.lower() == "okay":
            speak("It's awesome")
            className = "It's awesome"
        elif className.lower() == "peace":
            speak("Hello friend")
            className = "Hello friends"

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.LINE_AA)

        # Show the final output
        imag = cv2.imread('handphoto.png', 1)
        cv2.imshow('Image2', imag)
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # release the webcam and destroy all active windows
    cap.release()

    cv2.destroyAllWindows()


def selectOperation():
    root.withdraw()

    # img = ImageTk.PhotoImage(Image.open("handphoto.jpg"))
    # lab = Label(roo, image=img).pack()

    cap = cv2.VideoCapture(0)

    npHands = mp.solutions.hands
    hands = npHands.Hands()
    npDraw = mp.solutions.drawing_utils

    pTime = 0
    cTime = 0
    global i
    i = 2

    def FindNumber(pos, found):
        # 1-2,3-4 thumb
        vec1 = npy.array(pos[3])
        vec2 = npy.array(pos[4])
        vec1 = vec1 - vec2
        vec2 = npy.array(pos[1])
        temp = npy.array(pos[2])
        vec2 = vec2 - temp
        temp = npy.dot(vec1, vec2)
        if temp > 950:
            found += 1
        # 5-6,7-8 index
        vec1 = npy.array(pos[7])
        vec2 = npy.array(pos[8])
        vec1 = vec1 - vec2
        vec2 = npy.array(pos[5])
        temp = npy.array(pos[6])
        vec2 = vec2 - temp
        temp = npy.dot(vec1, vec2)
        if temp > 0:
            found += 1
        # 9-10,11-12 middel finger
        vec1 = npy.array(pos[11])
        vec2 = npy.array(pos[12])
        vec1 = vec1 - vec2
        vec2 = npy.array(pos[9])
        temp = npy.array(pos[10])
        vec2 = vec2 - temp
        temp = npy.dot(vec1, vec2)
        if temp > 0:
            found += 1
        # 13-14,15-16 ring finger
        vec1 = npy.array(pos[15])
        vec2 = npy.array(pos[16])
        vec1 = vec1 - vec2
        vec2 = npy.array(pos[13])
        temp = npy.array(pos[14])
        vec2 = vec2 - temp
        temp = npy.dot(vec1, vec2)
        if temp > 0:
            found += 1
        # 17-18,19-22 pinky
        vec1 = npy.array(pos[19])
        vec2 = npy.array(pos[20])
        vec1 = vec1 - vec2
        vec2 = npy.array(pos[17])
        temp = npy.array(pos[18])
        vec2 = vec2 - temp
        temp = npy.dot(vec1, vec2)
        if temp > 0:
            found += 1
        return found

    iter = 2
    ed = 2
    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        number = 0
        if results.multi_hand_landmarks:
            i = 0
            for handLms in results.multi_hand_landmarks:
                N = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * h), int(lm.y * w)
                    N.append([cx, cy])
                number = FindNumber(N, number)
                npDraw.draw_landmarks(img, handLms, npHands.HAND_CONNECTIONS)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, "Fps: " + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                    1, (255, 0, 255), 1)
        num = str(int(number))
        cv2.putText(img, num, (int(100), int(100)), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 255), 3)
        if num == '2':
            web.open("https://www.youtube.com/")
        elif num == '1':
            web.open("https://www.google.com/")
        elif num == '3':
            dir_pic = 'C:\\Users\\Leela Krishna\\Pictures'
            pic = os.listdir(dir_pic)
            os.startfile(os.path.join(dir_pic, pic[1]))
        elif num == '4':
            dir_vid = 'C:\\Users\\Leela Krishna\\Videos\\song videos\\avid1.mp4'
            # vid = os.listdir(dir_vid)
            os.startfile(dir_vid)  # os.path.join(dir_vid, vid[0])
        elif num == '5':
            cap.release()
            cv2.destroyAllWindows()
            root.deiconify()
            break
        elif num == '6':
            if (iter % 2 != 0):
                os.system("taskkill /f /im notepad.exe")
                iter += 1
            else:
                os.startfile('notepad.exe')
                iter += 1
        elif num == '7':
            dir_doc = 'C:\\Users\\Leela Krishna\\Documents'
            #doc = os.listdir(dir_doc)
            os.startfile(os.path.join(dir_doc))
        elif num == '8':
            os.system('cmd /c control')




        imag = cv2.imread('handphoto.png', 1)
        cv2.imshow("Image", img)
        cv2.imshow('Image2', imag)

        cv2.waitKey(500)


def selectGesture():
    r.withdraw()

    global root
    root = Toplevel()
    root.title('Gesture')
    root.geometry('700x300')

    def destroy():
        root.destroy()
        r.deiconify()

    img = ImageTk.PhotoImage(Image.open("image-removebg-preview.png"))
    lab = Label(root, image=img).pack(side=tk.TOP)

    button = Button(root, text='Translation', width=25, command=selectTranslation)
    button.pack(side=tk.LEFT)
    button1 = Button(root, text='Operation', width=25, command=selectOperation)
    button1.pack(side=tk.RIGHT)

    qt = Button(root, text="Back", command=destroy)
    qt.pack(side=tk.BOTTOM)
    button2 = Button(root, text='Stop', width=25, command=r.destroy)
    button2.pack(side=tk.BOTTOM, pady=10)

    root.mainloop()


global r
r = tk.Tk()
r.geometry('700x300')
r.title('Voice and Gesture operations')
img = ImageTk.PhotoImage(Image.open("image-removebg-preview.png"))
lab = Label(r, image=img).pack(side=tk.TOP)
button = tk.Button(r, text='Voice', width=25, command=selectVoice)
button.pack(side=tk.LEFT)
button1 = tk.Button(r, text='Gesture', width=25, command=selectGesture)
button1.pack(side=tk.RIGHT)
button2 = tk.Button(r, text='Stop', width=25, command=r.destroy)
button2.pack(side=tk.BOTTOM, pady=10)
button.pack()
playsound('C:\\Users\\Leela Krishna\\Downloads\\intro.wav')
r.mainloop()
