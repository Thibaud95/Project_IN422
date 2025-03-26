def FCFS(processes):
    processes.sort(key=lambda x: x[1])  # Trier selon l'Arrival Time (AT)
    
    time = 0
    schedule = []
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    total_tat = 0
    total_wt = 0
    
    for process in processes:
        pid, at, bt = process
        if time < at:
            time = at  # Attendre que le processus arrive
        
        for _ in range(bt):
            schedule.append(pid)
            time += 1
        
        completion_time[pid] = time
        turnaround_time[pid] = completion_time[pid] - at
        waiting_time[pid] = turnaround_time[pid] - bt
        total_tat += turnaround_time[pid]
        total_wt += waiting_time[pid]
    
    n = len(processes)
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    
    return {
        "Completion Time": completion_time,
        "Turnaround Time": turnaround_time,
        "Waiting Time": waiting_time,
        "Average Turnaround Time": avg_tat,
        "Average Waiting Time": avg_wt,
        "Schedule": schedule
    }

# Exemple d'utilisation
process_list = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 8)]
result = FCFS(process_list)
print(result)
# Output: {'Completion Time': {'P1': 5, 'P2': 8, 'P3': 16}, 'Turnaround Time': {'P1': 5, 'P2': 7, 'P3': 14}, 'Waiting Time': {'P1': 0, 'P2': 4, 'P3': 6}, 'Average Turnaround Time': 8.666666666666666, 'Average Waiting Time': 3.3333333333333335, 'Schedule': ['P1', 'P2', 'P2', 'P2', 'P1