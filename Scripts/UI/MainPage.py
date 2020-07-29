from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching, DefaultButton_WithLine
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI

class MainPage(Menu):
    name = "MainPage"

    def __init__(self, parent):
        super(MainPage, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        # self.statusBar = AnimationTextEdit(self, 75, 250, 250, 50, "", speed=1, pause=20)

        self.t0Status = DefaultButton(self, "t0Status", 150, 25, 128, 128, "", None, isButton=False, imageName="extruder-1")
        # self.t1Status = DefaultButton(self, "t1Status", 250, 25, 128, 128, "", None, isButton=False, imageName="extruder-2")
        # self.t2Status = DefaultButton(self, "t2Status", 50, 200, 128, 128, "", None, isButton=False,imageName="extruder-3")
        # self.t3Status = DefaultButton(self, "t3Status", 250, 200, 128, 128, "", None, isButton=False,imageName="extruder-4")
        self.bedStatus = DefaultButton(self, "bedStatus", 150, 375, 128, 128, "", None, isButton=False,imageName="bed")

        self.home = DefaultButton_WithLine(self, "Home", 380, 25, 200, 128, "Home", lambda: parent.ChangeMenu("PrintingMenu"), color="rgb(162, 37, 124)")
        self.bedLevel = DefaultButton_WithLine(self, "BedLevel", 580, 25, 200, 128, "Bed Level", lambda: print(1), imageName="bed-level", color="rgb(180, 223, 71)")
        self.Filament = DefaultButton_WithLine(self, "Filament", 380, 200, 200, 128, "Filament", lambda: print(1), imageName="filament", color="rgb(64, 144, 131)")
        self.menu = DefaultButton_WithLine(self, "MainMenu", 580, 200, 200, 128, "Menu", lambda: parent.ChangeMenu("MainMenu"), imageName="control", color="rgb(221, 108, 43)")

        self.print = DefaultButton_WithLine(self, "PrintFile", 380, 375, 400, 128, "PrintFile", lambda: parent.ChangeMenu("PrintFile"), imageName="print", color="rgb(162, 37, 124)")

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
        self.t0Status.setText(f"{round(OctoPrintAPI.TOOLS['tool0'].actual)}°C / {round(OctoPrintAPI.TOOLS['tool0'].target)}°C")
        # self.t1Status.setText(f"{round(OctoPrintAPI.TOOLS['tool1'].actual)}°C / {round(OctoPrintAPI.TOOLS['tool1'].target)}°C")
        # self.t2Status.setText(f"{round(OctoPrintAPI.TOOLS['tool1'].actual)}°C / {round(OctoPrintAPI.TOOLS['tool1'].target)}°C")
        # self.t3Status.setText(f"{round(OctoPrintAPI.TOOLS['tool1'].actual)}°C / {round(OctoPrintAPI.TOOLS['tool1'].target)}°C")
        self.bedStatus.setText(f"{round(OctoPrintAPI.TOOLS['bed'].actual)}°C / {round(OctoPrintAPI.TOOLS['bed'].target)}°C")
        # self.statusBar.SetText(f"[STATUS] {OctoPrintAPI.JOB.state}")