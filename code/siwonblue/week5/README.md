## Week 5

- 총무 : [itsnowkim](https://github.com/itsnowkim)

### 1. 랜덤 유형 백준

- 문제정보 : 내 집 마련하기 (30619)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/30619

- 선택 정렬로 풀이함
- 시간 복잡도 O(N N M) 2.7 x 10^7
- 선택정렬 + 범위에 들어가지 않는 요소일 경우 제외하는 예외처리만 추가
  ```c++
    vector<int> copy = houses;
    for(int i=0;i<copy.size();i++){
      if(copy[i]>max(L,R) || copy[i]<min(L,R)) continue;
      for(int j=i+1;j<copy.size();j++){
        if(copy[j]>max(L,R) || copy[j]<min(L,R)) continue;
        if(copy[i] > copy[j]) swap(copy[i],copy[j]);
      }
    }
  ```

### 2. 랜덤 유형 백준

- 문제정보 : donstructive (30618)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/30618

- 모르겠어서 고민 중

### 3. 랜덤 유형 백준

- 문제정보 : 보물섬 (2589)
- 출처 : 백준
- 링크 : https://www.acmicpc.net/problem/2589

무난한 BFS

- 접근 방식
  1. visit에 방문 여부와 이동거리 두가지 정보를 담는다. (이때 처음 시작점에 대한 예외처리도 해주자)
  ```c++
    for(int i=0;i<4;i++){
      int nx = x + dx[i];
      int ny = y + dy[i];
      if(nx<0 || ny<0 || nx>=N || ny>=M || char(map[nx][ny]+0)=='W') continue;
      if(visit[nx][ny]) continue;
      if(nx==start_x && ny==start_y) continue;
      cnt = max(visit[x][y]+1,cnt);
      visit[nx][ny] = visit[x][y]+1;
      deque.push(make_pair(nx,ny));
    }
  ```
  2. 시작점에서 이동할 수 있는 곳들에 대해 이전 점에서 +1만큼 처리해주고, 가장 큰 값을 반환하면 된다.
  3. BFS() 를 L에 대해 모두 수행하고 그 중에 가장 큰 값이 정답이다.
  ```c++
      int solution(){
        int ans = -1;
        input();
        for(int i=0;i<N;i++){
          for(int j=0;j<M;j++){
            if(char(map[i][j]+0)=='W') continue;
            // cout << i<<j<<"에서 최대값:"<< BFS(i,j);
            // cout << "\n";
            ans = max(ans, BFS(i,j));
          }
        }
        return ans;
      }
  ```
