import Conversions
import Hmac


def decrypt(cipherBin, pad):
    a = 0
    counter = 0

    FormattedPlainBin = ""
    pad = Conversions.toBinary(pad, "utf-8")

    x = len(cipherBin) % 8

    if len(cipherBin) % 8 > 0:
        for i in range(8 - x):
            FormattedPlainBin += "0"
            counter += 1

    for bit in list(cipherBin):
        a += 1
        formattedPlainBin += str(int(bit) ^ int(list(pad)[a]))

    #this formats the plainbin the same as it was on the encryption sideso
    originalPlainBin = formattedPlainBin[counter:-32]

    messageHMAC = Conversions.toBinary(Hmac.calc_mac(pad, str(originalPlainBin)), "utf-8")

    if messageHMAC[-32:] == formattedPlainBin[-32:]:
        print("valid authentication")
    else:
        print("invalid authentication")

    return formattedPlainBin
