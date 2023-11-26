# WEEK 5

## PROGRAMMERS 118668

### Code

```javascript
function solution(alp, cop, problems) {
    var answer = 0;
    let [maxAlp, maxCop] = [0, 0];

    problems.forEach(([alp_req, cop_req]) => {
        maxAlp = Math.max(maxAlp, alp_req);
        maxCop = Math.max(maxCop, cop_req);
    });

    const dp = new Array(maxAlp + 1)
        .fill()
        .map(() => new Array(maxCop + 1).fill(Number.MAX_SAFE_INTEGER));

    alp = Math.min(alp, maxAlp);
    cop = Math.min(cop, maxCop);

    dp[alp][cop] = 0;

    for (let i = alp; i <= maxAlp; i++) {
        for (let j = cop; j <= maxCop; j++) {
            // 알고리즘 공부
            if (i + 1 <= maxAlp) {
                dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + 1);
            }
            // 코딩 공부
            if (j + 1 <= maxCop) {
                dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + 1);
            }
            // 문제 풀기
            problems.forEach(([alp_req, cop_req, alp_rwd, cop_rwd, cost]) => {
                if (i >= alp_req && j >= cop_req) {
                    const nextAlp = Math.min(i + alp_rwd, maxAlp);
                    const nextCop = Math.min(j + cop_rwd, maxCop);

                    dp[nextAlp][nextCop] = Math.min(
                        dp[nextAlp][nextCop],
                        dp[i][j] + cost
                    );
                }
            });
        }
    }

    answer = dp[maxAlp][maxCop];

    return answer;
}
```

### Approach

1. `dp[i][j]`를 알고력 `i`, 코딩력 `j`를 얻는데 필요한 시간이라고 정의한다.
2.  필요한 최대 알고력, 최대 코딩력을 구한다.
3.  현재 알고력, 코딩력부터 시작해서
-  알고리즘을 공부하거나
-  코딩을 공부하거나
-  풀 수 있는 모든 문제를 푼다.
4. 이때, 이미 기존 알고력, 코딩력이 필요한 알고력, 코딩력보다 높은 경우에는 예외 처리를 해준다.
   
### TIL
- DP로 풀어야 할 거 같다고 생각했는데, `dp[i]`를 시간 i에서 얻을 수 있는 최대 알고력, 코딩력이라고 정의해서 헤맸다.
- 애초에 알고력, 코딩력의 대소 비교가 어렵다. `(11, 11)`, `(10, 12)` 요런 경우는 어떤 게 좋은 건지 비교 불가..
- 그래서 DP를 새로 정의해야한다고 생각했는데 아이디어를 떠올리지 못하고 결국엔 풀이를 봤다. 이렇게 하나 배워간다.


## PROGRAMMERS 118666

### Code

```javascript
const MID_VALUE = 4;

function solution(survey, choices) {
    var answer = '';
    const scores = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    
    survey.forEach((s, i)=>{
        const choice = choices[i];
        const [disagree, agree] = s;
        
        if(choice === MID_VALUE){
            return;
        }
        
        if(choice < MID_VALUE){
            scores[disagree] += MID_VALUE - choice;
        }else{
            scores[agree] += choice - MID_VALUE;
        }
    });
    
    answer += scores.R >= scores.T ? 'R' : 'T';
    answer += scores.C >= scores.F ? 'C' : 'F';
    answer += scores.J >= scores.M ? 'J' : 'M';
    answer += scores.A >= scores.N ? 'A' : 'N';
    
    return answer;
}
```

### Approach
1. 선택지를 하나씩 돌면서 '모르겠다' 면 패스
2. '비동의'면 `'모르겠다 값' - '선택지 값'` 을 더한다.
3. '동의'면 `'선택지 값' - '모르겠다 값'` 을 더한다.

### TIL
- 주어진 대로 잘 풀면 됐다.
- 실제 코테였다면, 풀었는지 여부보다는 코드 스타일을 중요하게 봤을 것 같다.
- 더 깔끔한 방법은 생각해봐야겠다.

## PROG 118669

### Code

```python
from heapq import heappush, heappop
from collections import defaultdict

def dijkstra(gates, graph, isSummit,isGate, n):
    distances = [float("inf") for _ in range(n + 1)] # distances[i]: 출발지에 상관 없이 i 로 가는 최소 intensity
    heap = []

    for gate in gates:
        distances[gate] = 0
        heap.append([0, gate])

    while heap:
        dist, cur = heappop(heap);

        # 이미 intensity가 최소이면 볼 필요가 없음
        # 정상 이후에는 intensity를 따지지 않아도 됨
        if dist > distances[cur] or isSummit[cur]:
            continue

        for adjacent, cost in graph[cur]:
            if isGate[adjacent]: continue # 출입구에 대해서는 intensity를 구할 필요 없음

            curPathCost = max(distances[cur], cost)
            if curPathCost < distances[adjacent]:
                distances[adjacent] = curPathCost
                heappush(heap, [curPathCost, adjacent])

    return distances

def solution(n, paths, gates, summits):
    answer = [-1, float("inf")]
    graph = defaultdict(list)
    isSummit = [False for _ in range(n + 1)]
    isGate = [False for _ in range(n + 1)]


    for summit in summits:
        isSummit[summit] = True;
    for gate in gates:
        isGate[gate] = True;

    for i, j, w in paths:
        graph[i].append([j, w]);
        graph[j].append([i, w])

    distances = dijkstra(gates, graph, isSummit, isGate, n)

    for summit in sorted(summits):
        if distances[summit] < answer[1]:
            answer = [summit, distances[summit]]

    return answer
```

### Approach
1. `n = 50,000` 이므로 이중 루프를 돌려선 안된다. 최대한 `nlogn`에서 끝내자.
2. 구해야할 것은 `min(입구 ~ 정상 경로에서 최대 intensity)`
3. min heap을 사용하는 다익스트라로 구하자.
4. max(max(현재 점까지 오는데 최대 intensity, 현재 점 ~ 이웃점 cost), distances[이웃 점])) 연산으로 다익스트라를 돌린다.
5. 구해야할 것은 입구에 상관없는 최대 intensity이므로 처음에 minheap에 입구를 다 넣고 시작한다.

### TIL
- 다익스트라까지는 생각했는데, 모든 입구마다 다익스트라를 돌려서 일부 문제에서 시간 초과가 났다.
- 결국에는 풀이를 봤는데, 처음에 minHeap에 모든 입구를 다 넣고 다익스트라를 한 번만 돌리더라.
- 생각해보면 구해야할 것은 입구에 상관 없이 최소 intensity이므로 그냥 모든 입구를 다 넣고 시작해도 됐다. (사실 아직도 이해가 잘 되지 않는다.. 이렇게 하면 연산이 다 섞이는 거 아닌가 ㅠ)
