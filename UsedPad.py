def usedPad(numbersUsed):
    with open("pad.txt") as file:
        pad = file.read()

    #removes used numbers in pad
    pad = pad[numbersUsed:]

    with open("pad.txt", "w") as newFile:
        newFile.write(str(pad))