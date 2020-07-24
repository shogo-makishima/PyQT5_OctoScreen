from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class PrintFile(Menu):
    name = "PrintFile"

    def __init__(self, parent):
        super(PrintFile, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu("MainPage"))

        self.led = DefaultButton(self, "LedSwitch", 300, 0, 100, 100, "Led", lambda: parent.ChangeMenu("LedSwitch"))
        self.color = DefaultButton(self, "ColorScheme", 300, 100, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))
        self.files = FileSystemWatching(self, 0, 0, 300, 300)

    def Update(self):
        print(self.parentMenu.currentMenu.name)