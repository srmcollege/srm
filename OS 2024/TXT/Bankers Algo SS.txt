P = 5                  
R = 3                  
available = [3, 3, 2]  

max_need = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
]

allocated = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
]

need = [
    [7, 4, 3],  # P0
    [1, 2, 2],  # P1
    [6, 0, 0],  # P2
    [0, 1, 1],  # P3
    [4, 3, 1]   # P4
]

def is_safe(available, max_need, allocated, need, P, R):
    work = available[:]
    finish = [False] * P
    safe_sequence = []
    
    while len(safe_sequence) < P:
        found = False
        for i in range(P):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(R)):
                for j in range(R):
                    work[j] += allocated[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break

        if not found:
            print("The system is not in a safe state.")
            return False

    print("The system is in a safe state.")
    print("Safe sequence is:", safe_sequence)
    return True

is_safe(available, max_need, allocated, need, P, R)

