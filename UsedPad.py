import json

def usedPad(numbersUsed):
    with open("pad.json") as file:
        pad = json.load(file)

    #removes used numbers in pad
    del pad[0:numbersUsed]

    with open("pad.json", "w") as newFile:
        newFile.write(str(pad))