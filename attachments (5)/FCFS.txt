def fcfs(process_list):
    t=0
    gantt=[]
    completed={}

    process_list.sort(key=lambda x:x[0])
    while process_list:
        if process_list[0][0]>t:
            gantt.append("Idle")
            t=process_list[0][0]
            continue
        process=process_list.pop(0)
        arrival_time,burst_time,pid=process
        gantt.append(pid)
        t+=burst_time
        completion_time=t
        turnaround=completion_time-arrival_time
        waiting=turnaround-burst_time

        completed[pid]=[completion_time,turnaround,waiting]
    
    print("Gantt Chart:")
    print(" -> ".join(gantt))
    print("\nProcess Details:")
    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid,(ct,tt,wt) in completed.items():
        print(f"{pid}\t{ct}\t\t{tt}\t\t{wt}")

if __name__=="__main__":
    process_list=[(2,6,"P1"),(5,2,"P2"),(1,8,"P3"),(0,3,"P4"),(4,4,"P5")]
    fcfs(process_list)
