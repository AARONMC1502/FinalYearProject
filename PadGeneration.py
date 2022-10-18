import secrets
import Conversions

def padGeneration():
    x = 0
    randomNumbers = ""

    while x < 20000:
        a = secrets.SystemRandom().randint(0, 9)
        randomNumbers += str(a)
        x += 1
    with open("pad.bin", "a") as pad:
        pad.write(str("0"+Conversions.toBinary(randomNumbers, "utf-8")))
        pad.close()

    with open("padForQR.txt", "a") as padQR:
        padQR.write(str(randomNumbers))
        padQR.close()

padGeneration()