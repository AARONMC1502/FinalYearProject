import string
from UsedPad import usedPad

def encrypt(pad, message):
    alphabet = list(string.printable)
    cipherText = ""
    plainText = [*message]
    for i in range(len(plainText)):
        """if plainText[i] == " ":
            cipherText += plainText[i]
            continue"""
        cipherIndex = (alphabet.index(plainText[i]) + pad[i]) % 100
        cipherText += alphabet[cipherIndex]
    usedPad(len(str(cipherText)))
    return cipherText