import speech_recognition as sr
import pyttsx3

def speak(text, language="en"):
    engine=pyttsx3.init()
    engine.setProperty('rate', 150)
    voices=engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[100].id)
    else:
        engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()

def speech_recognizer():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak in english. What is your name?")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        print("Could not Understand audio. try moving somewhere quieter or speaking closer to the microphone.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""

def main():
    name = speech_recognizer()
    greeting = f"Hello {name}! Nice to meet you and welcome to Python!"
    speak(greeting, language="en")
    print(greeting)

if __name__ == "__main__":
    main()