processes = ['P1', 'P2', 'P3', 'P4']
burst_time = [5, 4, 2, 1]
arrival_time = [0, 1, 2, 4]
time_quantum = 2

n = len(processes)
remaining_burst_time = burst_time[:]
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n
time = 0
gantt_chart = []

while True:
    all_done = True
    for i in range(n):
        if remaining_burst_time[i] > 0:  
            all_done = False
            if arrival_time[i] <= time:  
                exec_time = min(remaining_burst_time[i], time_quantum)
                gantt_chart.append((processes[i], time, time + exec_time))
                remaining_burst_time[i] -= exec_time
                time += exec_time
                if remaining_burst_time[i] == 0:  
                    completion_time[i] = time

    if all_done:  
        break

for i in range(n):
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

average_turnaround_time = sum(turnaround_time) / n
average_waiting_time = sum(waiting_time) / n

print("Gantt Chart:")
for entry in gantt_chart:
    print(f"{entry[0]}: {entry[1]}-{entry[2]}ms", end=" | ")
print("\n")

print("{:<10} {:<15} {:<15} {:<20} {:<20} {:<20}".format(
    "PID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"))
for i in range(n):
    print("{:<10} {:<15} {:<15} {:<20} {:<20} {:<20}".format(
        processes[i], arrival_time[i], burst_time[i], completion_time[i], turnaround_time[i], waiting_time[i]))

print("\nAverage Turnaround Time: {:.2f} ms".format(average_turnaround_time))
print("Average Waiting Time: {:.2f} ms".format(average_waiting_time))
