import Conversions
import UsedPad

def encrypt(message, pad):
    cipherBin = ""
    binMessage = Conversions.toBinary(message, "utf-8")

    a = 0

    for char in [*binMessage]:
        a += 1
        cipherBin += str(int(char) ^ int([*pad][a]))

    UsedPad.usedPad(len(binMessage))
    return cipherBin