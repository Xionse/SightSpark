# the unittest library to create test cases for the MacBraille class, it will test the display_text and close_connection methods.

import unittest
from mac import braille

class TestMacBraille(unittest.TestCase):
    def test_display_text(self):
        brl = braille.MacBraille()
        brl.display_text("Test text")
        # Additional test case for verifying the output

    def test_close_connection(self):
        brl = braille.MacBraille()
        brl.close_connection()
        # Additional test case for verifying the connection is closed

if __name__ == '__main__':
    unittest.main()
