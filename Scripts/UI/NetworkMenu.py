from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching, DefaultButton_WithLine
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI

class NetworkMenu(Menu):
    name = "NetworkMenu"

    def __init__(self, parent):
        super(NetworkMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        # self.statusBar = AnimationTextEdit(self, 75, 250, 250, 50, "", speed=1, pause=20)
        self.back = DefaultButton_WithLine(self, "Back", 600, 400, 200, 128, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True), imageName="back", color="rgb(180, 223, 71)")

        # self.led = DefaultButton(self, "LedSwitch", 0, 0, 100, 100, "Led", lambda: parent.ChangeMenu("LedSwitch"))
        # self.color = DefaultButton(self, "ColorScheme", 100, 0, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))
        # self.printFile = DefaultButton(self, "PrintFile", 200, 0, 100, 100, "Print", lambda: parent.ChangeMenu("PrintFile", OctoPrintAPI.JOB.state == "Operational"))
        # self.printingMenu = DefaultButton(self, "PrintingMenu", 300, 0, 100, 100, "Printing", lambda: parent.ChangeMenu("PrintingMenu"))

        # self.temperatureMenu = DefaultButton(self, "TemperatureMenu", 100, 100, 100, 100, "Heat", lambda: parent.ChangeMenu("TemperatureMenu"))

        # self.movingMenu = DefaultButton(self, "MovingMenu", 0, 100, 100, 100, "Move", lambda: parent.ChangeMenu("MovingMenu", OctoPrintAPI.JOB.state == "Operational"))

        # self.presetsMenu = DefaultButton(self, "PresetsMenu", 200, 100, 100, 100, "Preset", lambda: parent.ChangeMenu("PresetsMenu", OctoPrintAPI.JOB.state in ["Paused", "Pausing", "Printing"]))

        self.Update()
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def Update(self):
        pass