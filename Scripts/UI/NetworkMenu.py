from Scripts.UI.Menu import Menu, TextEdit, DefaultButton, VirtualKeyboard, ListWidget, AnimationTextEdit, FileSystemWatching, DefaultButton_WithLine
from Scripts.API.WiFiConnectionsAPI import WiFiConnectionAPI
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
        self.update = DefaultButton_WithLine(self, "Update", 575, 200, 200, 128, "Update", self.UpdateNetworks, imageName="refresh", color="rgb(221, 108, 43)")

        self.networks = ListWidget(self, "Files", 0, 0, 575, 600, self.ShowWifiConnectionSettings)

        self.ssidText = TextEdit(self, 0, 90, 250, 50, "SSID: null", funcEnterPressed=self.SetWifi)
        self.ssidText.setEnabled(False)
        self.ssidText.setHidden(True)

        self.passwordText = TextEdit(self, 0, 180, 250, 50, "PASSWORD: null", funcEnterPressed=self.SetWifi)
        self.passwordText.setEnabled(True)
        self.passwordText.setHidden(True)

        # self.led = DefaultButton(self, "LedSwitch", 0, 0, 100, 100, "Led", lambda: parent.ChangeMenu("LedSwitch"))
        # self.color = DefaultButton(self, "ColorScheme", 100, 0, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))
        # self.printFile = DefaultButton(self, "PrintFile", 200, 0, 100, 100, "Print", lambda: parent.ChangeMenu("PrintFile", OctoPrintAPI.JOB.state == "Operational"))
        # self.printingMenu = DefaultButton(self, "PrintingMenu", 300, 0, 100, 100, "Printing", lambda: parent.ChangeMenu("PrintingMenu"))

        # self.temperatureMenu = DefaultButton(self, "TemperatureMenu", 100, 100, 100, 100, "Heat", lambda: parent.ChangeMenu("TemperatureMenu"))

        # self.movingMenu = DefaultButton(self, "MovingMenu", 0, 100, 100, 100, "Move", lambda: parent.ChangeMenu("MovingMenu", OctoPrintAPI.JOB.state == "Operational"))

        # self.presetsMenu = DefaultButton(self, "PresetsMenu", 200, 100, 100, 100, "Preset", lambda: parent.ChangeMenu("PresetsMenu", OctoPrintAPI.JOB.state in ["Paused", "Pausing", "Printing"]))

        self.Update()
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def Start(self):
        self.UpdateNetworks()

    def UpdateNetworks(self):
        if (len(WiFiConnectionAPI.WIFI) != 0):
            self.networks.SetItems([wifi for wifi in WiFiConnectionAPI.WIFI])

    def SetWifi(self):
        # self.parent().virtualKeyboard.setHidden(True)
        self.parent().virtualKeyboard.PlayShowHideAnimation(True)
        self.ssidText.setHidden(True)
        self.passwordText.setHidden(True)

        WiFiConnectionAPI.ConnectWifi(WiFiConnectionAPI, self.ssidText.label.text(), self.passwordText.label.text())

        self.passwordText.label.setText("")


    def ShowWifiConnectionSettings(self, signal):
        # self.parent().virtualKeyboard.setHidden(False)
        self.parent().virtualKeyboard.PlayShowHideAnimation(False)
        self.ssidText.setHidden(False)
        self.passwordText.setHidden(False)

        network_ssid = self.networks.model.itemFromIndex(signal).text()
        self.ssidText.label.setText(network_ssid)

    def Update(self):
        pass