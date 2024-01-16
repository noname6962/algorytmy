def fcfs_scheduling(arrival_times, durations):
    tasks = list(zip(arrival_times, durations))
    tasks.sort(key=lambda x: x[0])
    sorted_arrival_times = [task[0] for task in tasks]
    sorted_durations = [task[1] for task in tasks]

    current_time = 0
    waiting_time = 0
    turnaround_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - FCFS Scheduling\n\n")

        for i in range(len(sorted_arrival_times)):
            if sorted_arrival_times[i] > current_time:
                current_time = sorted_arrival_times[i]

            waiting_time = current_time - sorted_arrival_times[i]
            turnaround_time = waiting_time + sorted_durations[i]

            report_file.write(f"Task: Arrival Time={sorted_arrival_times[i]}, Duration={sorted_durations[i]}\n")
            report_file.write(f"Start Time: {current_time}\n")
            report_file.write(f"End Time: {current_time + sorted_durations[i]}\n")
            report_file.write(f"Waiting Time: {waiting_time}\n")
            report_file.write(f"Turnaround Time: {turnaround_time}\n\n")
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time
            current_time += sorted_durations[i]

        average_waiting_time = total_waiting_time / len(sorted_arrival_times)
        average_turnaround_time = total_turnaround_time / len(sorted_arrival_times)

        report_file.write("Average Waiting Time: {:.2f}\n".format(average_waiting_time))
        report_file.write("Average Turnaround Time: {:.2f}\n".format(average_turnaround_time))
        report_file.write(f"Turnaround Time: {current_time}\n\n")
    return average_waiting_time, average_turnaround_time


if __name__ == "__main__":
    # Read input from the file
    with open("dane.txt", "r") as input_file:
        arrival_times = list(map(int, input_file.readline().split()))
        durations = list(map(int, input_file.readline().split()))

    # Run FCFS scheduling algorithm
    fcfs_scheduling(arrival_times, durations)

    print("Simulation report generated in 'raport.txt'")
