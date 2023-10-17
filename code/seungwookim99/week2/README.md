# Week 2

# 2573: 빙산
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```cpp
// C++ 풀이
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

#define MAX 301

using namespace std;

int dy[4] = {0,1,0,-1};
int dx[4] = {1,0,-1,0};

int N, M;
int board[MAX][MAX];
int year = 0;

struct Point {
  int y, x, num;
};

bool out_of_range_(int y, int x) {
  return (0 > y) || (0 > x) || (N <= y) || (M <= x);
}

void bfs(int y, int x, int glacier[MAX][MAX], int num) {
  queue<Point> q;
  Point start;
  start.y = y, start.x = x;
  q.push(start);
  while (!q.empty()) {
    Point curr = q.front();
    q.pop();
    for (int i = 0 ; i < 4 ; i++) {
      int ny = curr.y + dy[i];
      int nx = curr.x + dx[i];
      if (out_of_range_(ny,nx)) continue;
      if ((board[ny][nx] > 0) && (glacier[ny][nx] == 0)) {
        glacier[ny][nx] = num;
        Point next;
        next.y = ny, next.x = nx;
        q.push(next);
      }
    }
  }
}

int count_glacier() {
  int cnt = 0;
  int glacier[MAX][MAX] = {0,};
  for (int i = 0 ; i < N ; i++) {
    for (int j = 0 ; j < M ; j++) {
      if (board[i][j] == 0) continue; // 바닷물 skip
      if (cnt == 0) bfs(i, j, glacier, ++cnt); // 최초 빙하 덩어리 1로 매핑
      else if (glacier[i][j] == cnt) continue; // 1번 빙하 skip
      else return ++cnt; // 1번이 아닌 다른 빙하 조각 발견
    }
  }
  return cnt;
}

void melt() {
  vector<Point> candidate;
  for (int i = 0 ; i < N ; i++) {
    for (int j = 0 ; j < M ; j++) {
      if (board[i][j] == 0) continue;
      int cnt = 0;
      for (int k = 0 ; k < 4 ; k++) {
        int ny = i + dy[k], nx = j + dx[k];
        if (board[ny][nx] == 0) cnt++;
      }
      if (cnt > 0) {
        Point p;
        p.y = i, p.x = j, p.num = cnt;
        candidate.push_back(p); // 녹을 빙하 좌표, offset 저장
      }
    }
  }
  for (int i = 0 ; i < candidate.size() ; i++) {
    Point p = candidate[i];
    if (board[p.y][p.x] < p.num) board[p.y][p.x] = 0;
    else board[p.y][p.x] -= p.num; // 녹이기
  }
}

int main(void) {
  cin >> N >> M;
  for (int i = 0 ; i < N ; i ++) {
    for (int j = 0 ; j < M ; j++) {
      cin >> board[i][j];
    }
  }
  while(true) {
    /* 빙산 개수 count */
    int cnt = count_glacier();
    if (cnt == 0) {
      year = 0;
      break;
    }
    else if (cnt > 1) break;

    /* 빙산 녹임 */
    melt();
    year++;
  }
  cout << year << endl;
  return 0;
}
```

### ❗️ 결과

성공

### 💡 접근

두 단계로 나눠서 접근한다.

1. 빙산 덩어리 개수 세기
2. 빙산 녹이기

빙산 덩어리 개수 세기는 BFS로 해결할 수 있다. 주어진 board라는 2차원 배열을 (0,0)부터 (N-1,M-1)까지 순회하면서, 0이 아닌 값이 등장하면, glacier라는 2차원 배열에 BFS로 넘버링을 한다. 그럼 빙산 덩어리가 전부 1로 넘버링 된다. 이후 board를 이어서 순회하다가 0이 아니면서, glacier는 0인 위치가 등장하면 두번째 덩어리가 등장한 것이다. 그럼 즉시 빙산 덩어리 개수를 세는 작업을 중단한다.

빙산 녹이기는 board의 모든 요소를 순회하며 실제로 녹을 위치와 얼마나 녹을지 정보를 저장해야 한다. board를 전체 순회하며 0이 아닌 값들은 주변 동서남북을 탐색한다. 그리고 얼마나 녹을지 계산해서 vector에 저장했다. 순회가 끝나면 vector에 들어있는 값들을 순회하며 빙산을 녹이며 board를 업데이트 한다.

## 🥳 문제 회고

여러 서브태스크로 이뤄진 구현 문제였다. C++로 vector, tuple, queue를 처음 사용해서 어색한데 빨리 익혀야겠다.

