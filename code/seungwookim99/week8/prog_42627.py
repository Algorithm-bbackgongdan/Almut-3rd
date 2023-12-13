from collections import deque

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    prev_end = 0
    while jobs:
        selected_job = jobs[0]
        min_length = 1001
        for job in jobs:
            if prev_end < job[0]:
                break
            elif min_length > job[1]:
                selected_job = job
                min_length = job[1]
        
        arrived_at, length = selected_job
        if prev_end < arrived_at:
            prev_end = arrived_at + length
            answer += length
        else:
            answer += (prev_end - arrived_at) + length
            prev_end += length
        jobs.remove(selected_job)
    return answer // n