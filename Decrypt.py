import string

def decrypt(pad, message):
    alphabet = list(string.ascii_lowercase)
    plainText = ""
    cipherText = [*message]
    for i in range(len(cipherText)):
        if cipherText[i] == " ":
            plainText += cipherText[i]
            continue
        cipherIndex = (alphabet.index(cipherText[i]) - pad[i]) % 26
        plainText += alphabet[cipherIndex]
    return plainText