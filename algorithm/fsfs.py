def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    time = 0
    completed = []
    for process in processes:
        start_time = max(time, process['arrival_time'])
        completion_time = start_time + process['burst_time']
        turnaround_time = completion_time - process['arrival_time']
        waiting_time = turnaround_time - process['burst_time']
        completed.append({
            'process_id': process['process_id'],
            'arrival_time': process['arrival_time'],
            'burst_time': process['burst_time'],
            'start_time': start_time,
            'completion_time': completion_time,
            'turnaround_time': turnaround_time,
            'waiting_time': waiting_time
        })
        time = completion_time
    return completed