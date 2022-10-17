import TextToBinary
import UsedPad

def encryptV2(message, pad):
    cipherBin = ""

    binMessage = TextToBinary.toBinary(message, "utf-8")

    a = 0
    for char in [*binMessage]:
        a += 1
        cipherBin += str(int(char) ^ int([*pad][a]))

    UsedPad.usedPad(len(binMessage))
    return cipherBin