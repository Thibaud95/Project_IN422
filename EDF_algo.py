def EDF(processes, arrival_times, execution_times, deadlines, periods, time_limit):
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
                remaining_bt[instance_name] = execution_times[i]
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

    # 1. Vérification de la schedulabilité avec la formule d'utilisation CPU
    utilization = sum(execution_times[i] / periods[i] for i in range(n))
    bound = n * (2 ** (1/n) - 1)
    schedulable = utilization <= bound
    
    print(f"CPU Utilization: {utilization:.3f}")
    print(f"Utilization Bound: {bound:.3f}")
    print(f"Schedulable according to UB test: {schedulable}")
    
    import math

    # 2. Analyse de temps de réponse pour chaque tâche
    # TRIER les tâches selon priorité (plus petite période = plus prioritaire)
    sorted_tasks = sorted(zip(processes, arrival_times, execution_times, deadlines, periods), key=lambda x: x[3])
    sorted_processes, _, sorted_execution_times, _, sorted_periods = zip(*sorted_tasks)

    response_times = {}
    waiting_times = {}

    MAX_ITER = 10  # pour éviter les boucles infinies

    for i in range(n):
        C_i = sorted_execution_times[i]
        T_i = sorted_periods[i]
        R_prev = C_i

        for iteration in range(MAX_ITER):
            interference = 0
            for j in range(i):  # tâches de priorité plus haute (dans l’ordre trié !)
                C_j = sorted_execution_times[j]
                T_j = sorted_periods[j]
                interference += math.ceil(R_prev / T_j) * C_j

            R_next = C_i + interference

            if R_next == R_prev:
                break  # Convergence atteinte

            if R_next > T_i:
                R_next = float('inf')  # Tâche non schedulable
                break

            R_prev = R_next

        task_name = sorted_processes[i]
        response_times[task_name] = R_next
        waiting_times[task_name] = R_next - C_i if R_next != float('inf') else float('inf')

    
    print("\nResponse Time Analysis:")
    for i in range(n):
        print(f"{processes[i]}: R_i = {response_times[processes[i]]}, W_i = {waiting_times[processes[i]]}")

    avg_WT = sum(waiting_times.values()) / n


    print("Average WT:", avg_WT)
    avg_wt = avg_WT
    return {
        "CPU Utilization": utilization,
        "Utilization Bound": bound,
        "Response Time": response_times,
        "Waiting Time": waiting_times,
        "Average Waiting Time": avg_wt,
        "Schedule": timeline
    }
# Exemple d'utilisation
processes = ['P1', 'P2', 'P3']
arrival_times = [0, 0, 0]
execution_times = [3, 2, 2]
deadlines = [7, 4, 8]
periods = [20, 5, 10]
time_limit = 20

result = EDF(processes, arrival_times, execution_times, deadlines, periods, time_limit)

for key, value in result.items():
    print(f"{key}: {value}")

# suppose Output:['P2','P2','P1','P1','P1','P3','P3','P2','P2','none','P2','P2','P3','P3','none','P2','P2','none','none','none']

# suppose Output: {'Completion Time': {'P1': [3], 'P2': [5], 'P3': [7]}, 'Turnaround Time': {'P1': [3], 'P2': [5], 'P3': [7]}, 'Waiting Time': {'P1': [0], 'P2': [0], 'P3': [0]}, 'Average Turnaround Time': 5.0, 'Average Waiting Time': 0.0, 'Timeline': ['P1', 'P1', 'P1', 'none', 'P2