def aging(arrival_times, priorities, time_quant_aging, compleated_tasks, current_time, last_aging):
    if current_time - last_aging >= time_quant_aging:
        time_of_aging = current_time
        for i in range(len(priorities)):
            if i not in compleated_tasks:
                if arrival_times[i] <= time_of_aging:
                    priorities[i] = priorities[i] - 1


def que(arrival_times, priorities, ready_queue, current_time, compleated_tasks, current_priority, working_task):
    to_do = []
    for i in range(len(priorities)):
        if i not in compleated_tasks:
            if arrival_times[i] <= current_time:
                to_do.append(i)
        else:
            continue

    if to_do:
        current_priority = priorities[to_do[0]]
        for i in range(len(to_do)):
            if priorities[to_do[i]] < current_priority:
                current_priority = priorities[to_do[i]]
            else:
                continue

    for i in range(len(priorities)):
        if i not in compleated_tasks:
            if i not in ready_queue:
                if arrival_times[i] <= current_time:
                    if priorities[i] == current_priority:
                        ready_queue.append(i)



def round_robin_priority_scheduling(arrival_times, durations, priorities, time_quant_aging, time_quantum_rr):
    waiting_time = [0] * len(arrival_times)
    turnaround_time = [0] * len(arrival_times)
    og_durations = list(durations)
    ready_queue = []
    compleated_tasks = []

    current_time = min(arrival_times)
    current_priority = priorities[0]
    working_task = 0
    last_aging = 0

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - Round Robin Priority Scheduling with Aging\n\n")

        while len(compleated_tasks) < len(arrival_times):

            que(arrival_times, priorities, ready_queue, current_time, compleated_tasks, current_priority, working_task)

            if not ready_queue:
                current_time += 1
            else:
                durations[ready_queue[working_task]] = durations[ready_queue[working_task]] - time_quantum_rr

                if durations[ready_queue[working_task]] > 0:
                    current_time = current_time + time_quantum_rr
                    report_file.write(f"Task {ready_queue[working_task]}:\n")
                    report_file.write(f"priority {priorities[ready_queue[working_task]]}:\n")
                    report_file.write(f"Start Time: {current_time - time_quantum_rr}\n")
                    report_file.write(f"End Time: {current_time}\n\n")
                    working_task = working_task + 1

                elif durations[ready_queue[working_task]] <= 0:
                    current_time = current_time + time_quantum_rr + durations[ready_queue[working_task]]
                    turnaround_time[ready_queue[working_task]] = current_time - arrival_times[ready_queue[working_task]]
                    waiting_time[ready_queue[working_task]] = turnaround_time[ready_queue[working_task]] - og_durations[ready_queue[working_task]]
                    compleated_tasks.append(ready_queue[working_task])
                    report_file.write(f"Task compleated \n")
                    report_file.write(f"Task {ready_queue[working_task]}:\n")
                    report_file.write(f"priority {priorities[ready_queue[working_task]]}:\n")
                    report_file.write(f"Start Time: {current_time - durations[ready_queue[working_task]] - time_quantum_rr}\n")
                    report_file.write(f"End Time: {current_time}\n")
                    report_file.write(f"Waiting Time: {waiting_time[ready_queue[working_task]]}\n")
                    report_file.write(f"Turnaround Time: {turnaround_time[ready_queue[working_task]]}\n\n")
                    ready_queue.pop(working_task)

            if working_task >= len(ready_queue):
                working_task = 0

            aging(arrival_times, priorities, time_quant_aging, compleated_tasks, current_time, last_aging)

        average_waiting_time = sum(waiting_time) / len(arrival_times)
        average_turnaround_time = sum(turnaround_time) / len(arrival_times)

        report_file.write("Average Waiting Time: {:.2f}\n".format(average_waiting_time))
        report_file.write("Average Turnaround Time: {:.2f}\n".format(average_turnaround_time))
    return average_waiting_time, average_turnaround_time


with open("dane.txt", "r") as input_file:
    arrival_times = list(map(int, input_file.readline().split()))
    durations = list(map(int, input_file.readline().split()))
    priorities = list(map(int, input_file.readline().split()))
    time_quant_aging = int(input_file.readline())
    time_quantum_rr = int(input_file.readline())

while(1):
    dane = 0
    try:
        dane = int(input("jezeli chcesz dopisac proces do puli wpisz 1 w przeciwnym wypadku wpsiz dowolna wartosc: "))
        if dane == 1:
            arrival_times.append(int(input("podaj czas przybycia: ")))
            durations.append(int(input("podaj czas trwania: ")))
            priorities.append(int(input("podaj priorytet: ")))
        else:
            break
    except ValueError:
        print("bledne dane")


# Run Round Robin Priority scheduling algorithm
round_robin_priority_scheduling(arrival_times, durations, priorities, time_quant_aging, time_quantum_rr)

print("Simulation report generated in 'raport.txt'")
