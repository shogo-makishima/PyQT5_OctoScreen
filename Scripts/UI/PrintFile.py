from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI

class PrintFile(Menu):
    name = "PrintFile"

    def __init__(self, parent):
        super(PrintFile, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu("MainPage"))

        # self.led = DefaultButton(self, "LedSwitch", 300, 0, 100, 100, "Led", lambda: parent.ChangeMenu("LedSwitch"))
        # self.color = DefaultButton(self, "ColorScheme", 300, 100, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))

        self.files = FileSystemWatching(self, 0, 0, 300, 300, self.GetFile)

    def GetFile(self, signal):
        if (not self.files.fileSystem.isDir(signal)):
            file_path = self.files.fileSystem.filePath(signal)
            if (file_path[-5:] == "gcode"):
                OctoPrintAPI.SelectFile(OctoPrintAPI, file_path)
                self.parent().ChangeMenu("MainPage")


    def Update(self):
        print(self.parentMenu.currentMenu.name)