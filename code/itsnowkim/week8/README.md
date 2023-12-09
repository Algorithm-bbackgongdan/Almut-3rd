# 디스크 컨트롤러 - prog_42627

```python
import math

# FIFO -> SJF 로 하라는 뜻
def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[1], x[0]))
    N = len(jobs)
    curr = 0

    for j in jobs:
        arrived, consume = j

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

    return math.floor(answer/len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
```

Shortest Job First 로 풀면 된다고 생각하고 정렬해서 풀었는데, 알고리즘에 오류가 있었다.
처음부터 전체 job 에 대해 scheduling 을 하면 안되고,
current time 에 따라서 scheduling 을 해 주는게 맞지 않나.. 싶다.

그래서 다음과 같이 수정했다.
```python
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

    temp.sort(key=lambda x: (x[1]))
    
    return temp[0]

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
            tasks.append([next_job[0], next_job[1]])

    return math.floor(answer/N)


print(solution([[0, 3], [1, 9], [2, 6]]))
```

그랬더니 19번 빼고 전체 정답.
19번의 경우 예외 케이스가 있었는데,
아직 남아있는 job 이 있는데, 현재 curr 값에서는 수행할 job 이 없을 경우, (기다려야 하는 경우)
이 때에 대한 예외 처리가 없었다.

이 때의 예외 처리를 위해 다음 가장 빠른 job 이 있는 시간대로 curr를 옮겨야 하기 때문에,
curr 값을 update 하고 retry 하는 방식으로 구현하였다. (실제 스케줄링 알고리즘과 유사하도록)

```python
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
```

결과는 통과.

# 베스트앨범 - prog_42579

그냥 dictionary 로 key value 에 맞게 정렬만 하면 되는 문제.

# 행렬 테두리 회전하기 - prog_77485
푸는 중!
