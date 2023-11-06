# Week 3

# 16434: 드래곤 앤 던전
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
# Python 풀이
import sys
import math

# constant
TYPE, ATK, HP = 0, 1, 2
MONSTER, POTION = 1, 2

# get input
N, atk = map(int, sys.stdin.readline().rstrip().split())
rooms = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# search if possible (O(N))
def isPossible(max_HP):
    curr_hp, curr_atk = max_HP, atk
    for i in range(N):
        if rooms[i][TYPE] == MONSTER:
            mon_hp, mon_atk = rooms[i][HP], rooms[i][ATK]
            my_atk_count = math.ceil(mon_hp / curr_atk)
            monster_atk_count = math.ceil(curr_hp / mon_atk)
            if my_atk_count <= monster_atk_count:
                # win
                curr_hp -= (my_atk_count - 1) * mon_atk
            else:
                # lose
                return False
        else:
            curr_atk += rooms[i][ATK]
            if rooms[i][HP] + curr_hp > max_HP:
                curr_hp = max_HP
            else:
                curr_hp += rooms[i][HP]
    return True

left, right = 1, int(1e20)
answer = 0
while left <= right:  # binary search (O(logN))
    mid = (left + right) // 2
    if isPossible(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)
```

```java
// Java 풀이
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    int N, atk;
    ArrayList<Room> rooms = new ArrayList<>();

    class Room {
        public Room(long t, long a, long h) {
            this.t = t;
            this.a = a;
            this.h = h;
        }
        long t, a, h;
    }

    private boolean isPossible(long maxHP) {
        long currHP = maxHP, currAtk = atk;
        for(int i = 0 ; i < N ; i++) {
            if (rooms.get(i).t == 1) {
                // monster
                int my_atk_count = (int)(Math.ceil((double) rooms.get(i).h / currAtk));
                int monster_atk_count = (int)(Math.ceil((double) currHP / rooms.get(i).a));
                if (my_atk_count <= monster_atk_count) {
                    // win
                    currHP -= (my_atk_count - 1) * rooms.get(i).a;
                } else {
                    // lose
                    return false;
                }
            } else {
                // potion
                currAtk += rooms.get(i).a;
                if (currHP + rooms.get(i).h > maxHP)
                    currHP = maxHP;
                else
                    currHP += rooms.get(i).h;
            }
        }
        return true;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // for input
        StringBuilder sb = new StringBuilder(); // for output
        StringTokenizer st = new StringTokenizer(br.readLine());

        // get input
        N = Integer.parseInt(st.nextToken());
        atk = Integer.parseInt(st.nextToken());
        for (int i = 0 ; i < N ; i++) {
            st = new StringTokenizer(br.readLine());
            rooms.add(new Room(
                    Long.parseLong(st.nextToken()),
                    Long.parseLong(st.nextToken()),
                    Long.parseLong(st.nextToken())
            ));
        }

        long left = 1, right = Long.MAX_VALUE - 1, mid, answer = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            if (isPossible(mid)) {
                right = mid - 1;
                answer = mid;
            }
            else
                left = mid + 1;
        }
        sb.append(answer);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
```

### ❗️ 결과

성공

### 💡 접근

HmaxHP을 단순히 1부터 증가시키며 시뮬레이션을 하면 O(N^2)이 소요된다. 당연히 O(NlogN) 또는 O(N)의 접근이 필요하다.

임의의 MaxHP가 주어지면, 이 MaxHP로 용을 쓰러트릴 수 있는지 확인하는 데에는 O(N)이 소요됨을 확인했다. N개의 방을 순회하며 매 순회마다 단순한 사칙연산(O(1))으로 전투 시뮬레이션을 진행할 수 있기 때문이다. 

그럼 MaxHP를 O(logN)에 구하기 위해 이분 탐색을 적용해야 한다. 따라서 left, right 값을 나누어 이분탐색으로 MaxHP를 탐색하고, MaxHP에 대해 O(N)으로 시뮬레이션 했다.

## 🥳 문제 회고

처음에 분명 맞게 풀었는데 제출하니 계속 틀렸다. 그 이유는 right의 범위 때문이었다. 처음엔 1,000,000 * 1,000,000 의 값으로 설정했는데, 이보다 더 큰 HP가 필요한 경우가 존재했다.

파이썬으로 풀면 타입이 없어 수의 범위를 신경쓰지 않아도 되는데, c++이나 Java로 풀이할 경우 타입 신경을 잘 써야한다. Java의 경우 Int는 대략 21억 이므로, 무조건 long 을 써야한다. 참고로 long의 최대값은 9,223,372,036,854,775,807 이라고 한다. 물론 이 수를 외워서 상수로 사용하기보다는  `Long.MAX_VALUE` 을 사용하면 편하다.

# 1149: RGB거리
- 출처 : 백준
## 😎 Solved Code

### 💻 Code

```python
# 백준 1149 : RGB거리
# Python 풀이
import sys

R, G, B = 0, 1, 2

N = int(sys.stdin.readline().rstrip())
costs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

DP = [[0] * 3 for _ in range(N)]
DP[0][R] = costs[0][R]
DP[0][G] = costs[0][G]
DP[0][B] = costs[0][B]

for i in range(1, N):
    DP[i][R] = min(DP[i - 1][G], DP[i - 1][B]) + costs[i][R]
    DP[i][G] = min(DP[i - 1][R], DP[i - 1][B]) + costs[i][G]
    DP[i][B] = min(DP[i - 1][R], DP[i - 1][G]) + costs[i][B]

