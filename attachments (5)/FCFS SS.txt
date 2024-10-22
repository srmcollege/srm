def fcfs(process_list):
    process_list.sort(key=lambda x: (x[0], x[2]))
    t = 0             
    gantt = []        
    completed = {}    
    total_tat = 0
    total_wt = 0      
    
    while process_list:
        if process_list[0][0] > t:
            gantt.append("idle")
            t += 1
            continue
        at, bt, pid = process_list.pop(0)
        gantt.append(pid)
        t += bt  
        ct = t 
        tat = ct - at  
        wt = tat - bt 
        completed[pid] = [at, bt, ct, tat, wt]
        total_tat += tat
        total_wt += wt

    num_processes = len(completed)
    avg_tat = total_tat / num_processes
    avg_wt = total_wt / num_processes

    print("\nPID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for pid in sorted(completed.keys()):  
        stats = completed[pid]
        print(f"{pid}\t{stats[0]}\t{stats[1]}\t{stats[2]}\t\t{stats[3]}\t\t{stats[4]}")
    
    print()
    print("Average Turnaround Time is", avg_tat)
    print("Average Waiting Time is", avg_wt)
    
    print()
    print("Gantt Chart:", gantt)

if __name__ == "__main__":
    process_list = [(3, 4, "p1"), (5, 3, "p2"), (0, 2, "p3"), (5, 1, "p4"), (4, 3, "p5")]
    fcfs(process_list)

