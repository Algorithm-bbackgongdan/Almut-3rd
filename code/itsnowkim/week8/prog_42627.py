import math
from collections import deque

def schedule(current, jobs):
    # 현 시점에서 shortest job 으로 다시 정렬
    temp = []
    # print("current, jobs", current, jobs)

    for arrived, consume in jobs:
        if arrived > current:
            break
        temp.append([arrived, consume])

    if temp:
        # shortest job first in current time
        temp.sort(key=lambda x: (x[1]))
        return temp[0]
    else: # 현시점 아무런 task 할 건 없지만 아직 job 은 남아있음 - 다음 가장 빠른 job 의 시간 return
        return [-1,jobs[0][0]]

# FIFO -> SJF 로 하라는 뜻
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    N = len(jobs)
    
    tasks = deque([jobs[0]])

    curr = 0
    
    while tasks:
        arrived, consume = tasks.popleft()
        # print("arrived, consume", arrived, consume)

        if curr < arrived:
            curr = arrived + consume
            answer += consume
        elif curr == arrived:
            answer += consume
            curr += consume
        else:
            end = curr + consume
            answer += end-arrived
            curr += consume
        
        jobs.remove([arrived, consume])
        # scheduling
        if jobs:
            next_job = schedule(curr, jobs)
            if next_job[0] == -1:
                # retry
                curr+= next_job[1]-curr
                next_job = schedule(curr, jobs)
            
            tasks.append([next_job[0], next_job[1]])

    return math.floor(answer/N)


# print(solution([[0, 3], [1, 9], [2, 6]]))

print(solution([[1,4],[7,9],[1000,3]]))