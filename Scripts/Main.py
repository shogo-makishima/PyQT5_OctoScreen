from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import asyncio
from Scripts.UI.Menu import Menu
from Scripts.UI.MainPage import MainPage
from Scripts.UI.LedSwitch import LedSwitch
from Scripts.UI.ColorScheme import ColorScheme
from Scripts.UI.PrintFile import PrintFile
from Scripts.UI.PrintingMenu import PrintingMenu
from Scripts.UI.MovingMenu import MovingMenu
from Scripts.UI.TemperatureMenu import TemperatureMenu
from Scripts.UI.PresetsMenu import PresetsMenu, CreatePresetsMenu
from Scripts.API.OctoPrintAPI import OctoPrintAPI, COMMANDS, Profile

class Main(QtWidgets.QWidget):
    def __init__(self):
        self.Start()

        super().__init__()

        self.ListMenus: Menu = [
            Menu(self),
            MainPage(self),
            LedSwitch(self),
            ColorScheme(self),
            PrintFile(self),
            PrintingMenu(self),
            MovingMenu(self),
            TemperatureMenu(self),
            PresetsMenu(self),
            CreatePresetsMenu(self),
        ]

        font = QtGui.QFont("Trench", 30)

        self.setObjectName("Menu")
        self.setGeometry(100, 100, Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.currentMenu: Menu = self.GetMenuByName("MainPage")
        print(f"[MENU][CURRENT] {self.currentMenu.name}")

        self.timer = QtCore.QTimer(self)
        self.timer.start(Settings.UPDATE_PAUSE)
        self.timer.timeout.connect(lambda: self.UpdateChildMenu())

        self.setStyleSheet("background-color: black;")
        # self.setStyleSheet("background-image: url(Files/Images/UI/Logo.png);")

        self.Update()

    def Start(self):
        OctoPrintAPI.Login(OctoPrintAPI)
        OctoPrintAPI.GetProfiles(OctoPrintAPI)
        OctoPrintAPI.LoadPresets(OctoPrintAPI)

        # OctoPrintAPI.GetSettings(OctoPrintAPI)
        self.UpdateState()

    def UpdateState(self):
        if (not OctoPrintAPI.CheckConnection(OctoPrintAPI) in ["Connecting", "Close"]):
            OctoPrintAPI.GetJob(OctoPrintAPI)
        else: pass

        # OctoPrintAPI.GetSettings(OctoPrintAPI)
        OctoPrintAPI.GetAllFiles(OctoPrintAPI)
        OctoPrintAPI.GetProfiles(OctoPrintAPI)
        OctoPrintAPI.GetTemperaturePrinterState(OctoPrintAPI)

        # OctoPrintAPI.GetSettings(OctoPrintAPI)

        # try:
            # profile: Profile = OctoPrintAPI.PROFILES["Duplicator i3 Mini"]
        # except: pass
        # if (temp_stateJob != None):  Settings.DYNAMIC_VARIABLES.JobStatus = OctoPrintAPI.GetStateJob(OctoPrintAPI)

    def UpdateChildMenu(self):
        self.UpdateState()
        self.currentMenu.Update()

    def Update(self):
        for menu in self.ListMenus:
            menu.setHidden(not (menu == self.currentMenu))

        # self.currentMenu.Update()
        self.show()

    def ChangeMenu(self, name: str = "Menu", parameter: bool = True, isBack = False):
        if (parameter):
            t_lastMenuName = self.currentMenu.name
            # print(self.currentMenu.lastMenuName)
            self.currentMenu: Menu = self.GetMenuByName(name)
            print(f"[MENU][CURRENT] {self.currentMenu.name}")

            self.currentMenu.Start()
            self.Update()

            if (not isBack):
                self.currentMenu.lastMenuName = t_lastMenuName

    def GetMenuByName(self, name: str = "Default") -> Menu:
        for menu in self.ListMenus:
            if (menu.name == name): return menu

        for menu in self.ListMenus:
            if (menu.name == "Default"): return menu




"""
"""