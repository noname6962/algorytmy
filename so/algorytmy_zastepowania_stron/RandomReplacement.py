import random


def faults_random_replacment(odniesienia, sloty):
    check = []
    faults = 0
    hit = 0
    x=-1

    with open("../algorytmy_planowania/raport.txt", "w") as report_file:
        report_file.write("Simulation Report - opt page replacment\n\n")

        for i in range(len(odniesienia)):
            if odniesienia[i] in check:
                hit = hit + 1
                report_file.write(f"{check}   hit\n")
                continue
            else:
                if len(check) < sloty:
                    check.append(odniesienia[i])
                    faults = faults + 1
                    x = x +1
                else:
                    x = random.randint(0, sloty-1)
                    check[x] = odniesienia[i]
                    faults = faults + 1

            report_file.write(f"{check}   zamiana na slocie {x} \n")
        report_file.write(f"Faults: {faults}")
    return faults, hit


if __name__ == '__main__':
    with open("dane_page.txt", "r") as input_file:
        odniesienia = list(map(int, input_file.readline().split()))
        slots = int(input_file.readline())

    faults_random_replacment(odniesienia, slots)
