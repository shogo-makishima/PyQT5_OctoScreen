WINDOW_SIZE = (800, 600)
UPDATE_PAUSE = 500

class SETTINGS:
    LED_STATUS: bool = False

class IMAGES:
    pass

class GCODE:
    PRINTER_TOOL_1 = "T0"

    CONTROLLED_MOTION_0 = "G0"
    CONTROLLED_MOTION_1 = "G1"

    CLOCKWISE_MOTION = "G2"
    COUNTERCLOCKWISE_MOTION = "G3"

UI_PATH = "Files/Images/OctoScreen_UI"

import pynput
KEYBOARD_SIMULATOR = pynput.keyboard.Controller()

class Color:
    def __init__(self, name: str, r: int, g: int, b: int, w: int):
        self.r, self.g, self.b, self.w = r, g, b, w

class COLOR_PRESETS:
    RED = "RED"
    WHITE = "WHITE"
    OFF = "OFF"

class DYNAMIC_VARIABLES:
    JobStatus: str = "Offline"

SELECTED_LANGUAGE = "ENG"

class KeyboardSymbols:
    KEYBOARD_SYMBOLS: list = []
    UPPER_CASE: bool = False

    def SwapCase(self):
        self.UPPER_CASE = not self.UPPER_CASE
        print(f"UPPER_CASE: {self.UPPER_CASE}")
        if (self.UPPER_CASE): self.Upper(self)
        else: self.Lower(self)

    def Upper(self):
        for i in range(len(self.KEYBOARD_SYMBOLS)):
            if (self.KEYBOARD_SYMBOLS[i] not in ["Caps"]):
                self.KEYBOARD_SYMBOLS[i] = self.KEYBOARD_SYMBOLS[i].upper()

    def Lower(self):
        for i in range(len(self.KEYBOARD_SYMBOLS)):
            if (self.KEYBOARD_SYMBOLS[i] not in ["Caps"]):
                self.KEYBOARD_SYMBOLS[i] = self.KEYBOARD_SYMBOLS[i].lower()

class ENG_Keyboard(KeyboardSymbols):
    KEYBOARD_SYMBOLS =  [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "+",
        "-",
        "=",
        "*",
        "_",
        "q",
        "w",
        "e",
        "r",
        "t",
        "y",
        "u",
        "i",
        "o",
        "p",
        "a",
        "s",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "z",
        "x",
        "c",
        "v",
        "b",
        "n",
        "m",
        "Caps",
        "<-",
        ",",
        ".",
        "\\",
        "?",
        "!",
        ":",
        ";",
        "\"",
        "'",
        "|",
        "/",
        "Enter",
    ]

KEYBOARDS = {
    "ENG": ENG_Keyboard,
}