import Conversions
import UsedPad
import Hmac

def encrypt(message, pad):
    binMessage = list(Conversions.toBinary(message, "utf-8"))
    pad = Conversions.toBinary(pad, "utf-8")

    messageHMAC = Hmac.calc_mac(pad, "".join(binMessage))
    binHMAC = Conversions.toBinary(messageHMAC, "utf-8")

    # adds each part of the HMAC
    for bit in binHMAC[-32:]:
        binMessage.append(bit)

    print("hi", "".join(binMessage))

    a = 0
    cipherBin = ""

    for bit in binMessage:
        a += 1
        cipherBin += str(int(bit) ^ int(list(pad)[a]))

    usedKey = round(len(binMessage) / 8)
    UsedPad.usedPad(usedKey)

    return cipherBin
