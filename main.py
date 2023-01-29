from EncryptV2 import encrypt
from DecryptV2 import decrypt
import Conversions


f = open("pad.txt")
pad = f.read()

# Shows how much is left in the pad in percentage
padLeftPercentage = 100 - ((2000 - len(pad)) / 2000) * 100
print("left in pad: {:.2f}% left".format(padLeftPercentage))

# plaintext message
plainText = input("Message: ")

# Generates and prints cipher binary
cipherBinary = encrypt(plainText, pad)
print("Encrypted binary: {0}".format(cipherBinary))

# Shows what will be sent represented as UTF-8
print("Encrypted message: {0}".format(Conversions.toText(cipherBinary)))

# decrypted binary
decryptedText = decrypt(cipherBinary, pad)

print("HMAC Tag:", Conversions.toText(decryptedText)[-64:])

print("Decrypted binary: {0}".format(decryptedText))

# decoded message
print("Decrypted message: {0}".format(Conversions.toText(decryptedText))[:-64])