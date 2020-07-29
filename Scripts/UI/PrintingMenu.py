from Scripts.UI.Menu import Menu, DefaultButton, AnimationTextEdit, TextWithIcon, DefaultButton_WithLine, FileSystemWatching, StaticText, DefaultParameter
from PyQt5 import QtGui, QtCore, QtWidgets
import Scripts.Settings.Settings as Settings
import Scripts.Settings.StyleSheets as StyleSheets
from Scripts.API.OctoPrintAPI import OctoPrintAPI, COMMANDS

class PrintingMenu(Menu):
    name = "PrintingMenu"

    def __init__(self, parent):
        super(PrintingMenu, self).__init__(parent)

        self.setObjectName(self.name)
        self.setFixedSize(Settings.WINDOW_SIZE[0], Settings.WINDOW_SIZE[1])

        # self.statusBar = StaticText(self, 75, 200, 250, 50, f"[STATUS] {Settings.DYNAMIC_VARIABLES.JobStatus}")

        self.statusPrintingTime = TextWithIcon(self, 380, 25, 400, 50, "", "status", iconSize=(50, 50), textOffset=(20, 0), fontSize=25)
        self.statusPrintingFileName = TextWithIcon(self, 380, 75, 400, 50, "", "file", iconSize=(50, 50), textOffset=(20, 0), fontSize=25)
        self.statusPrinting = TextWithIcon(self, 380, 125, 400, 50, "", "print", iconSize=(50, 50), textOffset=(20, 0), fontSize=25)

        self.t0Status = DefaultButton(self, "t0Status", 150, 25, 128, 128, "", None, isButton=False,imageName="extruder-1")
        self.bedStatus = DefaultButton(self, "bedStatus", 150, 225, 128, 128, "", None, isButton=False, imageName="bed")


        self.pause = DefaultButton_WithLine(self, "Pause", 0, 400, 200, 128, "Pause", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.PAUSE, COMMANDS.ACTION.PAUSE), imageName="pause", color="rgb(221, 108, 43)")
        self.resume = DefaultButton_WithLine(self, "Resume", 200, 400, 200, 128, "Resume", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.PAUSE, COMMANDS.ACTION.RESUME), imageName="resume", color="rgb(162, 37, 124)")
        self.cancel = DefaultButton_WithLine(self, "Cancel", 400, 400, 200, 128, "Cancel", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.CANCEL, COMMANDS.ACTION.EMPTY), imageName="stop", color="rgb(64, 144, 131)")

        self.back = DefaultButton_WithLine(self, "Back", 600, 400, 200, 128, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True), imageName="back", color="rgb(180, 223, 71)")
        # self.parameterTool0 = DefaultParameter(self, "Tool0", 0, 0, 100, 100, "Back")
        # self.parameterBed = DefaultParameter(self, "Bed", 100, 0, 100, 100, "Back")
        # self.parameterChamber = DefaultParameter(self, "Chamber", 200, 0, 100, 100, "Back")
        # self.parameterProgress = DefaultParameter(self, "Progress", 200, 0, 100, 100, "Back")

        # self.progressBar = QtWidgets.QProgressBar(self)
        # self.progressBar.setGeometry(0, 260, 450, 30)

        # self.menu = DefaultButton(self, "Back", 300, 100, 100, 100, "Back", lambda: parent.ChangeMenu(self.lastMenuName, isBack=True))
        # self.resume = DefaultButton(self, "Resume", 0, 100, 100, 100, "Resume", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.PAUSE, COMMANDS.ACTION.RESUME))
        # self.pause = DefaultButton(self, "Pause", 100, 100, 100, 100, "Pause", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.PAUSE, COMMANDS.ACTION.PAUSE))

        # self.pause = DefaultButton(self, "Cancel", 200, 100, 100, 100, "Cancel", lambda: OctoPrintAPI.SetJob(OctoPrintAPI, COMMANDS.CANCEL, COMMANDS.ACTION.EMPTY))

        self.Update()
        # self.color = DefaultButton(self, "ColorScheme", 100, 0, 100, 100, "Color", lambda: parent.ChangeMenu("ColorScheme"))
        # self.printFile = DefaultButton(self, "PrintFile", 200, 0, 100, 100, "Print", lambda: parent.ChangeMenu("PrintFile"))
        # self.files = FileSystemWatching(self, 200, 0, 200, 100)

    def Update(self):
        self.t0Status.setText(f"{round(OctoPrintAPI.TOOLS['tool0'].actual)}°C / {round(OctoPrintAPI.TOOLS['tool0'].target)}°C")
        self.bedStatus.setText(f"{round(OctoPrintAPI.TOOLS['bed'].actual)}°C / {round(OctoPrintAPI.TOOLS['bed'].target)}°C")

        if (OctoPrintAPI.JOB.progress.completion != None):
            self.statusPrintingTime.SetText(f"{OctoPrintAPI.JOB.progress.printTime}s / {OctoPrintAPI.JOB.progress.printTimeLeft}s")
        else:
            self.statusPrintingTime.SetText(f"Ns / Ns")

        if (OctoPrintAPI.JOB.file.filename != None):
            self.statusPrintingFileName.SetText(f"{OctoPrintAPI.JOB.file.filename}")
        else:
            self.statusPrintingFileName.SetText(f"None")

        self.statusPrinting.SetText(f"{OctoPrintAPI.JOB.state}")

        # self.parameterTool0.SetText(f"T0\n{round(OctoPrintAPI.TOOLS['tool0'].actual)}°C\n{round(OctoPrintAPI.TOOLS['tool0'].target)}°C")
        # self.parameterBed.SetText(f"BED\n{OctoPrintAPI.TOOLS['bed'].actual}°C\n{OctoPrintAPI.TOOLS['bed'].target}°C")
        # self.parameterChamber.SetText(f"CHAM\n{OctoPrintAPI.TOOLS['chamber'].actual}°C\n{OctoPrintAPI.TOOLS['chamber'].target}°C")

        # if (OctoPrintAPI.JOB.progress.completion != None):
            # self.parameterProgress.SetText(f"PERS\n{round(OctoPrintAPI.JOB.progress.completion, 1)}%\n{OctoPrintAPI.JOB.progress.printTime // 60}m/{OctoPrintAPI.JOB.progress.printTimeLeft // 60}m")
        # else:
            #self.parameterProgress.SetText(f"PERS\nN%\nNm/Nm")

        # self.statusBar.SetText(f"[STATUS] {OctoPrintAPI.JOB.state}")

        # self.progressBar.setValue(round(OctoPrintAPI.JOB.progress.completion, 1))