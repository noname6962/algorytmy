import random


def page_generation():
    odniesienia = []

    for i in range(0, 20):
        odniesienia.append(random.randint(0, 10))

    sloty = random.randint(1, 5)

    with open("dane_page.txt", "w") as output_file:
        output_file.write(" ".join(map(str, odniesienia)) + "\n")
        output_file.write(str(sloty))
