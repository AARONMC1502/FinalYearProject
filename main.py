from Encrypt import encrypt
from Decrypt import decrypt
import json

#pad = padGeneration()

f = open("pad.json")
pad = json.load(f)

p_text = input()

c_text = encrypt(list(pad), p_text)

print(c_text)
print(decrypt(pad, c_text))