#  the pybrlapi library to create a braille display class that can display text on a braille display and close the connection.

import pybrlapi

class LinuxBraille:
    def __init__(self):
        self.brl = pybrlapi.Connection()
        self.brl.open()

    def display_text(self, text):
        self.brl.writeText(text)

    def close_connection(self):
        self.brl.close()
