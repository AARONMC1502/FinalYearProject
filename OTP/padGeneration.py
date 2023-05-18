import secrets
import string

def padGeneration():
    x = 0
    padSize = 500
    randomNumbers = ""
    charSet = list(string.ascii_letters + string.digits + string.punctuation)

    while x < padSize:
        a = secrets.SystemRandom().choice(charSet)
        randomNumbers += str(a)
        x += 1
    with open("pad.txt", "w") as pad:
        pad.write(randomNumbers)
        pad.close()

padGeneration()