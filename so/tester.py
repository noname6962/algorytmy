from so.algorytmy_zastepowania_stron.FCFS import fcfs_scheduling
from so.algorytmy_zastepowania_stron.sjf import sjf_scheduling
from so.algorytmy_zastepowania_stron.RR1 import round_robin_priority_scheduling
from so.algorytmy_zastepowania_stron.generator import generate

wait, turnaround = 0, 0
FCFS_wait_list, FCFS_turnaround_list = [], []
SJF_wait_list, SJF_turnaround_list = [],[]
RR_wait_list, RR_turnaround_list = [], []





for i in range(100000):
    print(i)
    generate()
    with open("algorytmy_zastepowania_stron/dane.txt", "r") as input_file:
        arrival_times = list(map(int, input_file.readline().split()))
        durations = list(map(int, input_file.readline().split()))
        priorities = list(map(int, input_file.readline().split()))
        time_quant_aging = int(input_file.readline())
        time_quantum_rr = int(input_file.readline())

    wait, turnaround = fcfs_scheduling(arrival_times, durations)
    FCFS_wait_list.append(wait)
    FCFS_turnaround_list.append(turnaround)
    wait, turnaround = sjf_scheduling(arrival_times, durations)
    SJF_wait_list.append(wait)
    SJF_turnaround_list.append(turnaround)
    wait, turnaround = round_robin_priority_scheduling(arrival_times, durations, priorities, time_quant_aging, time_quantum_rr)
    RR_wait_list.append(wait)
    RR_turnaround_list.append(turnaround)


with open("algorytmy_zastepowania_stron/raport_100k.txt", "w") as report_file:
    report_file.write("porownanie wynikow dla 100 000 powtorzen\n\n")
    report_file.write(F"sredni czas oczekiwania FCFS {sum(FCFS_wait_list)/len(FCFS_wait_list)} \n")
    report_file.write(F"sredni czas wykonania FCFS {sum(FCFS_turnaround_list)/len(FCFS_turnaround_list)} \n")
    report_file.write(F"sredni czas oczekiwania RR {sum(RR_wait_list)/len(RR_wait_list)} \n")
    report_file.write(F"sredni czas oczekiwania RR {sum(RR_turnaround_list)/len(RR_turnaround_list)} \n")
    report_file.write(F"sredni czas oczekiwania SJF {sum(SJF_wait_list)/len(SJF_wait_list)} \n")
    report_file.write(F"sredni czas oczekiwania SJF {sum(SJF_turnaround_list)/len(SJF_turnaround_list)} \n")




