import speech

class MacTextToSpeech:
    def __init__(self, voice='Samantha', rate=200):
        self.voice = voice
        self.rate = rate

    def say(self, text):
        speech.say(text, self.voice, self.rate)
