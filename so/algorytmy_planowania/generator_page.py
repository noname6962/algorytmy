import random


def page_generation():
    odniesienia = []

    x = random.randint(20, 100)
    for i in range(0, x):
        odniesienia.append(random.randint(0, 10))

    sloty = random.randint(2, 5)

    with open("../algorytmy_zastepowania_stron/dane_page.txt", "w") as output_file:
        output_file.write(" ".join(map(str, odniesienia)) + "\n")
        output_file.write(str(sloty))


if __name__ == '__main__':
    page_generation()
