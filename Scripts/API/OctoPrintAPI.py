import requests, json, threading, os

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

def Thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper

class Tool:
    def __init__(self, actual, target, offset):
        self.actual = actual
        self.target = target
        self.offset = offset

class File:
    def __init__(self, filename, origin, size, date, filePath=None):
        self.filename = filename; self.origin = origin; self.size = size; self.date = date; self.filePath = filePath

class Filament:
    def __init__(self, length, volume):
        self.length = length; self.volume = volume

class Progress:
    def __init__(self, completion, filepos, printTime, printTimeLeft):
        self.completion = completion; self.filepos = filepos; self.printTime = printTime; self.printTimeLeft = printTimeLeft

class Axis:
    def __init__(self, name, speed, inverted):
        self.name, self.speed, self.inverted = name, speed, inverted

class Volume:
    def __init__(self, formFactor, origin, width, depth, height):
        self.formFactor, self.origin, self.width, self.depth, self.height = formFactor, origin, width, depth, height

class Offset:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Extruder:
    def __init__(self, count, offsets):
        self.count, self.offsets = count, offsets

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

class Profile:
    def __init__(self, id, name, color, model, default, current, resource, volume, heatedBed, heatedChamber, axes, extruder):
        self.id, self.name, self.color, self.model, self.default, self.current, self.resource, self.volume, self.heatedBed, self.heatedChamber, self.axes, self.extruder = id, name, color, model, default, current, resource, volume, heatedBed, heatedChamber, axes, extruder

class Preset:
    def __init__(self, name, temperatureBed, temperatureT0, temperatureT1):
        self.name, self.temperatureBed, self.temperatureT0, self.temperatureT1 = name, temperatureBed, temperatureT0, temperatureT1


