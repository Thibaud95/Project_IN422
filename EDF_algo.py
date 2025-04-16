def EDF(processes, arrival_times, burst_times, deadlines, periods, time_limit):
    from collections import deque

    # Initialisation
    n = len(processes)
    ready_queue = []
    remaining_bt = {}
    next_release = {p: 0 for p in processes}
    deadlines_map = {}
    active_process = None
    completed_instances = {p: [] for p in processes}
    timeline = []

    current_time = 0

    while current_time < time_limit:
        # Libération des nouvelles instances à t = current_time
        for i in range(n):
            p = processes[i]
            if current_time >= next_release[p] and current_time >= arrival_times[i]:
                instance_id = len([d for d in deadlines_map if d.startswith(p)])
                instance_name = f"{p}_{instance_id}"
                remaining_bt[instance_name] = burst_times[i]
                deadlines_map[instance_name] = current_time + deadlines[i]
                next_release[p] += periods[i]

        # Filtrage des tâches prêtes
        ready_tasks = [(dl, inst) for inst, dl in deadlines_map.items() if remaining_bt[inst] > 0]
        if ready_tasks:
            # Choisir la tâche avec la plus petite deadline
            ready_tasks.sort()
            _, chosen_instance = ready_tasks[0]
            timeline.append(chosen_instance.split("_")[0])
            remaining_bt[chosen_instance] -= 1
            if remaining_bt[chosen_instance] == 0:
                process_name = chosen_instance.split("_")[0]
                completed_instances[process_name].append(current_time + 1)
        else:
            timeline.append("none")

        current_time += 1

    # Calcul des métriques
    CT, TAT, WT = {}, {}, {}
    total_tat, total_wt, total_instances = 0, 0, 0

    for i in range(n):
        p = processes[i]
        CT[p] = completed_instances[p]
        TAT[p] = []
        WT[p] = []
        for j, ct in enumerate(CT[p]):
            release_time = arrival_times[i] + j * periods[i]
            tat = ct - release_time
            wt = tat - burst_times[i]
            TAT[p].append(tat)
            WT[p].append(wt)
            total_tat += tat
            total_wt += wt
            total_instances += 1

    avg_tat = total_tat / total_instances if total_instances else 0
    avg_wt = total_wt / total_instances if total_instances else 0

    return {
        "Completion Time": CT,
        "Turnaround Time": TAT,
        "Waiting Time": WT,
        "Average Turnaround Time": avg_tat,
        "Average Waiting Time": avg_wt,
        "Timeline": timeline
    }
# Exemple d'utilisation
processes = ['P1', 'P2', 'P3']
arrival_times = [0, 0, 0]
burst_times = [3, 2, 2]
deadlines = [7, 4, 8]
periods = [20, 5, 10]
time_limit = 20

result = EDF(processes, arrival_times, burst_times, deadlines, periods, time_limit)

for key, value in result.items():
    print(f"{key}: {value}")

# suppose Output:['P2','P2','P1','P1','P1','P3','P3','P2','P2','none','P2','P2','P3','P3','none','P2','P2','none','none','none']

# suppose Output: {'Completion Time': {'P1': [3], 'P2': [5], 'P3': [7]}, 'Turnaround Time': {'P1': [3], 'P2': [5], 'P3': [7]}, 'Waiting Time': {'P1': [0], 'P2': [0], 'P3': [0]}, 'Average Turnaround Time': 5.0, 'Average Waiting Time': 0.0, 'Timeline': ['P1', 'P1', 'P1', 'none', 'P2