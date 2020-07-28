WINDOW_SIZE = (400, 300)
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


class Color:
    def __init__(self, name: str, r: int, g: int, b: int, w: int):
        self.r, self.g, self.b, self.w = r, g, b, w

class COLOR_PRESETS:
    RED = "RED"
    WHITE = "WHITE"
    OFF = "OFF"

class DYNAMIC_VARIABLES:
    JobStatus: str = "Offline"