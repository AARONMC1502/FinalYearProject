def usedPad(numbersUsed):
    with open("pad.bin") as file:
        pad = file.read()

    # removes used numbers in pad
    pad = pad[numbersUsed + 16:]

    with open("pad.bin", "w") as newFile:
        newFile.write(str(pad))
