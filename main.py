from Encrypt import encrypt
from Decrypt import decrypt
import json

f = open("pad.json")
pad = json.load(f)

print("left in pad: {0}".format(len(pad)))
p_text = input("Message: ")

c_text = encrypt(list(pad), p_text)

print(c_text)
print(decrypt(pad, c_text))