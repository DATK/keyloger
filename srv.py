from flask import Flask, request
import json


dbg = False


def write(js):
    try:
        with open("data.json", "r", encoding="UTF-8") as f:
            tmp = json.load(f)
        tmp["data"].extend(js["data"])
    except:
        return "bad"
    with open("data.json", "w", encoding="UTF-8") as f:
        json.dump(tmp, f)
    return "sucs"


app = Flask(__name__)


@app.route("/getin/it/data", methods=["POST"])
def get():
    data = request.json
    # print(data)
    return write(data)

@app.route("/connect", methods=["GET"])
def get1():
    return "q"

app.run(debug=dbg, host="0.0.0.0")
