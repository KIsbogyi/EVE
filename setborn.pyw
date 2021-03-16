from flask import Flask, render_template, make_response, send_file
import os
import json

def zeroer():
    global Plex
    global today
    Plex = []
    today = []



def beolvasas(file):
    fbe = open(file, "r")
    global data
    data = json.loads(fbe.readline())
    fbe.close()
    Plex.append(data["Plex"])
    today.append((data["today"]))


def helper():
    remove = ["api test.py","datavisualisation.py","eve.py","whole.py","__pycache__","setborn.pyw","static","templates"]
    arr = os.listdir()
    for elem in remove:
        arr.remove(elem)

    for file in arr:
        beolvasas(file)

def string_maker():
    global lstring
    lstring = ""
    for strings in today:
        lstring += str(strings)+"@"


#---------------------------------------------------------------------------------------------------------------

app = Flask(__name__)


@app.route('/')
def home():
    zeroer()
    helper()
    string_maker()
    global today
    resp = make_response(render_template('test.html', today = lstring	, Plex = Plex))
    return resp


if __name__ == '__main__':
   app.run(debug=True)