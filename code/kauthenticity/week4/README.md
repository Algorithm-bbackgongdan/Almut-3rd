# WEEK 4

## BOJ 1504

### Code

```javascript
function dijkstra(start, n, graph) {
    const dists = Array(n + 1).fill(MAX_VALUE);
    const visited = new Map();

    for (let node = 1; node <= n; node++) {
        dists[node] = graph[start][node];
    }
    dists[start] = 0;

    visited.set(start, true);

    while (visited.size < n) {
        // 방문하지 않은 제일 가까운 노드 찾기
        let [cur, minDist] = [-1, Number.MAX_SAFE_INTEGER];

        for (let node = 1; node <= n; node++) {
            if (!visited.get(node) && dists[node] < minDist) {
                minDist = dists[node];
                cur = node;
            }
        }

        if (cur === -1) {
            break;
        }
        visited.set(cur, true);

        // 이웃 노드들에 대해서 거리 갱신
        for (let adjacent = 1; adjacent <= n; adjacent++) {
            if (dists[adjacent] > dists[cur] + graph[cur][adjacent]) {
                dists[adjacent] = dists[cur] + graph[cur][adjacent];
            }
        }
    }
    return dists;
}

function solution(n, v1, v2, graph) {
    const startFrom1 = dijkstra(1, n, graph);
    const startFromV1 = dijkstra(v1, n, graph);
    const startFromV2 = dijkstra(v2, n, graph);

    let [path1, path2] = [MAX_VALUE, MAX_VALUE];

    // 1 - v1 - v2 - n
    if (
        startFrom1[v1] !== MAX_VALUE &&
        startFromV1[v2] !== MAX_VALUE &&
        startFromV2[n] !== MAX_VALUE
    ) {
        path1 = startFrom1[v1] + startFromV1[v2] + startFromV2[n];
    }

    // 1 - v2 - v1 - n
    if (
        startFrom1[v2] !== MAX_VALUE &&
        startFromV2[v1] !== MAX_VALUE &&
        startFromV1[n] !== MAX_VALUE
    ) {
        path2 = startFrom1[v2] + startFromV2[v1] + startFromV1[n];
    }

    return Math.min(path1, path2) === MAX_VALUE ? -1 : Math.min(path1, path2);
}
```

### Approach

1. 방법은 1 -> v1 -> v2 -> n, 1 -> v2 -> v1 -> n 밖에 없다.
2. 따라서 각 구간마다 최단 거리를 구하고, 그 합이 최소인 경로를 리턴하면 된다.
3. 최단 거리는 Dijkstra로 찾는다.

### TIL

1. Dijkstra를 구현하는데, 중간에 그래프가 끊길 수 있다는 생각을 못해서 틀렸다. 문제에서 답이 없는 경우를 명시했기 때문에 꼼꼼하게 조건을 읽어야겠다.
2. 처음엔 Bellman Ford가 떠올랐는데, 그럼 5.12 \* 10^8로 시간 초과가 발생해서 생각을 바꿨다. 최단 거리 문제는 데이터 크기를 잘 보고 작으면 BellmanFord, 그 이상이면 Dijkstra로 구현하자.

## BOJ 14938

### Code

```javascript
function solution(n, m, items, graph) {
    let answer = 0;

    for (let k = 1; k < n + 1; k++) {
        for (let i = 1; i < n + 1; i++) {
            for (let j = 1; j < n + 1; j++) {
                if (i === j) {
                    graph[i][j] = 0;
                    continue;
                }
                graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    for (let node = 1; node < n + 1; node++) {
        let itemSum = 0;

        for (let adjacent = 1; adjacent < n + 1; adjacent++) {
            if (graph[node][adjacent] <= m) {
                itemSum += items[adjacent];
            }
        }

        answer = Math.max(answer, itemSum);
    }

    return answer;
}
```

### Approach

1. v=100이므로 v^3 = 10^6으로 벨만포드를 사용해도 된다.
2. 벨만포드로 각 점과 점 사이의 최소 거리를 구한다.
3. 모든 점에 대해 아이템을 주울 수 있는지 확인하고 최대 아이템 개수를 구한다.

### TIL

1. 오랜만에 벨만포드를 구현해서 로직이 헷갈렸다. k, i, j 순서다.

## PROG 92344

### Code

```javascript
function solution(board, skill) {
    var answer = 0;
    const [n, m] = [board.length, board[0].length];
    const tempBoard = Array(n + 1)
        .fill()
        .map(() => Array(m + 1).fill(0));

    skill.forEach(([type, r1, c1, r2, c2, degree]) => {
        tempBoard[r1][c1] += type === 2 ? degree : -degree;
        tempBoard[r1][c2 + 1] += type === 2 ? -degree : degree;

        tempBoard[r2 + 1][c1] += type === 2 ? -degree : degree;
        tempBoard[r2 + 1][c2 + 1] += type === 2 ? degree : -degree;
    });

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m - 1; j++) {
            tempBoard[i][j + 1] += tempBoard[i][j];
        }
    }

    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n - 1; i++) {
            tempBoard[i + 1][j] += tempBoard[i][j];
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            board[i][j] += tempBoard[i][j];

            if (board[i][j] > 0) {
                answer++;
            }
        }
    }
    return answer;
}
```

### Approach

1. 각 skill에 대해, skill을 적용할 row와 column에 degree를 기록해 준다.
2. row 방향으로 skill을 적용해 준다.
3. column 방향으로 skill을 적용해 준다.

### TIL

1. 누적합이지 않을까...? 라는 생각이 들었지만, 정확히 누적합을 어떻게 활용해야 할지 몰라서 검색을 했다.
2. 이렇게 데이터의 구간이 주어지고 더하거나 빼면 누적합임을 생각하자
