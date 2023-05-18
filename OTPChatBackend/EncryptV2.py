import Conversions
import UsedPad
import Hmac


def encrypt(message, pad):
    binMessage = list(Conversions.toBinary(message, "utf-8"))
    pad = Conversions.toBinary(pad, "utf-8")

    messageHMAC = Hmac.calc_mac(pad, "".join(binMessage))
    print("Generated HMAC tag: {0}".format(messageHMAC))

    binHMAC = Conversions.HMACToBinary(messageHMAC, "utf-8")

    # adds each part of the HMAC
    for bit in binHMAC:
        binMessage.append(bit)

    a = 0
    cipherBin = ""

    for bit in binMessage:
        a += 1
        cipherBin += str(int(bit) ^ int(list(pad)[a]))

    return cipherBin
