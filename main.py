from Encrypt import encrypt
from Decrypt import decrypt
import json

f = open("pad.json")
pad = json.load(f)

# Shows how many characters are left in the pad
print("left in pad: {0}".format(len(pad)))

#plaintext message
p_text = input("Message: ")

#Generates and print cipher text
c_text = encrypt(list(pad), p_text)
print("Cipher text: {0}".format(c_text))

#Decrypts cipher text and print original plain text
d_text = decrypt(pad, c_text)
print("Decrypted text: {0}".format(d_text))