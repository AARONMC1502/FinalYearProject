def decrypt(cipherBin, pad):
    a = 0
    plainBin = ""

    x = len(cipherBin) % 8
    print(x)

    if len(cipherBin) % 8 > 0:
        for i in range(8 - x):
            print("add")
            plainBin += "0"

    for char in [*cipherBin]:
        a += 1
        plainBin += str(int(char) ^ int([*pad][a]))

    return plainBin
