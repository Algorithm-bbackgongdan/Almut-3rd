# 2주차

## 1. 백준\_RGB거리 (1149)

### 💡 Idea

- DP를 활용하여 문제를 해결할 수 있다.
- 각 집을 R, G, B로 칠하는데 필요한 비용을 각각 dp배열에 저장한다.
- 다음 집을 칠할 때, 이전 집과 다른 색을 선택하여 최솟값을 갱신한다.
- 마지막 집까지 도착한 후, 세 가지 색 중 가장 작은 비용을 출력한다.

### 🧑🏻‍💻 Code

```python
import sys

read = sys.stdin.readline

n = int(read())
cost = [list(map(int, read().split())) for _ in range(n)]

R, G, B = 0, 1, 2
dp = [[0] * 3 for _ in range(n)]

dp[0] = cost[0]  # dp 초기값 설정

for level in range(1, n):
    dp[level][R] = min(dp[level - 1][G], dp[level - 1][B]) + cost[level][R]
    dp[level][G] = min(dp[level - 1][B], dp[level - 1][R]) + cost[level][G]
    dp[level][B] = min(dp[level - 1][R], dp[level - 1][G]) + cost[level][B]

print(min(dp[n - 1]))

```

## 2. 백준\_드래곤 앤 던전 (16434)

### 💡 Idea

- 이진 탐색을 사용하여 클리어할 수 있는 최소 HMaxHP를 찾는다.
- 방 정보를 순회하면서 용사의 생명력과 공격력을 갱신하고, 몬스터를 쓰러트리는데 필요한 턴 수를 계산해서 현재 생명력을 계산한다.
- 이진탐색에서 설정된 HMaxHP (mid) 값으로 clear 할 수 있는 여부를 체크하는 can_clear() 함수를 만들어서 클리어 가능하다면 result 를 저장하고 HMaxHP 의 최댓값을 줄인다. 클리어 불가능하다면 HMaxHP 의 최솟값을 늘린다.

### 🧑🏻‍💻 Code

```python
N, A = map(int, input().split())
arr = []
for _ in range(N):
    type, atk, hp = map(int, input().split())
    arr.append((type, atk, hp))


# 던전 클리어 가능 여부를 확인하는 함수
def can_clear(maxHP):
    currentHP = maxHP
    currentATK = A

    for type, atk, hp in arr:
        if type == 1:  # 몬스터가 있는 방
            turns_needed = (hp + currentATK - 1) // currentATK  # 공격으로 몬스터를 쓰러트릴 때 필요한 턴 수 계산
            currentHP -= (turns_needed - 1) * atk  # 생명력 계산
        else:  # 포션이 있는 방
            currentATK += atk
            currentHP = min(maxHP, currentHP + hp)

        if currentHP <= 0:  # 현재 생명력이 0 이하인 경우 클리어 불가능
            return False
    return True


result = 0
start, end = 1, N * int(1e6) * int(1e6)

while start <= end:
    mid = (start + end) // 2

    if can_clear(mid):
        end = mid - 1  # 클리어 가능한 경우, 최소 maxHP를 줄임
        result = mid  # 현재의 mid를 결과로 저장

    else:
        start = mid + 1  # 클리어 불가능한 경우, 최소 maxHP를 늘림

print(result)

```

## 3. 프로그래머스\_징검다리 건너기 (64602)

### 💡 Idea

구해야 하는 것 : 주어진 징검다리 조건에서, 건널 수 있는 최대 사람 수

이진탐색을 사용하는데, 이진탐색 범위의 최댓값은 징검다리에 적힌 숫자의 최댓값이 된다. (건널 수 있는 사람의 최대 맥시멈)

현재의 mid 값 (건너는 사람 수) 과 징검다리에 적힌 숫자를 비교했을 때,

- `징검다리에 적힌 숫자(stone) < mid`` : 해당 징검다리는 0 이 되는 다리임

중요한 것은 연속되는 0인 징검다리 개수(consecutive_zeros)이다.
`consecutive_zeros` 값이 k 보다 크거나 같으면 건널 수 없다.

### 🧑🏻‍💻 Code

```python
def solution(stones, k):
    left, right = 1, max(stones)
    res = 0

    while left <= right:
        mid = (left + right) // 2

        consecutive_zeros = 0  # 연속된 0의 개수 초기화
        flag = True  # 건널 수 있는지 여부 플래그

        for stone in stones:
            if stone < mid:
                consecutive_zeros += 1  # 현재 돌의 값이 mid보다 작으면 연속된 0의 개수를 증가
                if consecutive_zeros >= k:
                    flag = False  # 연속된 0의 개수가 k보다 크거나 같으면 건널 수 없음
                    break
            else:
                consecutive_zeros = 0  # 현재 돌의 값이 mid 이상이면 연속된 0의 개수 초기화

        if flag:
            res = mid  # 답 저장
            left = mid + 1  # 건널 수 있는 경우, 왼쪽 범위를 mid + 1로 이동
        else:
            right = mid - 1  # 건널 수 없는 경우, 오른쪽 범위를 mid - 1로 이동

    return res

```
