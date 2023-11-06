# boj_16434 : 드래곤 앤 던전
### code
```python
N, H = map(int,input().split())

dungeon = []

for _ in range(N):
  info = list(map(int,input().split()))
  dungeon.append(info)

left = 1
right = N * 1000000000000
answer = 0

while (left <= right):
  mid = (left + right) // 2
  HP = mid
  attack = H

  for i in range(len(dungeon)):

    if dungeon[i][0] == 1:
      quotient = dungeon[i][2] // attack
      rest = dungeon[i][2] % attack
      if rest == 0:
        HP -= dungeon[i][1] * (quotient-1)
      else:
        HP -=dungeon[i][1] * quotient
      if HP <= 0:
          break
    
    else:
      attack += dungeon[i][1]
      HP += dungeon[i][2]
      if HP > mid:
        HP = mid
  
  if HP > 0:
    right = mid -1
    answer = mid
  else:
    left = mid + 1

print(answer)
  ```
## 결과
### 성공
## 접근
용을 쓰러트리기 위한 최소의 H maxHP를 이분탐색을 통해서 구하자.

용사가 가질 수 있는 최대의 H maxHP는 최대 공격력, 최대 생명력인 몬스터를 N번 만났을 때이다.
따라서 이분탐색의 right값을 문제에서 주어진 가장 큰값이 들어가는 "N * 10^12" 으로 설정

용사가 몬스터를 쓰러트릴 때까지의 반복 과정을 수학식으로 해결

던전을 돌고 남은 HP가 0보다 큰 가장 작은 수가 될 때 mid값 출력

## 문제 회고
구현의 조건들을 빼먹어서 문제를 틀리는 실수를 몇번 하였다.
구현 조건과 일어날 수 있는 상황을 좀 더 꼼꼼하게 생각해볼 필요가 있을 것 같다.

이분탐색문제는 항상 구하고자 하는 값을 이분탐색의 mid값으로 생각하는 습관을 기르자..!!
# boj_1149 : RGB거리
### code
```python
n = int(input())

houses = []
dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
  house = list(map(int,input().split()))
  houses.append(house)

dp[0][0] = houses[0][0]
dp[0][1] = houses[0][1]
dp[0][2] = houses[0][2]

for i in range(1,n):
  dp[i][0] = min(houses[i][0] + dp[i-1][1], houses[i][0] + dp[i-1][2])
  dp[i][1] = min(houses[i][1] + dp[i-1][0], houses[i][1] + dp[i-1][2])
  dp[i][2] = min(houses[i][2] + dp[i-1][0], houses[i][2] + dp[i-1][1])

result = min(dp[n-1])
print(result)
  ```
## 결과
### 성공
## 접근
1. 1번 집부터 n번 집까지 인접하는 집끼리 서로 다른 색으로 칠해야 한다.
2. i번 째 집에 칠할 색을 정할 때, (i-1)번째 집까지 색깔을 칠한 최소비용이 담겨있는 dp 값을 불러와서 (i-1)번째 집과 다른 색을 칠할 때의 최솟값을 구한다.
3. 위에서 언급한 2차원 리스트 dp를 선언한다. 
```python
dp[집번호][RGB] = 최소비용
```
4. 바텀업 방식으로 n번째 집까지 색을 칠하는 최소비용을 구한다.
## 문제 회고
문제를 읽고, 값을 도출하는데까지 동일한 연산이 반복되는 것을 파악하고 다이나믹프로그래밍(DP)를 바로 떠올릴 수 있었다.
# prog_64062 : 징검다리 건너기
### code
```python
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while(left <= right):
        cnt = 0
        results = []
        mid = (left + right) // 2

        for i in range(len(stones)):
            if stones[i] <= mid:
                cnt += 1
            else:
                results.append(cnt)
                cnt = 0
                
        results.append(cnt)
        result = max(results)

        if result < k:
            left = mid + 1

        else:
            answer = mid
            right = mid - 1
            
    return answer
  ```
## 결과
### 실패(32.8점) 후 질문 참조
## 접근
stones의 배열의 크기가 최대 200,000 이기 때문에 완전탐색 시 시간초과 발생할 가능성이 많다.

디딤돌의 적힌 숫자는 한번에 건널 수 있는 디딤돌의 최대 칸수 k 범위 내에 있을 때, 그 디딤돌을 밟고 건너갈 수 있는 니니즈 친구들의 숫자를 의미한다.

디딤돌에 적힌 숫자가 징검다리를 건너간 니니즈 친구들의 숫자(mid)보다 작거나 같은 연속되는 디딤돌의 개수(cnt)를 구한다.

k범위 내에서 징검다리를 건너갈 수 있는 니니즈 친구들의 인원 수(mid)를 이분탐색을 통해 구한다.

## 문제 회고
주어진 배열의 크기를 보고 완전탐색은 어려울 것이라는 판단하였지만, 디딤돌의 위치를 이동시키면 안되었기 때문에 정렬도 하지못하고
어떤 값을 이분탐색을 통해 구해야하는지 생각해내지 못했다. 결국 디딤돌 사이 거리가 k보다 커질 때까지 반복문을 통한 구현을 했고 실패하였다.

이후 질문하기를 통해 mid값 이하의 숫자를 가진 디딤돌의 개수를 통해 이분탐색을 할 수 있음을 알 수 있었다.
이번 문제처럼 이분탐색을 통해 구해야하는 값이 숨겨져있는 경우(내생각..ㅎㅎ) 아이디어를 떠올리기 굉장히 어려운 것 같다. 