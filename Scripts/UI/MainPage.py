from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class MainPage(Menu):
    name = "MainPage"

    def __init__(self, parent):
        super(MainPage, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        testText = "Temperature: 10°C; Humidity: 30%;"
        self.statusBar = AnimationTextEdit(self, 75, 250, 250, 50, testText)

        self.led = DefaultButton(self, "LedSwitch", 0, 0, 100, 100, "Led", lambda: parent.ChangeMenu("LedSwitch"))
        self.color = DefaultButton(self, "ColorScheme", 100, 0, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))
        self.printFile = DefaultButton(self, "PrintFile", 200, 0, 100, 100, "Print", lambda: parent.ChangeMenu("PrintFile"))
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def Update(self):
        print(self.parentMenu.currentMenu.name)