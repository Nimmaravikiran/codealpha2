import speech_recognition as sr
import pyttsx3
import DateTime
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def assistant(query, user):
    if 'time' in query:
        current_time = DateTime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif user in query:
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak("According to Wikipedia, " + result)
    else:
        speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    name = input("What is your name?  ")
    speak(f"Hello {name}! How can I assist you today?")

    while True:
        user_input = listen()
        if user_input == "exit":
            speak("Goodbye!")
            break
        elif user_input:
            assistant(query=user_input, user=name)
