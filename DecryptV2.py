import Conversions


def decrypt(cipherBin, pad):
    a = 0
    plainBin = ""
    pad = Conversions.toBinary(pad, "utf-8")

    x = len(cipherBin) % 8

    if len(cipherBin) % 8 > 0:
        for i in range(8 - x):
            plainBin += "0"

    for bit in list(cipherBin):
        a += 1
        plainBin += str(int(bit) ^ int(list(pad)[a]))

    return plainBin
