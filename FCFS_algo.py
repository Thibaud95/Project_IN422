def FCFS(processes, arrival_times, burst_times):
    processes = list(zip(processes, arrival_times, burst_times))
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
            while time < at:
                schedule.append(None)  # Ajoute du vide
                time += 1
        
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
processes = ["P1", "P2", "P3"]
arrival_times = [0, 1, 2]
burst_times = [5, 3, 8]

result = FCFS(processes, arrival_times, burst_times)
print(result)
# suppose Output: {'Completion Time': {'P1': 5, 'P2': 8, 'P3': 16}, 'Turnaround Time': {'P1': 5, 'P2': 7, 'P3': 14}, 'Waiting Time': {'P1': 0, 'P2': 4, 'P3': 6}, 'Average Turnaround Time': 8.666666666666666, 'Average Waiting Time': 3.3333333333333335, 'Schedule': ['P1', 'P2', 'P2', 'P2', 'P1
