# boj_30619 : 내 집 마련하기
### code
```python
import sys
import copy

n = int(sys.stdin.readline().rstrip())
houses = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

for i in range(m):
  people = []
  l, r = map(int,sys.stdin.readline().rstrip().split())
  relocation_houses = copy.deepcopy(houses)
  for j in range(len(houses)):
    if (l <= houses[j] <= r):
      people.append(houses[j])
      relocation_houses[j] = 0
  
  people.sort(reverse= True)

  for j in range(len(relocation_houses)):
    if relocation_houses[j] == 0:
      relocation_houses[j] = people[-1]
      people.pop()
      
  for house in relocation_houses:
    print(house, end=' ')
  
  ```
## 결과
### 성공
## 접근
높은 번호의 집에, 높은 번호의 사람이 살아야 감면받을 수 있는 세금이 커진다.

따라서 L번부터 R번까지의 사람이 번호 순으로 높은 번호의 집에 살 때 가장 많은 세금을 감면 받을 수 있다.

1. 주어진 수열에서 L~R번 사이 번호사람을 따로 뽑아 번호 역순으로 정렬 시킨다. 그리고 새로 정렬될 수열('relocation_houses')에 L~R번 사이의 사람이 살던 집을 0으로 초기화 한다.
2. 이후 재배열 되는 수열에 번호 순서대로 사람을 재배치 시킨다.
## 문제 회고
처음에 문제 이해가 한번에 되지않아 당황했다.
수열에서 인덱스와 값이 의미하는 것을 이해하고, 어렵지않게 정렬을 통해 문제를 해결할 수 있었다.

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고

# 1234 : ABCD
### code
```python

  ```
## 결과

## 접근

## 문제 회고