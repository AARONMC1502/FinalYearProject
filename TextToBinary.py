import binascii

def toBinary(text, *kwargs):
    byteText = bytes(text, *kwargs)
    binText = bin(int(binascii.hexlify(byteText),16))
    formattedBinMessage = "0"+binText[2:]
    return formattedBinMessage