def RM(processes, arrival_times, burst_times, periods, total_time):
    n = len(processes)
    schedule = []
    
    # Infos dynamiques pour chaque tâche
    next_arrival = [arrival_times[i] for i in range(n)]
    remaining_bt = [0] * n
    task_count = [0] * n  # Nombre d'instances arrivées
    completions = []  # Liste de tuples (process, completion time)
    
    time = 0
    active_tasks = []

    # Priorités selon période (plus la période est petite, plus la priorité est haute)
    priorities = sorted(range(n), key=lambda i: periods[i])

    while time < total_time:
        # Mise à jour : on relâche les nouvelles instances
        for i in range(n):
            if time == next_arrival[i]:
                remaining_bt[i] += burst_times[i]
                task_count[i] += 1
                next_arrival[i] += periods[i]

        # Sélection de la tâche avec la priorité la plus haute qui est prête
        current_task = None
        for i in priorities:
            if remaining_bt[i] > 0:
                current_task = i
                break

        if current_task is not None:
            remaining_bt[current_task] -= 1
            schedule.append(processes[current_task])

            # Si l’instance est terminée
            if remaining_bt[current_task] == 0:
                completions.append((processes[current_task], time + 1))
        else:
            schedule.append("none")

        time += 1

    # Recalcul des métriques
    CT = {p: 0 for p in processes}
    TAT = {p: 0 for p in processes}
    WT = {p: 0 for p in processes}
    count = {p: 0 for p in processes}

    for i, p in enumerate(processes):
        num_instances = task_count[i]
        period = periods[i]
        bt = burst_times[i]
        completed = 0
        last_completion = 0
        for t in range(total_time):
            if schedule[t] == p:
                if remaining_bt[i] == 0:
                    last_completion = t + 1
        CT[p] = last_completion
        TAT[p] = num_instances * period
        WT[p] = TAT[p] - (num_instances * bt)
        count[p] = num_instances

    avg_TAT = sum(TAT.values()) / n
    avg_WT = sum(WT.values()) / n

    print("Schedule:", schedule)
    print("Completion Time:", CT)
    print("Turnaround Time:", TAT)
    print("Waiting Time:", WT)
    print("Average TAT:", avg_TAT)
    print("Average WT:", avg_WT)
    completion_time = CT
    turnaround_time = TAT
    waiting_time = WT
    avg_tat = avg_TAT
    avg_wt = avg_WT
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
arrival_times = [0, 0, 0]
burst_times = [1, 2, 3]
periods = [4, 5, 10]
total_time = 20

RM(processes, arrival_times, burst_times, periods, total_time)
# suppose Output: {'Schedule': ['P1','P2','P2','P3','P1','P2','P2','P3','P1','P3','P2','P2','P1','P3','P3','P2','P1','P2','P3','none']

# 'Completion Time': {'P1': 20, 'P2': 20, 'P3': 20}, 'Turnaround Time': {'P1': 20, 'P2': 20, 'P3': 20}, 'Waiting Time': {'P1': 19, 'P2': 18, 'P3': 17}, 'Average TAT': 20.0, 'Average WT': 18.0}