import binascii

def toText(binary):
    Text = "".join([chr(int(binary[i: i + 8], 2)) for i in range(0, len(binary), 8)])
    return Text

def toBinary(text, *kwargs):
    byteText = bytes(text, *kwargs)
    binText = bin(int(binascii.hexlify(byteText),16))
    formattedBinMessage = "0"+binText[2:]
    return formattedBinMessage