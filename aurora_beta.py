import webbrowser
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello, how may I help you?")
engine.runAndWait()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Predefined list of websites to open
sites = ['google', 'facebook', 'instagram', 'chat gpt', 'youtube', 'x']

# Start listening in a loop
for _ in range(1, 100):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Check if any known command is spoken
            for site in sites:
                if f"open {site}" in text.lower():
                    engine.say(f"Opening {site}")
                    engine.runAndWait()
                    webbrowser.open(f"https://www.{site.replace(' ', '')}.com")
                    break  # Exit after opening the site

            # Stop condition
            if "stop" in text.lower() or "over" in text.lower():
                engine.say("Goodbye!")
                engine.runAndWait()
                break

        except sr.UnknownValueError:
            print("Sorry, I did not understand you. Could you repeat that?")
        except sr.RequestError:
            print("API request failed. Check your internet connection and try again.")
