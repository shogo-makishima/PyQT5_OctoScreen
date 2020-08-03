from Scripts.UI.Menu import Menu, DefaultButton, DefaultButton_WithLine
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets

class MainMenu(Menu):
    name = "MainMenu"

    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.move = DefaultButton_WithLine(self, "Move", 0, 72, 200, 128, "Move", lambda: parent.ChangeMenu("MovingMenu"), imageName="move", color="rgb(221, 108, 43)")
        self.toolChanger = DefaultButton_WithLine(self, "ToolChanger", 200, 72, 200, 128, "ToolChanger", lambda: print(1), imageName="toolchanger", color="rgb(162, 37, 124)")
        self.control = DefaultButton_WithLine(self, "Control", 400, 72, 200, 128, "Control", lambda: print(1), imageName="control", color="rgb(180, 223, 71)")
        self.system = DefaultButton_WithLine(self, "System", 600, 72, 200, 128, "System", lambda: print(1), imageName="info", color="rgb(64, 144, 131)")
        self.temperature = DefaultButton_WithLine(self, "Temperature", 0, 400, 200, 128, "Temperature", lambda: print(1), imageName="heat-up", color="rgb(162, 37, 124)")
        self.network = DefaultButton_WithLine(self, "Network", 200, 400, 200, 128, "Network", lambda: parent.ChangeMenu("NetworkMenu"), imageName="network", color="rgb(221, 108, 43)")
        self.preset = DefaultButton_WithLine(self, "Preset", 400, 400, 200, 128, "Preset", lambda: print(1), imageName="files", color="rgb(64, 144, 131)")
        # self.resume = DefaultButton_WithLine(self, "Resume", 600, 400, 200, 128, "Resume", lambda: print(1), imageName="resume", color="rgb(162, 37, 124)")

        self.back = DefaultButton_WithLine(self, "Back", 600, 400, 200, 128, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True), imageName="back", color="rgb(180, 223, 71)")

    def LedChangeState(self, state: bool = False):
        Settings.SETTINGS.LED_STATUS = state
        print(f"[LED][CURRENT] {Settings.SETTINGS.LED_STATUS}")

    def Update(self):
        pass
        # print(self.parentMenu.currentMenu.name)