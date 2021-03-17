from flask import Flask, render_template, make_response, send_file
import os
import json

def zeroer():
    global Plex
    global today
    global Arkonor
    global Bezdnacine
    global Bistot
    global Crokite
    global Dark_Ochre
    global Gneiss
    global Hedbergite
    global Hemorphite
    global Jaspet
    global Kernite
    global Mercoxit
    global Omber
    global Plagioclase
    global Pyroxeres
    global Rakovene
    global Scordite
    global Spodumain
    global Talassonite
    global Veldspar

    Plex = []
    today = []

    Arkonor = []
    Bezdnacine = []
    Bistot = []
    Crokite = []
    Dark_Ochre = []
    Gneiss  = []
    Hedbergite = []
    Hemorphite = []
    Jaspet = []
    Kernite = []
    Mercoxit = []
    Omber = []
    Plagioclase = []
    Pyroxeres = []
    Rakovene = []
    Scordite = []
    Spodumain = []
    Talassonite = []
    Veldspar = []

def beolvasas(file):
    fbe = open(file, "r")
    global data
    print(file)
    data = json.loads(fbe.readline())
    fbe.close()
    print(data, "hi")
    Plex.append(data["Plex"])
    today.append(data["today"])




def helper():
    remove = ["templates", "evewebserver.py"]
    arr = os.listdir()
    for elem in remove:
        arr.remove(elem)
    print(arr)

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
    resp = make_response(render_template('test.html', today = lstring	, Plex = Plex , Arkonor = Arkonor, Bezdnacine = Bezdnacine, Bistot = Bistot, Crokite = Crokite, Dark_Ochre = Dark_Ochre, Gneiss = Gneiss, Hedbergite = Hedbergite, Hemorphite = Hemorphite, Jaspet = Jaspet, Kernite = Kernite, Mercoxit = Mercoxit, Omber = Omber, Plagioclase = Plagioclase, Pyroxeres = Pyroxeres, Rakovene = Rakovene, Scordite = Scordite, Spodumain = Spodumain,Talassonite = Talassonite, Veldspar = Veldspar  ))
    return resp


if __name__ == '__main__':
   app.run(debug=True)
