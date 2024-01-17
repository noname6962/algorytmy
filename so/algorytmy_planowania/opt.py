def przewidzenie(odniesienia, check, i, slots):
    wizja = [0] * slots

    for j in range(slots):
        for k in range(i+1, len(odniesienia)):
            if odniesienia[k] != check[j]:
                wizja[j] = wizja[j] + 1
            else:
                break
    return wizja.index(max(wizja))

def faults_opt(odniesienia, slots):
    check = []
    hit = 0
    faults = 0
    x = -1

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - opt page replacment\n\n")

        for i in range(len(odniesienia)):
            if odniesienia[i] in check:
                report_file.write(f"{check}   hit\n")
                hit = hit + 1
                continue
            else:
                if len(check) < slots:
                    check.append(odniesienia[i])
                    faults = faults + 1
                    x = x + 1
                else:
                    check[przewidzenie(odniesienia, check, i, slots)] = odniesienia[i]
                    faults = faults + 1
                    x = przewidzenie(odniesienia, check, i, slots)

            report_file.write(f"{check}   zamiana na slocie {x}\n")
        report_file.write(f"Faults: {faults}")
    return faults, hit





if __name__ == '__main__':
    with open("../algorytmy_zastepowania_stron/dane_page.txt", "r") as input_file:
        odniesienia = list(map(int, input_file.readline().split()))
        slots = int(input_file.readline())

    faults_opt(odniesienia, slots)

