from Scripts.UI.Menu import Menu, DefaultButton
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class ColorScheme(Menu):
    name = "ColorScheme"

    def __init__(self, parent):
        super(ColorScheme, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu("MainPage"))
        self.RED = DefaultButton(self, "RED", 0, 0, 100, 100, "RED", lambda: self.ChangeColorScheme(Settings.COLOR_PRESETS.RED))
        self.WHITE = DefaultButton(self, "WHITE", 100, 0, 100, 100, "WHITE", lambda: self.ChangeColorScheme(Settings.COLOR_PRESETS.WHITE))
        self.OFF = DefaultButton(self, "OFF", 200, 0, 100, 100, "OFF", lambda: self.ChangeColorScheme(Settings.COLOR_PRESETS.OFF))

    def ChangeColorScheme(self, name: str = Settings.COLOR_PRESETS.RED):
        print(f"[COLOR][CURRENT] {name}")

    def Update(self):
        print(self.parentMenu.currentMenu.name)