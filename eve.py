
def start():
    import requests
    import datetime
    import json
    volumes = {
        "Arkonor": 16,
        "Bezdnacine": 16,
        "Bistot": 16,
        "Crokite": 16,
        "Dark Ochre": 8,
        "Gneiss": 5,
        "Hedbergite": 3,
        "Hemorphite": 3,
        "Jaspet": 2,
        "Kernite": 1.2,
        "Mercoxit": 40,
        "Omber": 0.6,
        "Plagioclase": 0.35,
        "Pyroxeres": 0.3,
        "Rakovene": 16,
        "Scordite": 0.15,
        "Spodumain": 16,
        "Talassonite": 16,
        "Veldspar": 0.1
    }

    ids = {
        "Arkonor": 22,
        "Bezdnacine": 52316,
        "Bistot": 1223,
        "Crokite": 1225,
        "Dark Ochre": 1232,
        "Gneiss": 1229,
        "Hedbergite": 21,
        "Hemorphite": 1231,
        "Jaspet": 1226,
        "Kernite": 20,
        "Mercoxit": 11396,
        "Omber": 1227,
        "Plagioclase": 18,
        "Pyroxeres": 1224,
        "Rakovene": 52315,
        "Scordite": 1228,
        "Spodumain": 19,
        "Talassonite": 52306,
        "Veldspar": 1230,
        "Plex": 44992
    }
    TemporaryDict = {}
    today = str(datetime.datetime.today())
    TemporaryDict["today"] = (today[0:13])

    for elem in ids:
        id_s = str(ids[elem])
        rVeldspar = (requests.get("https://api.evemarketer.com/ec/marketstat/json?typeid=" + id_s + "&usesystem=30000142").json())
        try:
            TemporaryDict[elem] = (rVeldspar[0]["sell"]["fivePercent"])/volumes[elem]
        except:
            TemporaryDict[elem] = rVeldspar[0]["sell"]["fivePercent"]

    def JsonWriter(data):
        with open(today[5:13]+".json" ,'w') as outfile:
            json.dump(data, outfile)
            outfile.close()
    print("runned")
    JsonWriter(TemporaryDict)

