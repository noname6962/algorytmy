def ready_queue_generator(sorted_arrival_times, current_time, ready_queue, compleated_tasks):

    ready_queue.clear()

    for i in range(len(sorted_arrival_times)):
        if sorted_arrival_times[i] <= current_time:
            if i not in compleated_tasks:
                ready_queue.append(i)


def sjf_scheduling(arrival_times, durations):
    current_time = 0
    waiting_time = 0
    turnaround_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    compleated_tasks = []
    ready_queue = []

    tasks = list(zip(arrival_times, durations))
    tasks.sort(key=lambda x: x[1])
    sorted_arrival_times = [task[0] for task in tasks]
    sorted_durations = [task[1] for task in tasks]

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - SJF Scheduling\n\n")

        while len(compleated_tasks) < len(arrival_times):
            ready_queue_generator(sorted_arrival_times, current_time, ready_queue, compleated_tasks)

            while not ready_queue:
                current_time += 1
                ready_queue_generator(sorted_arrival_times, current_time, ready_queue, compleated_tasks)

            current_time += sorted_durations[ready_queue[0]]
            waiting_time = current_time - sorted_arrival_times[ready_queue[0]] - sorted_durations[ready_queue[0]]
            turnaround_time = waiting_time + sorted_durations[ready_queue[0]]
            compleated_tasks.append(ready_queue[0])

            report_file.write(f"Task: Arrival Time={sorted_arrival_times[ready_queue[0]]}, Duration={sorted_durations[ready_queue[0]]}\n")
            report_file.write(f"Start Time: {current_time - sorted_durations[ready_queue[0]]}\n")
            report_file.write(f"End Time: {current_time}\n")
            report_file.write(f"Waiting Time: {waiting_time}\n")
            report_file.write(f"Turnaround Time: {turnaround_time}\n\n")
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

        average_waiting_time = total_waiting_time / len(arrival_times)
        average_turnaround_time = total_turnaround_time / len(arrival_times)

        report_file.write("Average Waiting Time: {:.2f}\n".format(average_waiting_time))
        report_file.write("Average Turnaround Time: {:.2f}\n".format(average_turnaround_time))
        report_file.write(f"Turnaround Time: {current_time}\n\n")
    return average_waiting_time, average_turnaround_time

if __name__ == "__main__":
    # Read input from the file
    with open("dane.txt", "r") as input_file:
        arrival_times = list(map(int, input_file.readline().split()))
        durations = list(map(int, input_file.readline().split()))

    # Run SJF scheduling algorithm
    sjf_scheduling(arrival_times, durations)

    print("Simulation report generated in 'sjf_simulation_report.txt'")
