# prog 118666 : 성격 유형 검사하기
### code
```python
def solution(survey, choices):
    answer = ''
    results = [[0 for _ in range(2)] for _ in range(8)]
               
    for i in range(len(choices)):
        if survey[i] == 'RT':
            if 1 <= choices[i] <= 3:
                results[0][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[0][1] += choices[i] - 4
        elif survey[i] == 'TR':
            if 1 <= choices[i] <= 3:
                results[1][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[1][1] += choices[i] - 4
        elif survey[i] == 'FC':
            if 1 <= choices[i] <= 3:
                results[2][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[2][1] += choices[i] - 4
        elif survey[i] == 'CF':
            if 1 <= choices[i] <= 3:
                results[3][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[3][1] += choices[i] - 4
        elif survey[i] == 'MJ':
            if 1 <= choices[i] <= 3:
                results[4][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[4][1] += choices[i] - 4
        elif survey[i] == 'JM':
            if 1 <= choices[i] <= 3:
                results[5][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[5][1] += choices[i] - 4
        elif survey[i] == 'AN':
            if 1 <= choices[i] <= 3:
                results[6][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[6][1] += choices[i] - 4
        elif survey[i] == 'NA':
            if 1 <= choices[i] <= 3:
                results[7][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[7][1] += choices[i] - 4
    
    answer += 'R' if (results[0][0] + results[1][1] >= results[0][1] + results[1][0]) else 'T'
    answer += 'C' if (results[2][0] + results[3][1] <= results[2][1] + results[3][0]) else 'F'
    answer += 'J' if (results[4][0] + results[5][1] <= results[4][1] + results[5][0]) else 'M'
    answer += 'A' if (results[6][0] + results[7][1] >= results[6][1] + results[7][0]) else 'N'
    
    return answer
  ```
## 결과
### 성공
## 접근
타 언어의 switch-case문처럼 8가지 경우의 수를 조건에 맞게 처리해주고, 결과값을 2차원 리스트에 담아 문제 조건에 맞게 answer에 추가해주었다.
## 문제 회고
위 코드로 문제해결은 가능했지만, 모범답안은 아닐 것이라고 생각하였다. 다른 풀이를 참조하여 딕셔너리 자료구조를 활용하면 보다 효율적인 풀이가 있음을 배울 수 있었다.

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고

# prog_118669 : 등산경로 정하기
### code
```python
import heapq
from math import inf

def solution(n, paths, gates, summits):
    # 간선 정리 (양방향)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    # 산봉우리 판별
    is_summit = [False] * (n + 1)
    for summit in summits:
        is_summit[summit] = True

    # gates 모두 시작 위치
    distance = [inf] * (n + 1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])

    # 다익스트라
    while queue:
        d, i = heapq.heappop(queue)
        # 산봉우리면 바로 continue
        # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
        if distance[i] < d or is_summit[i]:
            continue
        for j, dd in graph[i]:
            dd = max(distance[i], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(queue, [dd, j])

    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result
  ```
## 결과
### 실패 후 참조
## 접근
출입구에서 산봉우리까지의 등산코스를 그대로 돌아오면 되기 때문에 산봉우리까지 편도만 생각하여도 무방.

산봉우리와 출입구를 중복하여 지나지않기 위해 산봉우리 판별과 각각의 출입구를 거리 0으로 초기화하여 queue에 push해준다.

다익스트라로 각 위치에 도달하기 위한 최소 가중치를 업데이트해준다.
## 문제 회고
노드를 출입구, 산봉우리로 구분하여 다익스트라를 구현하는 것이 굉장히 어려웠다. 이 문제처럼 기준값이 경로 내 가중치 합이 아닌 응용된 다익스트라를 풀기 위해서 더 공부해야겠다..
