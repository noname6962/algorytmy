def fcfs_scheduling(arrival_times, durations):
    current_time = 0
    waiting_time = 0
    turnaround_time = 0

    with open("raport.txt", "w") as report_file:
        report_file.write("Simulation Report - FCFS Scheduling\n\n")

        for arrival, duration in zip(arrival_times, durations):
            if arrival > current_time:
                current_time = arrival

            waiting_time += current_time - arrival
            turnaround_time += waiting_time + duration

            report_file.write(f"Task: Arrival Time={arrival}, Duration={duration}\n")
            report_file.write(f"Start Time: {current_time}\n")
            report_file.write(f"End Time: {current_time + duration}\n")
            report_file.write(f"Waiting Time: {waiting_time}\n")
            report_file.write(f"Turnaround Time: {turnaround_time}\n\n")

            current_time += duration

        average_waiting_time = waiting_time / len(arrival_times)
        average_turnaround_time = turnaround_time / len(arrival_times)

        report_file.write("Average Waiting Time: {:.2f}\n".format(average_waiting_time))
        report_file.write("Average Turnaround Time: {:.2f}\n".format(average_turnaround_time))
        report_file.write(f"Turnaround Time: {current_time}\n\n")

    return average_waiting_time, average_turnaround_time, current_time


if __name__ == "__main__":
    # Read input from the file
    with open("dane.txt", "r") as input_file:
        arrival_times = list(map(int, input_file.readline().split()))
        durations = list(map(int, input_file.readline().split()))

    # Run FCFS scheduling algorithm
    fcfs_scheduling(arrival_times, durations)

    print("Simulation report generated in 'raport.txt'")
