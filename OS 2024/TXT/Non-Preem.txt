def priority_scheduling(process_list):
    process_list.sort(key=lambda x: (x[0], x[2], x[3]))
    t = 0             
    gantt = []        
    completed = {}    
    total_tat = 0
    total_wt = 0      

    while process_list:
        available_processes = [p for p in process_list if p[0] <= t]
        
        if not available_processes:
            gantt.append("idle")
            t += 1
            continue

        available_processes.sort(key=lambda x: (x[2], x[0], x[3]))
        selected_process = available_processes[0]
        process_list.remove(selected_process)
        
        at, bt, priority, pid = selected_process
        gantt.append(pid)
        t += bt  
        ct = t 
        tat = ct - at  
        wt = tat - bt 
        completed[pid] = [at, bt, priority, ct, tat, wt]
        total_tat += tat
        total_wt += wt

    num_processes = len(completed)
    avg_tat = total_tat / num_processes
    avg_wt = total_wt / num_processes

    print("\nPID\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for pid in sorted(completed.keys()):  
        stats = completed[pid]
        print(f"{pid}\t{stats[0]}\t{stats[1]}\t{stats[2]}\t\t{stats[3]}\t\t{stats[4]}\t\t{stats[5]}")
    
    print()
    print("Average Turnaround Time is", avg_tat)
    print("Average Waiting Time is", avg_wt)
    
    print()
    print("Gantt Chart:", gantt)

if __name__ == "__main__":
    process_list = [
        (0, 3, 2, "p1"),
        (2, 5, 6, "p2"),
        (1, 4, 3, "p3"),
        (4, 2, 5, "p4"),
        (6, 9, 7, "p5"),
        (5, 4, 4, "p6"),
        (7, 10, 19, "p7")
    ]
    priority_scheduling(process_list)


