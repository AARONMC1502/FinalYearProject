def decryptV2(cipherBin, pad):
    a = 0
    plainBin = ""

    for char in [*cipherBin]:
        a += 1
        plainBin += str(int(char) ^ int([*pad][a]))
    return plainBin
