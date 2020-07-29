from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI

class MovingMenu(Menu):
    name = "MovingMenu"

    def __init__(self, parent):
        super(MovingMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True))

        self.zPlus = DefaultButton(self, "Z", 300, 0, 100, 100, "Z+", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, 0, 0, +10))
        self.zMinus = DefaultButton(self, "Z", 300, 100, 100, 100, "Z-", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, 0, 0, -10))

        self.xMinus = DefaultButton(self, "X", 0, 100, 100, 100, "X-", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, -10, 0, 0))
        self.xPlus = DefaultButton(self, "X", 200, 100, 100, 100, "X+", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, +10, 0, 0))

        self.yPlus = DefaultButton(self, "Y", 100, 0, 100, 100, "Y+", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, 0, +10, 0))
        self.yMinus = DefaultButton(self, "Y", 100, 200, 100, 100, "Y-", lambda: OctoPrintAPI.SetJogPrintHead(OctoPrintAPI, 0, -10, 0))

        self.axesHome = DefaultButton(self, "H", 100, 100, 100, 100, "HOME", lambda: OctoPrintAPI.SetHomePrintHead(OctoPrintAPI))

        self.Update()
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def Update(self):
        pass