import speech_recognition as sr
import googlesearch
import webbrowser
import time
#INITIATING RECOGNIZER
recognizer=sr.Recognizer()


while True:
    #WE HAVE TO SPECIFY THE SOURCE. HERE WE USE MICORPHONE AS THE SOURCE FILE
    # IF WE WANT A RECORDED FILE AS SOURCE THEN WE WILL USE
    # with sr.AudioFile(filename) as source:
    with sr.Microphone() as source:
        #CLEARING SOUND OF VOICE

        print('Adjusting voice')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('recording audio')
        #RECORDING THE AUDIO

        audio=recognizer.listen(source,timeout=4)

        try:

            #GETTING THE TEXT USING GOOGLE API

            text=recognizer.recognize_google(audio,language='en-US')
            print(text)
            print("Start searching")

            #SEARCHING ON GOOGLE USING GOOLESEARCH LIBRABRY
            search=googlesearch.search(text,tld='com',lang='en',num=1,start=0,stop=1,pause=1.5)


            for j in search:
                print(j)
            #OPENING WEB BROWSER TO OPEN WITH URL OF TOP RESULT

                browser=webbrowser.open_new(j)
        except sr.UnknownValueError:
            print('Error')
        except sr.RequestError:
            print('request error')
        time.sleep(10)