class OctoPrintAPI:
    # API_KEY: str = None
    URL = "http://192.168.1.46:5000"

    User: str = "Toma Kozaburo"
    Password: str = "1234567890"

    PRESETS: dict = {

    }

    TOOLS: dict = {
        "tool0": Tool(0, 0, 0),
        "tool1": Tool(0, 0, 0),
        "tool2": Tool(0, 0, 0),
        "tool3": Tool(0, 0, 0),
        "bed": Tool(0, 0, 0),
        "chamber": Tool(0, 0, 0),
    }

    FILES: list = [

    ]

    PROFILES: dict = {

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

    def LoadPresets(self) -> None:
        self.PRESETS.clear()

        presets = list(filter(lambda x: x if (x.rsplit(".", 1)[-1] in ["preset", "json"]) else None, os.listdir(f"{os.getcwd()}/Files/Presets")))
        for preset in presets:
            with open(f"Files/Presets/{preset}", "r") as filePreset:
                try:
                    data = json.load(filePreset)
                    self.PRESETS[data["name"]] = Preset(
                        data["name"],
                        data["temperatureBed"],
                        data["temperatureT0"],
                        data["temperatureT1"],
                    )
                except Exception as exception: print(exception)

    @Thread
    def CreatePreset(self, name, temperatureBed, temperatureT0, temperatureT1):
        with open(f"Files/Presets/{name}.preset", "w") as filePreset:
            try:
                data = {
                    "name": name,
                    "temperatureBed": temperatureBed,
                    "temperatureT0": temperatureT0,
                    "temperatureT1": temperatureT1,
                }

                filePreset.write(json.dumps(data))

                self.PRESETS[name] = Preset(
                    name,
                    temperatureBed,
                    temperatureT0,
                    temperatureT1
                )
            except Exception as exception:
                print(exception)


    @Thread
    def Login(self) -> None:
        data = {
            "passive": True,
            "user": self.User,
            "pass": self.Password,
            "remember": True
        }

        request = self.ConnectSession.post(f"{self.URL}/api/login", data=data)
        print("[Debug] Login Successful" if (request.status_code == 200) else "[Debug] Login Failed")

    @Thread
    def Logout(self) -> None:
        request = self.ConnectSession.post(f"{self.URL}/api/logout")
        print("[Debug] Logout Successful" if (request.status_code == 200) else "[Debug] Logout Failed")

    @Thread
    def CurrentUser(self) -> None:
        request = self.ConnectSession.get(f"{self.URL}/api/currentuser")
        print(f'[Debug] User groups: {", ".join(request.json()["groups"])}')

    @Thread
    def CheckConnection(self) -> bool:
        try:
            request = self.ConnectSession.get(f"{self.URL}/api/connection")
            return request.json()["current"]["state"]
        except: return "Close"

    @Thread
    def GetJob(self) -> None:
        try:
            data = self.ConnectSession.get(f"{self.URL}/api/job").json()

            self.JOB.file.filename = data["job"]["file"]["name"]
            self.JOB.file.origin = data["job"]["file"]["origin"]
            self.JOB.file.size = data["job"]["file"]["size"]
            self.JOB.file.date = data["job"]["file"]["date"]

            for key in self.JOB.filament.keys():
                if (data["job"]["filament"] != None and data["job"]["filament"].get(key) != None):
                    self.JOB.filament[key].length = data["job"]["filament"][key]["length"]
                    self.JOB.filament[key].volume = data["job"]["filament"][key]["volume"]

            self.JOB.progress.completion = data["progress"]["completion"]
            self.JOB.progress.filepos = data["progress"]["filepos"]
            self.JOB.progress.printTime = data["progress"]["printTime"]
            self.JOB.progress.printTimeLeft = data["progress"]["printTimeLeft"]

            self.JOB.state = data["state"]
        except Exception as exception: print(exception)

    @Thread
    def GetProfiles(self):
        try:
            data = self.ConnectSession.get(f"{self.URL}/api/printerprofiles").json()

            for profileId in data["profiles"]:
                profile = data["profiles"][profileId]

                self.PROFILES[profile["name"]] = Profile(
                    profile["id"],
                    profile["name"],
                    profile["color"],
                    profile["model"],
                    profile["default"],
                    profile["current"],
                    profile["resource"],
                    profile["volume"],
                    profile["heatedBed"],
                    profile["heatedChamber"],
                    { axis: Axis(axis, profile["axes"][axis]["speed"], profile["axes"][axis]["inverted"]) for axis in profile["axes"] },
                    Extruder(
                        profile["extruder"]["count"],
                        [Offset(profile["extruder"]["offsets"][i][0], profile["extruder"]["offsets"][i][0]) for i in range(len(profile["extruder"]["offsets"]))],
                    ),
                )
        except: pass

    @Thread
    def GetSettings(self):
        try:
            data = self.ConnectSession.get(f"{self.URL}/api/settings")
            print(data.text)
        except: pass

    @Thread
    def GetAllFiles(self):
        try:
            request = self.ConnectSession.get(f"{self.URL}/api/files")
            self.FILES.clear()

            for file in request.json()["files"]:
                if (file.get("children") == None):
                    self.FILES.append(File(file["name"], file["origin"], file["size"], file["date"], file["path"]))
                else:
                    for fileChild in file["children"]:
                        self.FILES.append(File(fileChild["name"], fileChild["origin"], fileChild["size"], fileChild["date"], fileChild["path"]))
        except: pass
        # print([file.filePath for file in self.FILES])

    @Thread
    def GetTemperaturePrinterState(self) -> None:
        try:
            data = self.ConnectSession.get(f"{self.URL}/api/printer", headers=self.HEADERS).json()["temperature"]
            for key in data.keys():
                self.TOOLS[key] = Tool(data[key]["actual"], data[key]["target"], data[key]["offset"])
        except:
            pass

    @Thread
    def GetChamberPrinterState(self) -> None:
        try:
            request = self.ConnectSession.get(f"{self.URL}/api/printer/chamber", headers=self.HEADERS)
            if (request.status_code == 200):
                self.TOOLS["chamber"] = data["actual"], data["target"], data["offset"]
        except:
            pass

    @Thread
    def SetJob(self, command: str = COMMANDS.PAUSE, action: str = COMMANDS.ACTION.EMPTY) -> None:
        data = {
            "command": command,
            "action": action,
        }

        request = self.ConnectSession.post(f"{self.URL}/api/job", data=json.dumps(data), headers=self.HEADERS)

    @Thread
    def SetHomePrintHead(self, axes=["x", "y", "z"]):
        data = {
            "command": "home",
            "axes": axes,
        }

        request = self.ConnectSession.post(f"{self.URL}/api/printer/printhead", data=json.dumps(data), headers=self.HEADERS)

    @Thread
    def SetJogPrintHead(self, x, y, z, absolute=False, speed=6000):
        data = {
            "command": "jog",
            "x": x,
            "y": y,
            "z": z,
            "absolute": absolute,
            "speed": speed,
        }

        request = self.ConnectSession.post(f"{self.URL}/api/printer/printhead", data=json.dumps(data), headers=self.HEADERS)


    @Thread
    def SelectFile(self, filename, print=True):
        data = {
            "command": "select",
            "print": print,
        }

        request = self.ConnectSession.post(f"{self.URL}/api/files/local/{filename}", data=json.dumps(data), headers=self.HEADERS)

    @Thread
    def SetToolTemperature(self, tool0, tool1=None, offset=True):
        data = {
            "command": "offset" if (offset) else "target",
            "offsets" if (offset) else "targets": {
                # "tool0": tool0,
                # "tool1": tool1,
            },
        }

        if (tool0 != None): data["offsets" if (offset) else "targets"]["tool0"] = tool0
        if (tool1 != None): data["offsets" if (offset) else "targets"]["tool1"] = tool0

        request = self.ConnectSession.post(f"{self.URL}/api/printer/tool", data=json.dumps(data), headers=self.HEADERS)

"""
    def GetTemperaturePrinterState(self) -> None:
        data = self.GetPrinterState(self)["temperature"]
        for key in data.keys():
            self.TOOLS[key] = Tool(data[key]["actual"], data[key]["target"], data[key]["offset"])

    def GetChamberPrinterState(self) -> None:
        request = self.ConnectSession.get(f"{self.URL}/api/printer/chamber", headers=self.HEADERS)
        if (request.status_code == 200):
            self.TOOLS["chamber"] = data["actual"], data["target"], data["offset"]
    """

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
