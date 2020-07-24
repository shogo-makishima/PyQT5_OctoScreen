from Scripts.UI.Menu import Menu, DefaultButton
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class LedSwitch(Menu):
    name = "LedSwitch"

    def __init__(self, parent):
        super(LedSwitch, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu("MainPage"))
        self.ledON = DefaultButton(self, "LedON", 0, 0, 100, 100, "ON", lambda: self.LedChangeState(True))
        self.ledOFF = DefaultButton(self, "LedOFF", 300, 0, 100, 100, "OFF", lambda: self.LedChangeState(False))


    def LedChangeState(self, state: bool = False):
        Settings.SETTINGS.LED_STATUS = state
        print(f"[LED][CURRENT] {Settings.SETTINGS.LED_STATUS}")

    def Update(self):
        print(self.parentMenu.currentMenu.name)