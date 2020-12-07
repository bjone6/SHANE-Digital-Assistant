import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date

# Speech Recognition Constants
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Python Text-to-Speech (pyttsx3) Constants
engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

# Wake word in Listen Function
WAKE = "Shane"

# Used to store user commands for analysis
CONVERSATION_LOG = "Conversation Log.txt"

# Initial analysis of words that would typically require a Google search
SEARCH_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}


class Shane:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # Used to hear the commands after the wake word has been said
    def hear(self, recognizer, microphone, response):
        try:
            with microphone as source:
                print("Waiting for command.")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                # May reduce the time out in the future
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio)
                s.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")

    # Used to speak to the user
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    # Used to track the date of the conversation, may need to add the time in the future
    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as f:
            f.write("Conversation started on: " + today + "\n")

    # Writes each command from the user to the conversation log
    def remember(self, command):
        with open(CONVERSATION_LOG, "a") as f:
            f.write("User: " + command + "\n")

    def find_search_words(self, command):
        # Checks the first word in the command to determine if it's a search word
        if SEARCH_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:
            return True

    # Analyzes the command
    def analyze(self, command):
        try:
            # If the command starts with a search word it will do a Google search
            if self.find_search_words(command):
                s.speak("Here is what I found.")
                webbrowser.open("https://www.google.com/search?q={}".format(command))
            # Will need to expand on "open" commands
            elif command == "open youtube":
                s.speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com/channel/UCW34Ghe9-_TCA5Vy3-Agfnw")
            elif command == "introduce yourself":
                s.speak("I am Shane. I'm a digital assistant.")
            else:
                s.speak("I don't know how to do that yet.")
        except TypeError:
            pass

    # Used to listen for the wake word
    def listen(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print("Listening.")
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source, timeout=5.0)
                    response = recognizer.recognize_google(audio)
                    if response == WAKE:
                        s.speak("How can I help you?")
                        return response.lower()
                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error.")


s = Shane()
s.start_conversation_log()
while True:
    response = s.listen(recognizer, microphone)
    command = s.hear(recognizer, microphone, response)
    s.analyze(command)
