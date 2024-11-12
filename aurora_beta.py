import webbrowser
import pyttsx3
engine=pyttsx3.init()
engine.say("hello , how may i help you?")
engine.runAndWait()

import speech_recognition as sr
recognizer=sr.Recognizer()
for i in range(1,100):
    with sr.Microphone() as source:
        print("listening...")
        audio=recognizer.listen(source)
        
        try:
            text=recognizer.recognize_google(audio)
            print("you said :",text)
            x=['google','facebook','instagram','chat gpt','youtube','x']
            for i in x:
                if (f"open {i}") in text.lower():
                    engine.say(f"opening {i}")
                    webbrowser.open(f"www.{i}.com")
                    engine.runAndWait()
            break
            if (("stop")or("over")) in text.lower():
                    break
        except sr.UnknownValueError:
            print("Sorry i did not understand you , could you repeat what you just said?")
        except sr.RequestError:
            print("Unable to request api , check your connection and please try again.")



