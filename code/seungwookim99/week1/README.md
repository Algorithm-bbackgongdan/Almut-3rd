# Week 1

# 21758: 꿀 따기 
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```python
# Python 풀이
import sys

N = int(sys.stdin.readline().rstrip())
place = list(map(int, sys.stdin.readline().rstrip().split()))

cumulativeSumFromLeft = [0] * N
cumulativeSumFromLeft[0] = place[0]
for i in range(1, N):
  cumulativeSumFromLeft[i] = cumulativeSumFromLeft[i-1] + place[i]
  
cumulativeSumFromRight = [0] * N
cumulativeSumFromRight[N-1] = place[N-1]
for i in range(N-2, -1, -1):
  cumulativeSumFromRight[i] = cumulativeSumFromRight[i+1] + place[i]

maxVal = 0
# 벌통이 맨 왼쪽일 경우
for i in range(1, N-1):
  maxVal = max(maxVal, cumulativeSumFromLeft[i] + cumulativeSumFromLeft[N-1] - place[N-1] - 2*place[i])

# 벌통이 맨 오른쪽일 경우
for i in range(1, N-1):
  maxVal = max(maxVal, cumulativeSumFromRight[i] + cumulativeSumFromRight[0] - place[0] - 2*place[i])

# 벌통이 중간일 경우
for i in range(1,N-1):
  maxVal = max(maxVal, cumulativeSumFromLeft[i] + cumulativeSumFromRight[i] - place[0] - place[N-1])
print(maxVal)
```

```cpp
// C++ 풀이
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
  int N;
  cin >> N;
  int place[N];
  for (int i = 0; i < N; i++)
    cin >> place[i];

  int maxVal = 0;
  int cumulativeSumFromLeft[N];
  cumulativeSumFromLeft[0] = place[0];
  for (int i = 1; i < N; i++)
    cumulativeSumFromLeft[i] = place[i] + cumulativeSumFromLeft[i - 1]; // 누적합 계산
  int cumulativeSumFromRight[N];
  cumulativeSumFromRight[N - 1] = place[N - 1];
  for (int i = N - 2; i >= 0; i--)
    cumulativeSumFromRight[i] = place[i] + cumulativeSumFromRight[i + 1]; // 누적합 계산

  // 맨 왼쪽(0번째 인덱스)이 벌통
  for (int i = 1; i < N - 1; i++)
    maxVal = max(maxVal, cumulativeSumFromLeft[N - 1] + cumulativeSumFromLeft[i] - 2 * place[i] - place[N - 1]);

  // 맨 오른쪽(마지막 인덱스)이 벌통
  for (int i = N - 2; i > 0; i--)
    maxVal = max(maxVal, cumulativeSumFromRight[0] + cumulativeSumFromRight[i] - 2 * place[i] - place[0]);

  // 중간 인덱스가 벌통
  for (int i = 1; i < N - 1; i++)
    maxVal = max(maxVal, cumulativeSumFromLeft[i] + cumulativeSumFromRight[i] - place[0] - place[N - 1]);
  cout << maxVal << endl;
  return 0;
}
```

### ❗️ 결과

성공

### 💡 접근

두 벌과 벌통의 위치가 가변적이기 때문에 어느 하나라도 고정을 시켜야 한다. 최대한 많은 꿀을 모으려면 벌과 벌통이 멀리 떨어져 있어야 한다. 따라서 벌통이나 벌이 배열상에 가장 왼쪽이나 오른쪽에 위치할 것이다.

벌통을 기준으로 생각해보면 벌통이 맨 왼쪽, 오른쪽, 중간 어딘가에 위치할 경우 3가지가 있다.

벌통이 맨 왼쪽일 경우, 벌 한마리는 맨 오른쪽에 있어야 최대한 많은 벌을 딴다. 따라서 남은 벌 한마리의 위치만 순회로 결정하면 된다.

벌통이 맨 오른쪽일 경우, 같은 논리로 벌 한마리는 맨 왼쪽에 있어야 한다. 그리고 남은 벌 한마리의 위치는 순회로 결정하면 된다.

벌통이 중앙 어딘가에 있을 경우는, 두마리의 벌이 각자 왼쪽, 오른쪽 끝에 위치하면 된다. 그럼 벌통의 위치는 양 끝 인덱스는 제외하고 순회하여 결정할 수 있다.

