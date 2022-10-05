import secrets

def padGeneration():
    x = 0
    randomNumbers = []
    while x < 2000:
        a = secrets.SystemRandom().randint(1, 9)
        randomNumbers.append(a)
        x += 1
    with open("pad.json", "a") as pad:
        pad.write(str(randomNumbers))
        pad.close()

padGeneration()