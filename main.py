import pyttsx3  #it will help - convert text to speech
import speech_recognition as sr 
import webbrowser
import datetime     #to see the time on runtime
import pyjokes
import os
import time

# This function will convert speech to text.
def sptext():

    recognizer =  sr.Recognizer()

    with sr.Microphone() as source :
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                  print("Recongnizing....")
                  data = recognizer.recognize_google(audio)
                  print(data)
                  return data
            
            except sr.UnknownValueError :
                  print("Not Understand.")
                  return ""

# This function will convert text to speech.
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)       #0 for male voice and 1 for female voice.
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait() 
    

if __name__ == '__main__':
      
    user_input = sptext().lower()  or " "
    if user_input in "hey peter":

        while True :

            data1 = sptext().lower() 

            if "your name" in data1:
                name = "My name is peter."
                speechtx(name)

            elif "old are you" in data1:
                age = "My age is 24 years old."
                speechtx(age)

            elif 'current time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
                #   print(time)

            elif 'YouTube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'webpage' in data1:
                webbrowser.open("https://codepen.io/web-dot-dev/pen/yLojraG")

            elif 'Joke' in data1:
                joke_01 = pyjokes.get_joke(language='en', category='neutral')
                print(joke_01)
                speechtx(joke_01)

            elif 'play video' in data1:
                add = "C:\\Users\\Nkprm\\Videos\\Dragon Ball Z Super"
                listvideo = os.listdir(add)
                print(listvideo)
                os.startfile(os.path.join(add, listvideo[0]))

            elif "exit" in data1:
                 speechtx("Thank You!")
                 break
            time.sleep(5)
            
        else :
             print("Thanks!")
