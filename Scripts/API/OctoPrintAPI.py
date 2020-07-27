import requests, json

class COMMANDS:
    START = "start"
    CANCEL = "cancel"
    RESTART = "restart"
    PAUSE = "pause"

    class ACTION:
        EMPTY = None
        PAUSE = "pause"
        RESUME = "resume"
        TOGGLE = "toggle"

class Tool:
    def __init__(self, actual, target, offset):
        self.actual = actual
        self.target = target
        self.offset = offset

class File:
    def __init__(self, filename, origin, size, date):
        self.filename = filename; self.origin = origin; self.size = size; self.date = date

class Filament:
    def __init__(self, length, volume):
        self.length = length; self.volume = volume

class Progress:
    def __init__(self, completion, filepos, printTime, printTimeLeft):
        self.completion = completion; self.filepos = filepos; self.printTime = printTime; self.printTimeLeft = printTimeLeft

class Job:
    def __init__(self, file, estimatedPrintTime, filament_t0, filament_t1, progress, state):
        self.file = file
        self.estimatedPrintTime = estimatedPrintTime
        self.filament = {
            "tool0": filament_t0,
            "tool1": filament_t1,
        }
        self.progress = progress
        self.state = state


class OctoPrintAPI:
    # API_KEY: str = None
    URL = "http://192.168.1.46:5000"

    User: str = "Toma Kozaburo"
    Password: str = "1234567890"

    IS_Online: bool = False

    TOOLS: dict = {
        "tool0": Tool(0, 0, 0),
        "tool1": Tool(0, 0, 0),
        "bed": Tool(0, 0, 0),
        "chamber": Tool(0, 0, 0),
    }

    JOB = Job(
        File("empty", "local", 0, 0),
        0,
        Filament(0, 0),
        Filament(0, 0),
        Progress(0, 0, 0, 0),
        "Offline"
    )

    HEADERS = {
        "content-type": "application/json"
    }

    StateJob: str = None
    ConnectSession: requests.Session = requests.Session()

    def Login(self) -> None:
        data = {
            "passive": True,
            "user": self.User,
            "pass": self.Password,
            "remember": True
        }

        request = self.ConnectSession.post(f"{self.URL}/api/login", data=data)
        print("[Debug] Login Successful" if (request.status_code == 200) else "[Debug] Login Failed")

    def Logout(self) -> None:
        request = self.ConnectSession.post(f"{self.URL}/api/logout")
        print("[Debug] Logout Successful" if (request.status_code == 200) else "[Debug] Logout Failed")

    def CurrentUser(self) -> None:
        request = self.ConnectSession.get(f"{self.URL}/api/currentuser")
        print(f'[Debug] User groups: {", ".join(request.json()["groups"])}')

    def GetJob(self) -> None:
        try:
            data = self.ConnectSession.get(f"{self.URL}/api/job").json()

            self.JOB.file.filename = data["job"]["file"]["name"]
            self.JOB.file.origin = data["job"]["file"]["origin"]
            self.JOB.file.size = data["job"]["file"]["size"]
            self.JOB.file.date = data["job"]["file"]["date"]

            for key in self.JOB.filament.keys():
                if (data["job"]["filament"].get(key) != None):
                    self.JOB.filament[key].length = data["job"]["filament"][key]["length"]
                    self.JOB.filament[key].volume = data["job"]["filament"][key]["volume"]

            self.JOB.progress.completion = data["progress"]["completion"]
            self.JOB.progress.filepos = data["progress"]["filepos"]
            self.JOB.progress.printTime = data["progress"]["printTime"]
            self.JOB.progress.printTimeLeft = data["progress"]["printTimeLeft"]

            self.JOB.state = data["state"]
        except: pass

    def SetJob(self, command: str = COMMANDS.PAUSE, action: str = COMMANDS.ACTION.EMPTY) -> None:
        data = {
            "command": command,
            "action": action,
        }

        request = self.ConnectSession.post(f"{self.URL}/api/job", data=json.dumps(data), headers=self.HEADERS)

    def GetPrinterState(self) -> dict:
        return self.ConnectSession.get(f"{self.URL}/api/printer", headers=self.HEADERS).json()

    def GetTemperaturePrinterState(self) -> None:
        data = self.GetPrinterState(self)["temperature"]
        for key in data.keys():
            self.TOOLS[key] = Tool(data[key]["actual"], data[key]["target"], data[key]["offset"])

    def GetChamberPrinterState(self) -> None:
        request = self.ConnectSession.get(f"{self.URL}/api/printer/chamber", headers=self.HEADERS)
        if (request.status_code == 200):
            self.TOOLS["chamber"] = data["actual"], data["target"], data["offset"]

"""
OctoPrintAPI.Login(OctoPrintAPI)
OctoPrintAPI.CurrentUser(OctoPrintAPI)

print(OctoPrintAPI.GetJob(OctoPrintAPI))
print(OctoPrintAPI.GetProgress(OctoPrintAPI))
OctoPrintAPI.GetTemperaturePrinterState(OctoPrintAPI)
OctoPrintAPI.GetChamberPrinterState(OctoPrintAPI)

OctoPrintAPI.Logout(OctoPrintAPI)
OctoPrintAPI.CurrentUser(OctoPrintAPI)
"""
