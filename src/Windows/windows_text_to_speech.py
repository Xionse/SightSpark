import win32com.client as wincl

class WindowsTextToSpeech:
    def __init__(self, rate=200):
        self.rate = rate
        self.speak = wincl.Dispatch("SAPI.SpVoice")
        self.speak.Rate = self.rate

    def say(self, text):
        self.speak.Speak(text)
