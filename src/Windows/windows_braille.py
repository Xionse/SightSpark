
#  the win32api library to create a braille display class that can display text on a braille display and doesn't need to close any connection
import win32api

class WindowsBraille:
    def __init__(self):
        pass

    def display_text(self, text):
        win32api.OutputDebugString(text)

    def close_connection(self):
        pass
