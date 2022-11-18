import Conversions
import Hmac


def decrypt(cipherBin, pad):
    a = 0
    counter = 0

    plainBin = ""
    pad = Conversions.toBinary(pad, "utf-8")

    x = len(cipherBin) % 8

    if len(cipherBin) % 8 > 0:
        for i in range(8 - x):
            plainBin += "0"
            counter += 1

    for bit in list(cipherBin):
        a += 1
        plainBin += str(int(bit) ^ int(list(pad)[a]))

    #this formats the plainbin the same as it was on the encryption side
    originalPlainBin = plainBin[counter:-512]

    messageHMAC = Conversions.HMACToBinary(Hmac.calc_mac(pad, str(originalPlainBin)), "utf-8")

    if messageHMAC[-512:] == plainBin[-512:]:
        print("valid authentication")
    else:
        print("invalid authentication")

    return plainBin
