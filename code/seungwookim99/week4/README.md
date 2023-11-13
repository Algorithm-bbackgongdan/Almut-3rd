# Week 4

# 14938: 서강그라운드
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```cpp
#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

long INF = 2000000000;
int n, m, r;
int items[101];

int main(void) {
  long d[101][101];
  for(int i = 1; i <= 100; i++) {
    for(int j = 1; j <= 100; j++) {
      d[i][j] = d[j][i] = INF;
    }
    d[i][i] = 0;
  }
  
  cin >> n >> m >> r;
  for(int i = 1; i <= n; i++)
    cin >> items[i];
  for(int i = 0; i < r; i++) {
    int a,b,l;
    cin >> a >> b >> l;
    d[a][b] = d[b][a] = l;
  }

  //floyd-warshall
  for(int k = 1; k <= n; k++) {
    for(int i = 1; i <= n; i++) {
      for(int j = 1; j <= n; j++) {
        if (d[i][j] > d[i][k] + d[k][j]) d[i][j] = d[i][k] + d[k][j];
      }
    }
  }

  int res = 0;
  for(int i = 1; i <= n; i++) {
    int cnt = 0;
    for(int j = 1; j <= n; j++) {
      if(d[i][j] <= m) {
        cnt += items[j];
      }
    }
    res = max(res, cnt);
  }
  cout << res << endl;
}
```

### ❗️ 결과

성공

### 💡 접근

시작점(낙하산 떨어질 지역)이 어디일지 모른다. 따라서 모든 노드에 대해 다른 노드로의 모든 거리를 구해야한다. n=100 이므로 O(N^3)인 floyd-warshall을 사용해도 될 듯 하다.

floyd-warshall로 모든 거리를 구한 뒤, 시작 노드를 순회하며 최대로 얻을 수 있는 아이템들을 구한다. 그 중 최대값을 찾으면 된다.

## 🥳 문제 회고

k-i-j 순서대로 3중 loop를 구성해야 하는데, 실수로 i-j-k 순서대로 loop를 돌려서 엄청 헤맸다. floyd-warshall 알고리즘에서 거쳐가는 노드(k)는 항상 가장 outer loop에서 돌려야 하는걸 잊지 말자!!


# 1504: 특정한 최단 경로
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

long INF = 1000000000;

int N, E, u, v;
long d[801];
vector<pair<int,long> > edges[801];

void dijkstra(int start) {
  for(int i = 0; i < 801; i++)
    d[i] = INF;
  d[start] = 0;
  priority_queue<pair<long, int> > pq;
  pq.push(make_pair(0, start));
  while(!pq.empty()) {
    int curr = pq.top().second;
    long distance = -pq.top().first;
    pq.pop();
    if(d[curr] < distance) continue;
    for(int i = 0; i < edges[curr].size(); i++) {
      int next = edges[curr][i].first;
      long newDistance = distance + edges[curr][i].second;
      if (newDistance < d[next]) {
        d[next] = newDistance;
        pq.push(make_pair(-newDistance, next));
      }
    }
  }
}

