def decryptV2(cipherBin, pad):
    a = 0
    plainBin = ""

    if len(cipherBin) % 8 > 0:
        plainBin += "0"

    for char in [*cipherBin]:
        a += 1
        plainBin += str(int(char) ^ int([*pad][a]))
    return plainBin
