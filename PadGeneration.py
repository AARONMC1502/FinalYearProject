import secrets

def padGeneration():
    x = 0
    randomNumbers = ""

    while x < 20000:
        a = secrets.SystemRandom().randint(0, 1)
        randomNumbers += str(a)
        x += 1
    with open("pad.txt", "a") as pad:
        pad.write(str(randomNumbers))
        pad.close()

padGeneration()