from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
from Scripts.UI.Menu import Menu
from Scripts.UI.MainPage import MainPage
from Scripts.UI.LedSwitch import LedSwitch
from Scripts.UI.ColorScheme import ColorScheme
from Scripts.UI.PrintFile import PrintFile

class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ListMenus: Menu = [
            Menu(self),
            MainPage(self),
            LedSwitch(self),
            ColorScheme(self),
            PrintFile(self),
        ]

        font = QtGui.QFont("Trench", 30)

        self.setObjectName("Menu")
        self.setGeometry(100, 100, Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.currentMenu: Menu = self.GetMenuByName("MainPage")
        print(f"[MENU][CURRENT] {self.currentMenu.name}")

        self.setStyleSheet("background-color: black;")
        # self.setStyleSheet("background-image: url(Files/Images/UI/Logo.png);")

        self.Update()

    def Update(self):
        for menu in self.ListMenus:
            menu.setHidden(not (menu == self.currentMenu))

        # self.currentMenu.Update()
        self.show()

    def ChangeMenu(self, name: str = "Menu"):
        self.currentMenu: Menu = self.GetMenuByName(name)
        print(f"[MENU][CURRENT] {self.currentMenu.name}")

        self.Update()

    def GetMenuByName(self, name: str = "Default") -> Menu:
        for menu in self.ListMenus:
            if (menu.name == name): return menu

        for menu in self.ListMenus:
            if (menu.name == "Default"): return menu




"""
def thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper
"""