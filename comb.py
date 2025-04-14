import webbrowser
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello, how may I help you?")
engine.runAndWait()

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# List of websites that can be opened via voice command
sites = ['google', 'facebook', 'instagram', 'chat gpt', 'youtube', 'x']

# Start listening for voice commands
for _ in range(1, 100):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Handle site opening commands
            for site in sites:
                if f"open {site}" in text.lower():
                    engine.say(f"Opening {site}")
                    engine.runAndWait()
                    # Remove space in site names like 'chat gpt' → 'chatgpt'
                    site_url = site.replace(" ", "")
                    webbrowser.open(f"https://www.{site_url}.com")
                    break  # Exit the site check loop after opening one

            # Handle stop commands
            if "stop" in text.lower() or "over" in text.lower():
                engine.say("Goodbye!")
                engine.runAndWait()
                break

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that. Could you please repeat?")
        except sr.RequestError:
            print("Speech recognition service is unavailable. Check your internet connection.")
import math
print("this is the combiantion tool:")
x=input("enter the question :")
if 'select'or'combination' in x:
    n=int(input("enter n : "))
    r=int(input("enter r : "))
    result=math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    print("the combinations is :",result)
elif 'arrangements'or'permutation' in x:
    print("this is a perm pb")
    printf("is it a string problem?")
    z=input()
    if z=='yes':
        s=input("enter the string:")
        perm=math.factorial(len(s))
        for i in s:
            perm=perm/math.factorial(s.count(i))
        else:
            print('haha')


else:
    print("this is not a related pb")
