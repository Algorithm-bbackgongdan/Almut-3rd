# boj_16434 : 드래곤 앤 던전
### code
```python

  ```
## 결과

## 접근

## 문제 회고
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
# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고