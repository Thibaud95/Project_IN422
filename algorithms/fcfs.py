def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x["arrival"])
    completion_time = 0
    result = []
    
    for process in processes:
        start_time = max(completion_time, process["arrival"])
        completion_time = start_time + process["burst"]
        result.append({
            "Process": process["name"],
            "Start": start_time,
            "Completion": completion_time,
            "Turnaround": completion_time - process["arrival"],
            "Waiting": start_time - process["arrival"]
        })
    
    return result
