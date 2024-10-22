processes=5
resources=3

max_res = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
allocated_res=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
ava_res = [3,3,2]

def calculate_need():
    need=[]
    for i in range(processes):
        row=[]
        for j in range(resources):
            row.append(max_res[i][j]-allocated_res[i][j])
        need.append(row)
    return need

def is_safe(need):
    work=ava_res[:]
    finish=[False]*processes
    safe_sequence=[]
    while len(safe_sequence)<processes:
        found_safe_process=False
        for i in range(processes):
            if not finish[i]:
                can_allocate=True
                for j in range(resources):
                    if need[i][j]>work[j]:
                        can_allocate=False
                        break
                if can_allocate:
                    for j in range(resources):
                        work[j]+=allocated_res[i][j]
                    finish[i]=True
                    safe_sequence.append(i)
                    found_safe_process=True
                    break
        if not found_safe_process:
            return False,[]
    return True,safe_sequence

def bankers_algorithm():
    need=calculate_need()
    for i in range(processes):
        print(f"Process {i}: {need[i]}")
    safe_flag,safe_seq=is_safe(need)
    if safe_flag:
        print("\nThe system is in a safe state.")
        print("Safe sequence is:",safe_seq)
    else:
        print("\nThe system is not in a safe state.")

bankers_algorithm()
