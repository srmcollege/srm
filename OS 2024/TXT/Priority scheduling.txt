def priority_scheduling(processes):
    processes.sort(key=lambda p: (p[0], p[2]))
    time, total_tat, total_wt = 0, 0, 0
    gantt_chart = []
    table_data = []

    for p in processes:
        if p[0] > time:
            gantt_chart.append("idle")
            time = p[0]

        gantt_chart.append(p[3])
        completion_time = time + p[1]
        tat = completion_time - p[0]
        wt = tat - p[1]
        total_tat += tat
        total_wt += wt
        table_data.append([p[3], p[0], p[1], p[2], completion_time, tat, wt])
        time = completion_time

    print("PID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for row in table_data:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t\t{row[4]}\t\t{row[5]}\t\t{row[6]}")

    n = len(processes)
    print(f"\nAverage Turnaround Time = {total_tat / n:.2f}")
    print(f"Average Waiting Time = {total_wt / n:.2f}")
    print(f"\nGantt Chart: {gantt_chart}")

processes = [
    (0, 3, 2, "P1"),
    (2, 5, 6, "P2"),
    (1, 4, 3, "P3"),
    (4, 2, 5, "P4"),
    (6, 9, 7, "P5"),
    (5, 4, 4, "P6"),
    (7, 10, 19,"P7")
]
priority_scheduling(processes)
