from EncryptV2 import encrypt
from DecryptV2 import decrypt
import Conversions

f = open("pad.txt")
pad = f.read()

print("------ This demonstrates the flow of messages in the proposed system ------")

# Shows how much is left in the pad in percentage
padLeftPercentage = 100 - ((500 - len(pad)) / 500) * 100

print("left in pad: {:.2f}% left".format(padLeftPercentage))
print("------ Client A ------")

plainText = input("Message: ")
cipherBinary = encrypt(plainText, pad)

print("Encrypted binary: {0}".format(cipherBinary))
print("Encrypted message: {0} \n".format(Conversions.toText(cipherBinary)))

print("------ Server in between... ------\n")
print("Message forwarded between server: {0} \n".format(cipherBinary))
print("------ Server in between... ------\n")

print("------ Client B ------")

decryptedText = decrypt(cipherBinary, pad)
print("Received HMAC Tag: {0}\n".format(Conversions.toText(decryptedText)[-64:]))
print("Decrypted binary: {0}".format(decryptedText))
print("Decrypted message: {0}".format(Conversions.toText(decryptedText))[:-64])