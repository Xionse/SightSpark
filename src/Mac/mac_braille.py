
#  the speech library to create a braille display class that can display text on a braille display and doesn't need to close any connection.
import speech

class MacBraille:
    def __init__(self):
        pass

    def display_text(self, text):
        speech.say(text)

    def close_connection(self):
        pass
