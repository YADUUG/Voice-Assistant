import speech_recognition as sr
import pyttsx3
import datetime

recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't process your request. Please try again later.")
        return ""

def greet():
    speak("Hello! How can I help you today?")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak("The current time is " + current_time)

def get_date():
    today = datetime.date.today()
    speak("Today is " + today.strftime("%B %d, %Y"))

def main():
    greet()
    
    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there!")
        elif "time" in command:
            get_time()
        elif "date" in command:
            get_date()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
