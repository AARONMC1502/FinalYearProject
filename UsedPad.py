import json

def usedPad(numbersUsed):
    newPad = []
    with open("pad.json") as file:
        pad = json.load(file)
    del pad[0:numbersUsed]

    """for i in pad:
        if pad.index(i) < numbersUsed:
            continue
        else:
            newPad.append(i)"""
    with open("pad.json", "w") as newFile:
        newFile.write(str(pad))