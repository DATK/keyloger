import json 

with open("data.json","r",encoding="UTF-8") as f:
    d=json.load(f)

with open("data copy.json","r",encoding="UTF-8") as f:
    d1=json.load(f)
    
print(len(d["data"]))
print(len(d1["data"]))