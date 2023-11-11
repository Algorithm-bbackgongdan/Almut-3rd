## Week 4

- 총무 : [jonghyeonjo99](https://github.com/jonghyeonjo99)

### 1. 최단경로

- 문제정보 : 서강그라운드 (14938)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/14938

- 접근 방식:

  1. 다익스트라 구현
  2. 수색 범위 내에 있는 모든 값 합쳐서 아이템 개수 파악
  3. 시작점마다 아이템 개수에 대해 최대 값으로 업데이트

- 다익스트라만 잘 알고 있으면 쉽게 풀 수 있으니까 외우자

  ```cpp
  int dijkstra(int v){
    int sum = 0;
    priority_queue<pair<int,int>> pq;
    pq.push(make_pair(0,v));
    for(int i=0;i < dist.size();i++) dist[i]=INF;
    dist[v] = 0;
    while(!pq.empty()){
      int cost = -pq.top().first; // max heap 이어서 - 를 붙이면 min heap이 됨
      int cur = pq.top().second;
      pq.pop();
      for(int i=0;i<maps[cur].size();i++){
        int end = maps[cur][i].first;
        int nCost = maps[cur][i].second;
        if(dist[end] > cost + nCost){
          dist[end] = cost + nCost;
          pq.push(make_pair(-dist[end], end));
        }
      }
    }
    for(int i=1;i<dist.size();i++){
      if(dist[i] <= m) sum += items[i];
    };
    // cout << v << "에서의 수색 값은 :" << sum << "\n";
    return sum;
  }

  ```

- dist를 초기화하려면 직접 아래처럼 해줘야 한다.

  ```cpp
  for(int i=0;i < dist.size();i++) dist[i]=INF;
  ```

### 2. 그래프이론

- 문제정보 : 특정한 최단 경로 (1504)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/1504

- 시간안에 못 풀어서 답 찾아봄.
- 접근 방식

  1. 다익스트라 구현하고 v1, v2, N 까지 가는 각각의 거리를 계산하고 그 중 최소값을 찾으면 됨

- 다익스트라 기본 구현하고 각 포인트별로 따로 실행한 다음에 그 값중 최소를 찾는 아이디어를 생각하지 못했다.

### 3. 프로그래머스

- 문제정보 : 파괴되지 않은 건물 (92344)
- 출처 : 프로그래머스
- 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92344

- 고민 중