print(min(DP[-1]))
```

```cpp
// 백준 1149 : RGB거리
// C++ 풀이
#include <iostream>
#include <cstdio>
#define R 0
#define G 1
#define B 2
#define MAX 1000
using namespace std;

int main(int argc, char **argv) {
  int N;
  int costs[MAX][3];
  int dp[MAX][3];
  cin >> N;
  for (int i = 0 ; i < N ; i++)
    cin >> costs[i][R] >> costs[i][G] >> costs[i][B];
  dp[0][R] = costs[0][R];
  dp[0][G] = costs[0][G];
  dp[0][B] = costs[0][B];

  for (int i = 1 ; i < N ; i++) {
    dp[i][R] = costs[i][R] + min(dp[i-1][G], dp[i-1][B]);
    dp[i][G] = costs[i][G] + min(dp[i-1][R], dp[i-1][B]);
    dp[i][B] = costs[i][B] + min(dp[i-1][R], dp[i-1][G]);
  }

  cout << min(dp[N-1][R], min(dp[N-1][G], dp[N-1][B])) << endl;
  return 0;
}
```

```java
// 백준 1149 : RGB거리
// Java 풀이
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    int N;
    ArrayList<House> house = new ArrayList<>();

    class House {
        int R,G,B;
        House (int R, int G, int B) {
            this.R = R;
            this.G = G;
            this.B = B;
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // for read
        StringBuilder sb = new StringBuilder(); // for output

        /* get input */
        N = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < N ; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            house.add(new House(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }

        /* initialize */
        House dp[] = new House[N];
        for (int i = 0 ; i < N ; i++)
            dp[i] = new House(0, 0, 0);
        dp[0].R = house.get(0).R;
        dp[0].G = house.get(0).G;
        dp[0].B = house.get(0).B;

        /* dp */
        for (int i = 1 ; i < N ; i++) {
            dp[i].R = house.get(i).R + Math.min(dp[i-1].G, dp[i-1].B);
            dp[i].G = house.get(i).G + Math.min(dp[i-1].R, dp[i-1].B);
            dp[i].B = house.get(i).B + Math.min(dp[i-1].R, dp[i-1].G);
        }

        sb.append(Math.min(dp[N-1].R, Math.min(dp[N-1].G, dp[N-1].B)));
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
```

### ❗️ 결과

성공

### 💡 접근

DP로 간단히 접근할 수 있다. i번째 집을 R,G,B 세가지로 칠할 각각의 경우는, i-1번째 집을 R,G,B로 칠한 경우의 최소 비용 값을 살펴보면 쉽게 구할 수 있다. 예를 들어 i번째 집을 R로 칠하는 최소 비용은, i-1번째 집이 G 또는 B로 칠한 경우중 최소 비용을 선택해 구할 수 있다. 

## 🥳 문제 회고

처음에는 그리디로 풀려다가 논리가 맞지 않다 느꼈고, 반례를 찾았다. i, i+1 사이의 관계를 살펴보니 DP로 쉽게 풀 수 있겠다는 생각이 들었다.

# 64062: 징검다리 건너기
## 😎 Solved Code

### 💻 Code

```python
# Python 풀이
def canPass(num, stones, k):
    count = 0
    for i in range(len(stones)):
        if stones[i] < num:
            count += 1
        else:
            count = 0
        if count == k:
            return False
    return True

def solution(stones, k):
    answer = 0
    right, left = max(stones), min(stones)
    while left <= right:
        mid = (left + right) // 2
        if canPass(mid, stones, k):
            answer = max(answer, mid) 
            left = mid + 1
        else:
            right = mid - 1
    return answer
```

```java
// Java 풀이
class Solution {
    private boolean isPossible(int n, int[] stones, int k) {
        int count = 0;
        for(int i = 0 ; i < stones.length ; i++) {
            if (stones[i] < n){
                if (++count == k) return false;
            }
            else count = 0;
        }
        return true;
    }
    
    public int solution(int[] stones, int k) {
        int answer = 0;
        int left = 1, right = 200000000, mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (isPossible(mid, stones, k)) {
                left = mid + 1;
                answer = mid;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }
}
```

### ❗️ 결과

성공

### 💡 접근

stones 범위가 200,000,000 인 것을 보니 대놓고 이분탐색으로 풀어달라는 문제였다. 건널 수 있는 애들의 수(n)를 이분탐색값으로 설정하고 문제를 풀고자 했다. 임의의 n이 주어졌을 때, n명 모두 건널 수 있는지 없는지 판별하는 함수를 만들면 된다. 이 함수는 O(N)의 시간복잡도를 가져야 한다.

stones를 순회하며 n보다 작은 stone이 등장하면 count++ 를 해준다. 그렇지 않으면 count = 0 으로 초기화 한다. 즉, n명이 모두 건널 수 없는 연속된 돌의 개수를 세는 것이다. 돌의 개수가 마지노선인 k와 같아지는 순간 n명 모두 건널 수 없음이 자명하므로 return false 한다.

## 🥳 문제 회고

접근은 맞았는데 처음에 isPossible 함수를 조금 복잡하게 짰더니 효율성 테스트 일부가 fail이었다. 조금 더 간단한 로직으로 바꾸니 통과했다. 배열에 access하는 것 같은 instruction 몇 개만 없앴을 뿐인데 성공한 것을 보면, 효율성 테스트가 존재하는 문제는 로직을 최대한 간단하게 짜야할 것 같다.