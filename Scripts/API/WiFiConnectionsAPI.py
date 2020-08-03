from wifi import Cell, Scheme
import os, platform, subprocess, time, re
from Scripts.API.OctoPrintAPI import Thread

class WiFiNetwork:
    def __init__(self, ssid, bssid):
        self.ssid, self.bssid = ssid, bssid

class WiFiConnectionAPI:
    SYSTEM: str = platform.system()

    if (SYSTEM == "Windows"): INTERFACE_NAME: str = "wlan"
    elif (SYSTEM == "Linux"): INTERFACE_NAME: str = "wlan0"

    WIFI: list = {

    }

    def __runCommand(self, cmd):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for (LINE) in iter(process.stdout.readline, b''):
            if (LINE):
                yield LINE
        while (process.poll() == None):
            time.sleep(0.1)
        err = process.stderr.read()
        if process.returncode != 0:
            print("" + err)

    def GetWifiNetworks(self) -> None:
        self.WIFI.clear()

        if (self.SYSTEM == "Windows"):
            self.__GetNetworks_Windows(self)
        elif (self.SYSTEM == "Linux"):
            self.__GetNetworks_Linux(self)

    def ConnectWifi(self, ssid, password) -> None:
        if (self.SYSTEM == "Windows"):
            self.__ConnectionWifi_Windows(self, ssid, password)
        elif (self.SYSTEM == "Linux"):
            self.__ConnectionWifi_Linux(self, ssid, password)

    @Thread
    def __GetNetworks_Windows(self) -> None:
        results = self.__runCommand(self, f"netsh {self.INTERFACE_NAME} show networks mode=bssid")
        results = [i.decode('cp866') for i in results]

        ssid, bssid = "", ""
        for line in results:
            if (ssid != str() and bssid != str()):
                self.WIFI[ssid] = WiFiNetwork(ssid, bssid)
                ssid, bssid = "", ""

            if ("BSSID" in line):
                bssid = re.sub('BSSID [\d]+:', '', line.strip()).strip()
            elif ("SSID" in line):
                ssid = re.sub('SSID [\d]+:', '', line.strip()).strip()

    @Thread
    def __GetNetworks_Linux(self) -> None:
        for cell in Cell.all("wlan0"):
            self.WIFI[cell.ssid] = WiFiNetwork(cell.ssid, cell.address)

    def __ConnectionWifi_Windows(self, ssid, password) -> None:
        pass

    def __ConnectionWifi_Linux(self, ssid, password) -> None:
        try:
            os.system(f"wpa_passphrase {ssid} {password} | sudo tee /etc/wpa_supplicant.conf")
            os.system(f"sudo wpa_supplicant -B -c /etc/wpa_supplicant.conf -i {self.INTERFACE_NAME}")
        except Exception as exception: print(exception)

"""
WiFiConnectionAPI.GetWifiNetworks(WiFiConnectionAPI)
print(", ".join([WiFiConnectionAPI.WIFI[wifi].ssid for wifi in WiFiConnectionAPI.WIFI]))
WiFiConnectionAPI.ConnectWifi(WiFiConnectionAPI, "SSID", "PASSWORD")
"""