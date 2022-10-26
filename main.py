from EncryptV2 import encrypt
from DecryptV2 import decrypt
import Conversions
import time

f = open("pad.txt")
pad = f.read()

# Shows how much is left in the pad in percentage
padLeftPercentage = 100 - ((750 - len(pad)) / 750) * 100
print("left in pad: {:.2f}% left".format(padLeftPercentage))

# plaintext message
p_text = input("Message: ")

# Generates and prints cipher binary
c_binary = encrypt(p_text, pad)
print("Encrypted binary: {0}".format(c_binary))

# Shows what will be sent represented as UTF-8
print("Encrypted message: {0}".format(Conversions.toText(c_binary)))

# Decrypts cipher binary and prints message binary
d_text = decrypt(c_binary, pad)
print("Decrypted binary: {0}".format(d_text))

# decoded binary
print("Decrypted message: {0}".format(Conversions.toText(d_text)))