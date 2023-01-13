import pyttsx3

class LinuxTextToSpeech:
    def __init__(self, voice='en', rate=200):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('voice', voice)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

