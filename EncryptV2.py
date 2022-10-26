import Conversions
import UsedPad


def encrypt(message, pad):
    cipherBin = ""
    binMessage = list(Conversions.toBinary(message, "utf-8"))
    pad = Conversions.toBinary(pad, "utf-8")

    a = 0

    for bit in binMessage:
        a += 1
        cipherBin += str(int(bit) ^ int(list(pad)[a]))

    UsedPad.usedPad(len(binMessage))
    return cipherBin
