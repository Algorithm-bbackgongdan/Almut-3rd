# Week 6

# 118666 : 성격 유형 검사하기
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
def solution(survey, choices):
    ans = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        first, second = survey[i]
        choice = choices[i]
        if choice > 4:
            ans[second] += choice - 4
        elif choice < 4:
            ans[first] += 4 - choice
    answer = ''
    # get result
    answer += 'R' if ans['R'] >= ans['T'] else 'T'
    answer += 'C' if ans['C'] >= ans['F'] else 'F'
    answer += 'J' if ans['J'] >= ans['M'] else 'M'
    answer += 'A' if ans['A'] >= ans['N'] else 'N'
    return answer
```

### ❗️ 결과

성공

### 💡 접근

각 성격 유형을 key값으로 갖는 dictionary를 만들고, survey를 순회하며 점수를 계산한다. 마지막에 1,2,3,4번 지표에 대해 더 큰 값을 찾아 최종 결과를 도출한다.

## 🥳 문제 회고

간단한 구현 문제였다. 문제에서 성격 유형 개수가 8개 밖에 없어서 1,2,3,4번 지표에 대한 유형을 구할 때 하드코딩으로 금방 해결할 수 있었다.

# 118668 : 코딩 테스트 공부
- 출처 : 프로그래머스

## 🥺 Unsolved Code

### 💻 Code

```python
def solution(alp, cop, problems):
    INF = int(1e12)
    answer = INF
    MAX_ALP = max([prob[0] for prob in problems])
    MAX_COP = max([prob[1] for prob in problems])
    
    # init dp matrix (alp x cop)
    dp = [[INF] * 181 for _ in range(181)]
    dp[alp][cop] = 0 # base case
    for i in range(alp, MAX_ALP+1):
        for j in range(cop, MAX_COP+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_rwd: continue
                dp[i+alp_rwd][j+cop_rwd] = min(dp[i][j] + cost, dp[i+alp_rwd][j+cop_rwd])
    return dp[MAX_ALP][MAX_COP]
```

### ❗️ 결과

실패 - 정확도 3개 정답

### 💡 접근

DP를 이용해 문제를 해결하고자 했다.

먼저 주어진 문제중 최대 알고력(MAX_ALP), 최대 코딩력(MAX_COP)를 구한다. 이후 초기 알고력(alp), 코딩력(cop)으로부터 MAX_ALP, MAX_COP까지 도달하기 위해 DP를 활용한다. 2차원 리스트 dp를 이용했으며, row는 알고력, col은 코딩력을 나타낸다. dp[i][j]의 값은 알고력 i, 코딩력 j에 도달하기 위한 최소 비용(시간)을 저장한다.

dp[alp][cop]는 초기값으로 0을 저장한다. 이후 `알고리즘 공부를 하는 경우`(알고력 1 증가), `코딩 공부를 하는 경우`(코딩력 1증가), 그리고 `문제를 푸는 경우`(문제를 풀 수 있는 경우) 3가지 경우에 대해 bottom-top 방식으로 dp 리스트를 채운다.

### 🧐 접근에 대한 회고

접근을 맞게 한 것 같은데 대부분 실패가 뜬다. 어딘가 실수가 있는 것 같은데 원인을 잘 모르겠다…

# 118669 : 등산코스 정하기
- 출처 : 프로그래머스

## 🥺 Unsolved Code

### 💻 Code

```python
from collections import deque
import heapq

def solution(n, paths, gates, summits):
    answer = []
    isGate = [False]*(n+1)
    for gate in gates:
        isGate[gate] = True
    isSummit = [False]*(n+1)
    for summit in summits:
        isSummit[summit] = True
    
    graph = [[] for _ in range(n+1)]
    for a,b,cost in paths:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    
    def bfs(start, n):
        INF = int(1e9)
        q = deque([(start, (1 << start), 0)]) #(curr_node, bitmask_path, min_cost)
        
        candidate = []
        while q:
            curr, path, min_cost = q.popleft()
            for next, cost in graph[curr]:
                if isGate[next] or (path & (1 << next)): continue
                if isSummit[next]:
                    heapq.heappush(candidate, (max(min_cost, cost), next)) #(intensity, summit)
                else:
                    q.append((next, path | (1 << next), max(min_cost, cost)))
        return candidate[0] if candidate else (None, None)
    
    candidate = []
    for gate in gates:
        intensity, summit = bfs(gate, n)
        if intensity:
            heapq.heappush(candidate, (intensity, summit))
        
    return [candidate[0][1], candidate[0][0]]
```

### ❗️ 결과

실패 - (51.6점 / 100점)

### 💡 접근

모든 출입구에 대해 bfs로 최소 intensity로 임의의 산봉우리에 도달할 수 있는 경우를 전부 구한다. 이 때, queue에 push 할 때마다 지나온 경로 정보를 저장하고, 다음으로 이동할 인접 노드가 경로에 존재하면 방문하지 않는다.

경로 정보를 단순히 리스트 형태로 저장하고, 인접 노드가 리스트에 속하는지 탐색하면 O(N)의 시간복잡도가 소요된다. O(1) 시간에 이를 수행하고자 비트마스킹을 사용한다.

만약 path = 0b001010 이라면 1,3번 노드는 이미 방문한 것이다.

### 🧐 접근에 대한 회고

bfs에 딱히 백트래킹을 넣을게 없어서 느낌이 쎄하긴 했다. 답이 나오는 코드인 것 같지만, 여러 테스트 케이스에서 전부 시간 초과가 나왔다.

## 😎 Solved Code

### 💻 Code

```python
import heapq

def solution(n, paths, gates, summits):
    INF = int(1e10)
    answer = []
    graph = [[] for _ in range(n+1)]
    summits.sort()
    for i, j, w in paths:
        graph[i].append((j,w))
        graph[j].append((i,w))
    isGate = [False]*(n+1)
    for i in gates:
        isGate[i] = True
    isSummit = [False]*(n+1)
    for i in summits:
        isSummit[i] = True
    
    def dijkstra(starts, summits):
        q = []
        intensity = [INF] * (n+1)
        for start in starts:
            heapq.heappush(q, (0, start))
            intensity[start] = 0
        while q:
            curr_intensity, curr = heapq.heappop(q)
            if intensity[curr] < curr_intensity: continue
            if isSummit[curr]: continue #산봉우리면 stop
            for next, cost in graph[curr]:
                if isGate[next]: continue
                if intensity[next] > max(curr_intensity, cost):
                    intensity[next] = max(curr_intensity, cost)
                    heapq.heappush(q, (intensity[next], next))
        
        answer = [INF,INF]
        for i in summits:
            if intensity[i] < answer[1]:
                answer[0] = i
                answer[1] = intensity[i]
        return answer
    
    return dijkstra(gates, summits)
```

### ❗️ 결과

성공 - 카카오 해설 참고

### 💡 접근

다익스트라 알고리즘을 변형해서 intensity를 업데이트 해 나간다. 다익스트라는 특정 노드까지 가는 최소 비용을 구하지만, 본 문제에서는 최소의 intensity를 저장한다. 한 gate에서 출발해 임의의 한 산봉우리에 도착하면 탐색을 종료할 수 있다. 그 이유는 gate - 쉼터 - 산봉우리 까지 단방향 경로를 알면, 그 경로를 되돌아 오면 왕복 코스가 완성되기 때문이다.

또한 모든 gate에 대해 각각 다익스트라 알고리즘을 수행하면 시간초과가 발생하기에, 초기 queue에 시작 정점으로 모든 gate를 push하여 문제를 해결할 수 있다.

## 🥳 문제 회고

정말 어려운 문제라고 느껴졌다. 다익스트라 알고리즘을 이렇게까지 변형할 수 있구나 싶은 인상적인 문제였다. 또 모든 gate를 시작 정점으로 push해도 알고리즘이 문제없이 작동하는 것을 깨우칠려면, 다익스트라 알고리즘에 대해 제대로 이해하고 있어야 한다고 느꼈다. 여러모로 배울게 많았고 잘 만든 문제라 다음에 또 풀어봐야겠다.