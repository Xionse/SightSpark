
# the unittest library to create test cases for the LinuxTextToSpeech class, it will test the say method.

import unittest
from windows import text_to_speech

class TestWindowsTextToSpeech(unittest.TestCase):
    def test_say(self):
        tts = text_to_speech.WindowsTextToSpeech()
        tts.say("Test text")


if __name__ == '__main__':
    unittest.main()