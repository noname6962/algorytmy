def faults_fifo(odniesienia, sloty):
    check = []
    faults = 0
    hit = 0
    x = 0
    with open("FIFO_raport.txt", "w") as report_file:
        report_file.write("Simulation Report - fifo page replacment\n\n")

        for i in range(len(odniesienia)):
            if odniesienia[i] in check:
                hit = hit + 1
                report_file.write(f"{check}    hit\n")
                continue
            else:
                if len(check) < sloty:
                    check.append(odniesienia[i])
                    faults = faults + 1
                else:
                    check[x] = odniesienia[i]
                    faults = faults + 1
            if x < sloty - 1:
                x = x + 1
                report_file.write(f"{check}    zamiana na slocie {x - 1}\n")
            else:
                x = 0
                report_file.write(f"{check}    zamiana na slocie {sloty - 1}\n")

        report_file.write(f"Faults: {faults}")
    return faults, hit


if __name__ == '__main__':
    with open("../dane_page.txt", "r") as input_file:
        odniesienia = list(map(int, input_file.readline().split()))
        slots = int(input_file.readline())

    faults_fifo(odniesienia, slots)
