import random

def generate():
    przybycie = []
    trwanie = []
    priorytet = []
    kwant = 0
    kwant1 = 0

    for i in range(0, random.randint(15,15)):
            przybycie.append(random.randint(0, 50))
            trwanie.append(random.randint(1, 20))
            priorytet.append(random.randint(1, 10))

    kwant = random.randint(1, 5)
    kwant1 = random.randint(1, 5)

    ziped = list(zip(przybycie, trwanie, priorytet))
    sorted_data = sorted(ziped, key=lambda x: x[0])
    przybycie, trwanie, priorytet = zip(*sorted_data)


    with open("dane.txt", "w") as output_file:
        output_file.write(" ".join(map(str, przybycie)) + "\n")
        output_file.write(" ".join(map(str, trwanie)) + "\n")
        output_file.write(" ".join(map(str, priorytet)) + "\n")
        output_file.write(str(kwant) + "\n")
        output_file.write(str(kwant1))


if __name__ == "__main__":
    generate()
