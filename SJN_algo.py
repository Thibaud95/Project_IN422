def SJN(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Trier par Arrival Time (AT), puis par Burst Time (BT)
    
    time = 0
    schedule = []
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    total_tat = 0
    total_wt = 0
    ready_queue = []
    index = 0
    n = len(processes)
    
    while len(completion_time) < n:
        while index < n and processes[index][1] <= time:
            ready_queue.append(processes[index])
            index += 1
        
        if ready_queue:
            ready_queue.sort(key=lambda x: x[2])  # Trier par Burst Time (BT)
            process = ready_queue.pop(0)
            pid, at, bt = process
            
            for _ in range(bt):
                schedule.append(pid)
                time += 1
            
            completion_time[pid] = time
            turnaround_time[pid] = completion_time[pid] - at
            waiting_time[pid] = turnaround_time[pid] - bt
            total_tat += turnaround_time[pid]
            total_wt += waiting_time[pid]
        else:
            schedule.append(None)  # Aucun processus en cours d'exécution
            time += 1
    
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
process_list = [("P1", 0, 7), ("P2", 2, 4), ("P3", 4, 1), ("P4", 5, 4)]
result = SJN(process_list)
print(result)
# suppose Output: {'Completion Time': {'P1': 11, 'P2': 15, 'P3': 16, 'P4': 20}, 'Turnaround Time': {'P1': 11, 'P2': 13, 'P3': 12, 'P4': 15}, 'Waiting Time': {'P1': 4, 'P2': 9, 'P3': 11, 'P4': 11}, 'Average Turnaround Time': 12.75, 'Average Waiting Time': 8.75, 'Schedule': ['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P2', 'P3', 'P4', 'P4', 'P4', 'P4']}