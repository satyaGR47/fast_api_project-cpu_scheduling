def sjf_non_preemptive(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))
    time = 0
    completed = []
    while processes:
        available = [p for p in processes if p['arrival_time'] <= time]
        if available:
            current = min(available, key=lambda x: x['burst_time'])
            processes.remove(current)
            start_time = time
            completion_time = start_time + current['burst_time']
            turnaround_time = completion_time - current['arrival_time']
            waiting_time = turnaround_time - current['burst_time']
            completed.append({
                'process_id': current['process_id'],
                'arrival_time': current['arrival_time'],
                'burst_time': current['burst_time'],
                'start_time': start_time,
                'completion_time': completion_time,
                'turnaround_time': turnaround_time,
                'waiting_time': waiting_time
            })
            time = completion_time
        else:
            time += 1
    return completed