import numpy as np


def RM(processes, arrival_times, execution_times, periods, total_time):
    n = len(processes)
    schedule = []
    
    # Infos dynamiques pour chaque tâche
    next_arrival = [arrival_times[i] for i in range(n)]
    remaining_bt = [0] * n
    task_count = [0] * n  # Nombre d'instances arrivées
    completions = []  # Liste de tuples (process, completion time)
    
    time = 0

    # Priorités selon période (plus la période est petite, plus la priorité est haute)
    priorities = sorted(range(n), key=lambda i: periods[i])

    while time < total_time:
        # Mise à jour : on relâche les nouvelles instances
        for i in range(n):
            if time == next_arrival[i]:
                remaining_bt[i] += execution_times[i]
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
    sorted_tasks = sorted(zip(processes, arrival_times, execution_times, periods), key=lambda x: x[3])
    sorted_processes, _, sorted_execution_times, sorted_periods = zip(*sorted_tasks)

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
        "Schedule": schedule
    }



# Exemple d'utilisation
processes = ["P1", "P2", "P3"]
arrival_times = [0, 0, 0]
execution_times = [1, 2, 3]
periods = [4, 5, 10]
total_time = 20

RM(processes, arrival_times, execution_times, periods, total_time)
# suppose Output: {'Schedule': ['P1','P2','P2','P3','P1','P2','P2','P3','P1','P3','P2','P2','P1','P3','P3','P2','P1','P2','P3','none']