N이 100,000이기 때문에 O(N제곱) 이라면 시간초과가 나올 것이다. 따라서 O(N)에 해결할 방법이 필요하다. 위에서 분류한 세 가지 케이스마다 한 마리의 벌이나 벌통의 위치를 바꿔가며 순회한다. 매 순회는 O(N)이 소요된다. 따라서 매 순회마다 해당 상황에서 모은 꿀의 양이 얼마인지 O(1)에 구해야한다. 

그러기 위해서 누적합을 떠올렸다. `cumulativeSumFromLeft` 와 `cumulativeSumFromRight` 라는 배열을 만들어, 각자 인덱스 오름차순, 내림차순 방향으로 누적합들을 구했다. 누적합을 구하는 과정은 O(N)에 가능하다.

## 🥳 문제 회고

두 벌의 위치와 벌통의 위치가 가변적이라 많이 고민했다. 그러다 극단적인 위치(맨 왼쪽 또는 오른쪽)에서 답이 나올 것이라는 느낌이 들었다. 그래서 일부 변수들을 고정하고 문제를 바라보니 풀이가 떠올랐다. 또 이번 문제는 벌통의 위치를 세가지 경우로 분류하는 과정이 필수적인 것 같은데, 상황에 따라 문제를 작게 나눠 푸는 습관을 들여야겠다.

# 2174: 로봇 시뮬레이션
- 출처 : 백준

## 😎 Solved Code

### 💻 Code

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

struct Bot
{
  int x, y, dir;
};

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int A, B, N, M;
Bot bot[101];

bool out_of_range_(int y, int x)
{
  return (y < 0) || (y >= B) || (x < 0) || (x >= A);
}

int crash_into_robot(int y, int x)
{
  for (int i = 1; i <= N; i++)
  {
    if ((bot[i].y == y) && (bot[i].x == x))
      return i;
  }
  return -1;
}

int main(void)
{
  cin >> A >> B >> N >> M;
  for (int i = 1; i <= N; i++)
  {
    int rx, ry;
    char rdir;
    cin >> rx >> ry >> rdir;
    bot[i].x = rx - 1;
    bot[i].y = ry - 1;
    bot[i].dir = (rdir == 'S' ? 0 : (rdir == 'E' ? 1 : (rdir == 'N' ? 2 : 3)));
  }
  for (int i = 0; i < M; i++)
  {
    int idx, repeat;
    char cmd;
    cin >> idx >> cmd >> repeat;
    for (int j = 0; j < repeat; j++)
    {
      switch (cmd)
      {
      case 'L':
        bot[idx].dir = (bot[idx].dir + 1) % 4;
        break;
      case 'R':
        bot[idx].dir = (bot[idx].dir == 0 ? 3 : bot[idx].dir - 1);
        break;
      case 'F':
        int dir = bot[idx].dir;
        int ny = bot[idx].y + dy[dir], nx = bot[idx].x + dx[dir];
        int crashed;
        if (out_of_range_(ny, nx))
        {
          cout << "Robot " << idx << " crashes into the wall" << endl;
          return 0;
        }
        else if ((crashed = crash_into_robot(ny, nx)) > 0)
        {
          cout << "Robot " << idx << " crashes into robot " << crashed << endl;
          return 0;
        }
        bot[idx].y = ny;
        bot[idx].x = nx;
        break;
      }
    }
  }
  cout << "OK" << endl;
  return 0;
}
```

### ❗️ 결과

성공

### 💡 접근

흔히 접하는 시뮬레이션 문제라서 시키는 대로 진행했다. 다만 평소 내가 푸는 좌표계와 문제에서 주어진 좌표계가 달라 문제 상황을 일부 변형했다.

위에서 아래 방향으로 y가 증가하고, 왼쪽에서 오른쪽으로 x가 증가하게끔 좌표계를 변형했다.

수학으로 치면 동서남북 방향을 x축 대칭이동 시켰다.

로봇 구조체를 만들어 좌표와 방향을 저장했다. 이후 명령어를 반복 수행하면서 L,R이 나오면 이에 맞게 로봇의 방향을 업데이트 했다. 그리고 F 명령어가 나오면 `out_of_range_` 함수로 벽에 박는지, `crash_into_robot` 함수로 로봇에 박는지 검사한다. `crash_into_robot` 함수는  robot 구조체 배열을 순회하며 모든 로봇의 현 위치 좌표와 비교한다.

## 🥳 문제 회고

처음에 좌표계 때문에 틀렸다. 문제를 꼼꼼하게 읽고 구현하고 테스트를 해야겠다.