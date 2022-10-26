import Conversions
import UsedPad


def encrypt(message, pad):
    cipherBin = ""

    print(list(message))

    binMessage = list(Conversions.toBinary(message, "utf-8"))

    a = 0

    for bit in binMessage:
        a += 1
        cipherBin += str(int(bit) ^ int(list(pad)[a]))

    UsedPad.usedPad(len(binMessage))
    return cipherBin
