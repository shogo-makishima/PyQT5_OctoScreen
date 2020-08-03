from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching, ListWidget, DefaultButton_WithLine
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

        self.back = DefaultButton_WithLine(self, "Back", 575, 400, 200, 128, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True), imageName="back", color="rgb(180, 223, 71)")
        self.update = DefaultButton_WithLine(self, "Update", 575, 200, 200, 128, "Update", self.UpdateFiles, imageName="refresh", color="rgb(221, 108, 43)")

        # self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True))

        # self.led = DefaultButton(self, "Update", 300, 0, 100, 100, "Update", self.UpdateFiles)
        # self.color = DefaultButton(self, "ColorScheme", 300, 100, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))

        self.files = ListWidget(self, "Files", 0, 0, 575, 600, self.GetFile)

        """
        self.files = FileSystemWatching(self, 0, 0, 300, 300, self.GetFile)
        """

    def Start(self):
        self.UpdateFiles()

    def GetFile(self, signal):
        file_path = self.files.model.itemFromIndex(signal).text()
        if (file_path[-5:] == "gcode"):
            OctoPrintAPI.SelectFile(OctoPrintAPI, file_path)
            self.parent().ChangeMenu("MainPage")

        #if (not self.files.fileSystem.isDir(signal)):
            #file_path = self.files.fileSystem.filePath(signal)
            #if (file_path[-5:] == "gcode"):
                #OctoPrintAPI.SelectFile(OctoPrintAPI, file_path)
                #self.parent().ChangeMenu("MainPage")

    def UpdateFiles(self):
        print("; ".join([file.filePath for file in OctoPrintAPI.FILES]))
        self.files.SetItems([file.filePath for file in OctoPrintAPI.FILES])

    def Update(self):
        pass
        # self.files.SetItems([file.filePath for file in OctoPrintAPI.FILES])
        # print(self.parentMenu.currentMenu.name)