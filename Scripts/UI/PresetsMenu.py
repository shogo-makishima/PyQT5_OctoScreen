from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, FileSystemWatching, ListWidget, TextEdit
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI, Preset

class PresetsMenu(Menu):
    name = "PresetsMenu"

    def __init__(self, parent):
        super(PresetsMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.menu = DefaultButton(self, "Back", 300, 200, 100, 100, "Back", lambda: parent.ChangeMenu("MainPage"))
        self.addPreset = DefaultButton(self, "Add", 300, 100, 100, 100, "Add", lambda: parent.ChangeMenu("CreatePresetsMenu"))
        self.updatePresets = DefaultButton(self, "Update", 300, 0, 100, 100, "Update", self.UpdatePreset)

        self.files = ListWidget(self, "Files", 0, 0, 300, 300, self.SetPreset)

        self.Update()
        self.UpdatePreset()
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def UpdatePreset(self):
        OctoPrintAPI.LoadPresets(OctoPrintAPI)
        self.files.SetItems(OctoPrintAPI.PRESETS.keys())

    def SetPreset(self, signal):
        key = self.files.model.itemFromIndex(signal).text()
        OctoPrintAPI.SetToolTemperature(OctoPrintAPI, OctoPrintAPI.PRESETS[key].temperatureT0, OctoPrintAPI.PRESETS[key].temperatureT1, False)

    def Update(self):
        pass
        # self.statusBar.SetText(f"[STATUS] {OctoPrintAPI.JOB.state}")


class CreatePresetsMenu(Menu):
    name = "CreatePresetsMenu"

    def __init__(self, parent):
        super(CreatePresetsMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        self.i_name = TextEdit(self, 0, 20, 250, 50, "Name: str", "Preset")
        self.i_temperatureBed = TextEdit(self, 0, 90, 250, 50, "Temperature Bed: null")
        self.i_temperatureT0 = TextEdit(self, 0, 160, 250, 50, "Temperature T0: int", "200")
        self.i_temperatureT1 = TextEdit(self, 0, 230, 250, 50, "Temperature T1: null")

        self.menu = DefaultButton(self, "Back", 300, 180, 100, 100, "Back", lambda: parent.ChangeMenu("PresetsMenu"))

        self.createPreset = DefaultButton(self, "Save", 300, 20, 100, 100, "Save", self.SavePreset)

        self.Update()
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def SavePreset(self):
        try:
            t_name = self.i_name.label.text()
            t_tempBed = None if (self.i_temperatureBed.label.text() == "") else float(self.i_temperatureBed.label.text())
            t_tempT0 = None if (self.i_temperatureT0.label.text() == "") else float(self.i_temperatureT0.label.text())
            t_tempT1 = None if (self.i_temperatureT1.label.text() == "") else float(self.i_temperatureT1.label.text())

            OctoPrintAPI.CreatePreset(OctoPrintAPI, t_name, t_tempBed, t_tempT0, t_tempT1)
        except Exception as exception: print(exception)

    def Update(self):
        pass
        # self.statusBar.SetText(f"[STATUS] {OctoPrintAPI.JOB.state}")