int main(void) {
  cin >> N >> E;
  for(int i = 0; i < E; i++) {
    int a,b;
    long c;
    cin >> a >> b >> c;
    edges[a].push_back(make_pair(b,c));
    edges[b].push_back(make_pair(a,c));
  }
  cin >> u >> v;
  // from 1
  dijkstra(1);
  long oneToU = d[u], oneToV = d[v];

  // from u
  dijkstra(u);
  long uToV = d[v], uToN = d[N];

  // from v
  dijkstra(v);
  long vToU = d[u], vToN = d[N];

  long res = min(oneToU + uToV + vToN, oneToV + vToU + uToN);
  if (res >= INF) res = -1;
  cout << res << endl;
  return 0;
}
```

### ❗️ 결과

성공

### 💡 접근

최단거리를 구하는 문제이므로 floyd-warshall, dijkstra 알고리즘을 떠올릴 수 있다. floyd-warshall은 O(N^3)이므로 800^3 은 대략 5억이 넘어가는 연산이라 사용할 수 없다. 따라서 O(NlogE)인 dijkstra 알고리즘으로 문제를 풀고자 했다.

1에서 N까지 가는 경로중 u,v를 반드시 거쳐야 한다. 따라서

1→u→v→N과 1→v→u→N 중 최솟값을 구하면 된다.

그러므로 dijkstra를 1,u,v가 start인 총 3가지 경우로 3번 돌려 값을 구했다.

## 🥳 문제 회고

Dijkstra 알고리즘 구현 자체가 어려운데 실수없이 잘 구현하는 연습을 하자.

# 92344: 파괴되지 않은 건물
- 출처 : 프로그래머스
## 😎 Solved Code

### 💻 Code

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

int res[1001][1001];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    memset(res, 0, sizeof(int)*1001*1001);
    //누적합 표시
    for(vector<int> s: skill) {
        int type = s[0], r1 = s[1], c1 = s[2], r2 = s[3], c2 = s[4], deg = s[5];
        deg *= (type == 1) ? -1 : 1;
        res[r1][c1] += deg;
        res[r1][c2+1] -= deg;
        res[r2+1][c1] -= deg;
        res[r2+1][c2+1] += deg;
    }
    //누적합 계산
    for(int i = 0; i < board.size(); i++) {
        for(int j = 1; j < board[0].size(); j++) {
            res[i][j] += res[i][j-1];
        }
    }
    
    for(int j = 0; j < board[0].size(); j++) {
        for(int i = 1; i < board.size(); i++) {
            res[i][j] += res[i-1][j];
        }
    }
    //파괴되지 않은 건물 계산
    for(int i = 0; i < board.size(); i++) {
        for(int j = 0; j < board[0].size(); j++) {
            if (res[i][j] + board[i][j] > 0) answer++;
        }
    }
    return answer;
}
```

### ❗️ 결과

성공

### 💡 접근

단순히 (r1,c1)에서 (r2,c2)까지 값을 갱신하면 O(N^2)의 시간복잡도다. skill의 길이가 250,000 이므로 최대 1,000 * 1,000 * 250,000 번의 연산이 필요하다. 이렇게 하면 효율성 검사를 통과할 수 없다.

누적합 알고리즘을 이용해 O(N)에 문제를 해결할 수 있다.

(0,0)에서 (3,3)까지 3, (1,0), (2,2)까지 2의 내구도를 올린다면 아래와 같이 나타낼 수 있다.

| 3 | 0 | 0 | 0 | -3 |
| --- | --- | --- | --- | --- |
| 2 | 0 | 0 | -2 | 0 |
| 0 | 0 | 0 | 0 | 0 |
| -2 | 0 | 0 | 2 | 0 |
| -3 | 0 | 0 | 0 | 3 |

즉, (r1,c1) = degree, (r1,c2+1) = -degree, (r2+1,c1) = -degree, (r2+1,c2+1) = degree 의 값을 넣어준다.

이후 좌에서 우 방향으로 모든 row를 누적합 하고, 상에서 하 방향으로 모든 col을 누적합 하면 O(N+M)의 시간복잡도가 소요되며 아래와 같은 결과가 나온다.

| 3 | 3 | 3 | 3 | 0 |
| --- | --- | --- | --- | --- |
| 5 | 5 | 5 | 3 | 0 |
| 5 | 5 | 5 | 3 | 0 |
| 3 | 3 | 3 | 3 | 0 |
| 0 | 0 | 0 | 0 | 0 |

우리가 의도한 대로 결과가 나오는 것을 확인할 수 있다. 따라서, 값을 업데이트할 시작 좌표와 끝 좌표를 이용해 차곡차곡 기록해뒀다, 마지막에 O(NM)의 시간복잡도로 누적합 계산을 하면 아주 빠르게 연산을 할 수 있다.

## 🥳 문제 회고

예전에 풀어본 문제였다. 당시에 누적합 알고리즘을 처음 접하고 인상적이어서 기억하고 있었다. 카카오 기출에도 몇 번 등장한 알고리즘이라 잘 익혀두자.