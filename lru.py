def faults(odniesienia, sloty):
    check = []
    far_check = [0] * sloty
    faults = 0

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - opt page replacment\n\n")

        for i in range(len(odniesienia)):
            if odniesienia[i] in check:
                report_file.write(f"{check}\n")
                continue
            else:
                if len(check) < sloty:
                    check.append(odniesienia[i])
                    faults = faults + 1

                    for j in range(i+1):
                        far_check[j] = far_check[j] + 1
                else:
                    zastapienie = far_check.index(max(far_check))
                    check[zastapienie] = odniesienia[i]
                    far_check[zastapienie] = 0
                    for j in range(len(far_check)):
                        far_check[j] = far_check[j] + 1

                    faults = faults + 1

            report_file.write(f"{check}\n")
        report_file.write(f"Faults: {faults}")

if __name__ == '__main__':
    with open("dane_page.txt", "r") as input_file:
        odniesienia = list(map(int, input_file.readline().split()))
        slots = int(input_file.readline())

    faults(odniesienia, slots)
