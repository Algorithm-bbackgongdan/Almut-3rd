# Week1
# boj_21758 : 꿀 따기
### code
```python
n = int(input())
honeys = list(map(int,input().split()))
result = 0

prefixSum = [0] * n
prefixSum[0] = honeys[0]
for i in range(1, n):
  prefixSum[i] = prefixSum[i-1] + honeys[i]

if n == 3:
  result = max(honeys) * 2

#꿀통 맨 왼쪽
for i in range(1, n-1):
  result = max(result, prefixSum[n-2] + prefixSum[i] - 2 * honeys[i])

#꿀통 맨 오른쪽
for i in range(1, n-1):
  result = max(result, prefixSum[n-1] - honeys[0] - honeys[i] + prefixSum[n-1] - prefixSum[i])

#꿀통 가운데
for i in range(1, n-1):
  result = max(result, prefixSum[i] - honeys[0] + prefixSum[n-2] - prefixSum[i-1])

print(result)

  ```
## 결과
### 성공
## 접근
가장 먼저 꿀벌 두 마리와 1개의 벌통을 무작위로 배치 후, 최대의 꿀의 양을 계산할려고 했지만,
n이 최대 100,000 이기 때문에 nC1 * (n-1)C2 이면 시간 초과가 난다고 판단 했다.

n = 3 일때는 1 개의 벌통과 꿀벌 2마리가 모두 할당되기 때문에 가장 큰 수에 벌통이 놓여있을 때 가장 많은 양의 꿀을 수확할 수 있다.

이후 n = 4, 5, 6 일 때를 하나하나 생각해보면서 공통점을 찾을 수 있었다.

벌통과 꿀벌 한 마리가 가장 멀리 떨어져 있을 때 가장 많은 양의 꿀을 수확할 수 있음을 깨달았다.
양쪽 끝 중 하나에 벌통이 있고, 반대쪽 끝에 꿀벌이 있는 경우 중, 남은 한 마리 꿀벌의 위치에 따라 가장 많은 양의 꿀을 얻을 수 있었다.

그리고 벌통이 중간 그 어딘가에 있을 때 최대로 많은 양의 꿀을 수확할 수 있는 경우가 있었는데,
이 때는 꿀벌이 양 쪽 끝에 위치함을 알 수 있었다.
## 문제 회고
벌통과 꿀벌 2마리 모두 위치를 바꿀 수 있어서 많은 경우의 수를 생각하는데 시간을 많이 소요했다.
벌통 혹은 꿀벌 중 어느 하나를 고정시키고 싶었지만 그 방법이 맞을까? 하는 생각에 많이 망설였던 문제였다. 

# 2174 : 로봇 시뮬레이션
### code
```python
A, B = map(int,input().split())
N, M = map(int,input().split())

robots = []

# N W S E
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(1,N+1):

  robot = list(input().split())

  #문제의 좌표 변환
  x = B - int(robot[1])
  y = int(robot[0]) - 1
  robot[0] = x
  robot[1] = y

  if robot[2] == 'N':
    robot[2] = 0
  elif robot[2] == 'W':
    robot[2] = 1
  elif robot[2] == 'S':
    robot[2] = 2
  else:           #'E'
    robot[2] = 3

  robots.append(robot)

for i in range(M):
  order = list(input().split())
  for j in range(int(order[2])):
    if order[1] == 'F':
      nx = robots[int(order[0])-1][0] + dx[robots[int(order[0])-1][2]]
      ny = robots[int(order[0])-1][1] + dy[robots[int(order[0])-1][2]]
      for k in robots:
        if k[0] == nx and k[1] == ny:
          print("Robot",order[0],"crashes into robot",robots.index(k)+1)
          exit()
      robots[int(order[0])-1][0] = nx
      robots[int(order[0])-1][1] = ny

      if nx < 0 or nx >= B or ny < 0 or ny >= A:
        print("Robot",order[0],"crashes into the wall")
        exit()
    elif order[1] == 'L':
      #robot 머리 숫자 + 1
      #if robot 머리 숫자 == 4 -> 0으로 바꿈
      robots[int(order[0])-1][2] += 1
      if robots[int(order[0])-1][2] == 4:
        robots[int(order[0])-1][2] = 0
    elif order[1] == 'R':
      #robot 머리 숫자 - 1
      #if robot 머리 숫자 == -1 -> 3으로 바꿈
      robots[int(order[0])-1][2] -= 1
      if robots[int(order[0])-1][2] == -1:
        robots[int(order[0])-1][2] = 3
print("OK")



  ```
## 결과
### 성공
## 접근
문제를 따라가면서 그대로 구현하고자 함.
문제의 좌표와 2차원 리스트의 인덱스가 달라 좌표 조정을 하였다.
알파벳으로 주어지는 로봇의 방향을 숫자로 변환하여 조작하고자 하였다.

## 문제 회고
처음에 로봇이 지나온 곳을 저장해야한다고 착각해서 헤맸다.
조정된 좌표를 기준으로 로봇의 움직임을 생각하는 것에서 머리가 많이 꼬여서 시간소요가 많았다. 입력으로 알파벳을 받다보니 인덱스 계산에서 int를 남발한 것이 맘에 들지 않는다.