# 2470: 두 용액
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```cpp
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int N;

int main(void) {
  cin >> N;
  vector<int> plus, minus;
  for (int i = 0 ; i < N ; i++) {
    int tmp;
    cin >> tmp;
    if (tmp > 0) plus.push_back(tmp);
    else minus.push_back(tmp);
  }

  sort(plus.begin(), plus.end());
  sort(minus.rbegin(), minus.rend());

  /* 산성 없음 (음수만)*/
  if (plus.empty()) {
    cout << minus[1] << " " << minus[0] << endl;
    return 0;
  }
  /* 알칼리성 없음 (양수만)*/
  else if (minus.empty()) {
    cout << plus[0] << " " << plus[1] << endl;
    return 0;
  }

  /* 산성, 알칼리성 둘 다 있음 */
  int i = 0, j = 0;
  int answer[2] = {minus[i], plus[j]};
  while ((i < minus.size()) && (j < plus.size())) {
    if (abs(minus[i] + plus[j]) < abs(answer[0] + answer[1])) {
      answer[0] = minus[i], answer[1] = plus[j];
    }
    if (minus[i] + plus[j] > 0) i++;
    else j++;
  }

  if ((plus.size() >= 2) && (plus[0] + plus[1] < abs(answer[0] + answer[1])))
    cout << plus[0] << " " << plus[1] << endl;
  else if ((minus.size() >= 2) && (abs(minus[0] + minus[1]) < abs(answer[0] + answer[1])))
    cout << minus[1] << " " << minus[0] << endl;
  else
    cout << answer[0] << " " << answer[1] << endl;
  return 0;
}
```

### ❗️ 결과

성공

### 💡 접근

세가지로 나눠 풀었다.

1. 산성만 있음
2. 알칼리성만 있음
3. 산성 & 알칼리성 둘 다 있음

먼저 입력을 받을 때, 산성과 알칼리성을 나눠서 저장했다. 그리고 산성(+)은 오름차순 정렬, 알칼리성(-)은 내림차순 정렬했다.

1,2번 둘 다 절대값이 가장 작은 두 값이 답이므로 0,1번 인덱스 값이 답이다.

3번은 조금 복잡한데, 투포인터로 접근했다. 산성과 알칼리성의 배열을 각각 0번째 인덱스부터 투포인터로 순회한다. 

두 값의 합이 양수라면 알칼리성 배열 인덱스를 1 증가시킨다. 반대라면 산성 배열 인덱스를 1 증가시킨다. 이렇게 두 값의 합이 0에 근접할 수 있도록 인덱스를 조정하는 것이다.

매 순회마다 합을 구해 최소값을 구한다.

3번의 경우 예외적으로 두 산성 값의 합 또는 두 알칼리성 값의 합이 더 작을 수 있다. 예를 들어 아래와 같은 경우다.

```cpp
-100 1 2 3 4 5
```

따라서 1,2번 처럼 두 산성 값, 두 알칼리성 값을 구해 지금까지 구한 최솟값과 비교한다.

## 🥳 문제 회고

케이스를 나눠 생각하면 그리디로 해결할 수 있는 문제였다. 우선 시간복잡도를 고려해 산성, 알칼리성 용액을 정렬하는 것이 중요했다.

# 43163: 단어 변환
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```cpp
// C++ 풀이
#include <string>
#include <iostream>
#include <vector>
#define MAX 1000000000

using namespace std;

int answer = MAX;

int different_alphabets_num(string a, string b) {
    int cnt = 0;
    for(int i = 0 ; i < a.length() ; i++) {
        if (a[i] != b[i]) cnt++;
    }
    return cnt;
}

void dfs(int cnt, string begin, string target, vector<string> words, vector<bool> visited) {
    if (begin.compare(target) == 0) {
        answer = min(answer, cnt);
        return;
    }
    for(int i = 0 ; i < visited.size() ; i++) {
        if (visited[i]) continue;
        if (different_alphabets_num(words[i], begin) == 1) {
            visited[i] = true;
            dfs(cnt + 1, words[i], target, words, visited);
            visited[i] = false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    vector<bool> visited(words.size(), false);
    dfs(0, begin, target, words, visited);
    if (answer == MAX) answer = 0;
    return answer;
}
```

### ❗️ 결과

성공

### 💡 접근

완전탐색을 통해 정답을 찾아야한다고 생각했다. 그래서 DFS로 문제를 해결했다.

알파벳 1개를 바꿔 words 값 중 하나로 만드는 과정을 DFS를 1회 호출하는 것이라 생각했다.

따라서 words 값으로 바뀌는 것을 방문이라 생각해 words의 사이즈에 해당하는 visited vector를 생성했다.

그리고 현재 문자열에서 실제 특정 word로 바꿀 수 있는지 확인하기 위해 `different_alphabets_num` 함수를 만들었다. 몇 개의 알파벳이 다른지 알려주는 함수다.

## 🥳 문제 회고

DFS를 이용해 해결할 수 있는 문제였다. DFS는 주로 시뮬레이션 상황이나 그래프가 주어지는데, 조금 다른 상황이 주어져 어떻게 접근할지 고민됐던 문제다.