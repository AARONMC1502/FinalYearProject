import string

def decrypt(pad, message):
    alphabet = list(string.printable)
    plainText = ""
    cipherText = [*message]
    for i in range(len(cipherText)):
        cipherIndex = (alphabet.index(cipherText[i]) - pad[i]) % 100
        plainText += alphabet[cipherIndex]
    return plainText