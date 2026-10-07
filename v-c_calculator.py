import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def get_voice_by_language(language="en"):
    voices = engine.getProperty('voices')
    if not voices:
        return None

    for v in voices:
        name = v.name.lower()
        if language == "en" and "english" in name:
            return v.id
        if language == "de" and ("german" in name or "deutsch" in name):
            return v.id

    return voices[0].id

def speak(text, language="en"):
    voice_id = get_voice_by_language(language)
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

def speech_recognizer(language="en-US"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source, timeout=25)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""

def main():
    speak("Hi there! I am your voice-controlled calculator!")

    speak("Please say the first number of your calculation.")
    num1_spoken = speech_recognizer("en-US")
    print(f"First number text: {num1_spoken}")

    speak("Please say an operation: addition, subtraction, multiplication or division.")
    op_spoken = speech_recognizer("en-US")
    print(f"Operation text: {op_spoken}")

    speak("Please say the second number of your calculation.")
    num2_spoken = speech_recognizer("en-US")
    print(f"Second number text: {num2_spoken}")

    num1 = float(num1_spoken)
    num2 = float(num2_spoken)

    operation = ""

    if "add" in op_spoken or "plus" in op_spoken:
        operation = "addition"
    elif "sub" in op_spoken or "minus" in op_spoken:
        operation = "subtraction"
    elif "mul" in op_spoken or "times" in op_spoken:
        operation = "multiplication"
    elif "div" in op_spoken or "over" in op_spoken:
        operation = "division"
    else:
        operation = "unknown"

    print("Operation detected:", operation)
    result = 0

    if operation == "addition":
        result = num1 + num2
    elif operation == "subtraction":
        result = num1 - num2
    elif operation == "multiplication":
        result = num1 * num2
    elif operation == "division":
        if num2 == 0:
            speak("Cannot divide by zero. Please choose another number")
            speak("Please say a new second number.")
            new_num2_text = speech_recognizer("en-US")
            new_num2 = float(new_num2_text)
            result = num1 / new_num2
        else:
            result = num1 / num2
    else:
        result = None

    if result is not None:
        answer = "The answer is " + str(result)
        print(answer)
        speak(answer)
    else:
        speak("I did not understand the operation.")

        print("Result:", result)

if __name__ == "__main__":
    main()