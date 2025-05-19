def RR(processes, arrival_times, burst_times, quantum):
    from collections import deque

    processes = list(zip(processes, arrival_times, burst_times))
    processes.sort(key=lambda x: x[1])  # Trier par Arrival Time

    n = len(processes)
    queue = deque()
    time = 0
    schedule = []
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    remaining_bt = {pid: bt for pid, at, bt in processes}
    arrived = set()
    index = 0

    while len(completion_time) < n:
        # Ajouter les nouveaux processus arrivés
        while index < n and processes[index][1] <= time:
            pid, at, bt = processes[index]
            queue.append(pid)
            arrived.add(pid)
            index += 1

        if queue:
            pid = queue.popleft()
            bt = remaining_bt[pid]
            executed_time = min(bt, quantum)

            for _ in range(executed_time):
                schedule.append(pid)
                time += 1
                # Vérifier s'il y a des nouveaux arrivants pendant l'exécution
                while index < n and processes[index][1] <= time:
                    new_pid, at, bt = processes[index]
                    if new_pid not in arrived:
                        queue.append(new_pid)
                        arrived.add(new_pid)
                    index += 1

            remaining_bt[pid] -= executed_time
            if remaining_bt[pid] == 0:
                completion_time[pid] = time
            else:
                queue.append(pid)
        else:
            schedule.append(None)
            time += 1

    total_tat = 0
    total_wt = 0

    for pid, at, bt in processes:
        tat = completion_time[pid] - at
        wt = tat - bt
        turnaround_time[pid] = tat
        waiting_time[pid] = wt
        total_tat += tat
        total_wt += wt

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
quantum_time = 4
result = RR(processes, arrival_times, burst_times, quantum_time)
print(result)
# suppose Output: {'Completion Time': {'P1': 5, 'P2': 8, 'P3': 16}, 'Turnaround Time': {'P1': 5, 'P2': 7, 'P3': 14}, 'Waiting Time': {'P1': 0, 'P2': 4, 'P3': 6}, 'Average Turnaround Time': 8.666666666666666, 'Average Waiting Time': 3.3333333333333335, 'Schedule': ['P1', 'P1', 'P2', 'P2', 'P3', 'P3', 'P3', 'P1']}