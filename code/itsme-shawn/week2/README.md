# 2주차

## 1. 백준\_빙산 (2573)

### 💡 Idea

미방문한 빙산에 대해 bfs 를 돌리면 연결된 빙산(같은 덩어리인 빙산)은 방문처리가 되므로 빙산 한 덩어리가 카운팅 된다.

그리고 bfs 를 돌리면서 iceberg[i][j] 의 인접한 상하좌우를 보면서 깎아야할 높이를 계산해준다. => visited 배열에 방문여부와 함께 이 높이까지 같이 저장했다.

bfs 를 다 돌리고 나면 visited 에 담긴 정보를 바탕으로 높이를 감소시켜준다.

만일 분리된 빙산이 0개, 즉 count가 2가 되기 전에 다 녹아버린 경우는 flag 를 통해 0을 출력해준다.

### 🧑🏻‍💻 Code

```python
from collections import deque

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
flag = False

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        r, c = queue.popleft() # row, col
        for dy, dx in directions:
            nr = r + dy # next row
            nc = c + dx # next col

            if 0 <= nr < n and 0 <= nc < m:
                if iceberg[nr][nc] == 0: # 주변이 빙산이 아니라면 (바다라면)
                    visited[r][c] += 1 # 깎을 빙산 수 증가

                if not visited[nr][nc] and iceberg[nr][nc] != 0: # 미방문한 빙산에 대해
                    queue.append((nr, nc))
                    visited[nr][nc] = True

time = 0
while True:
    count = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and iceberg[i][j] != 0:
                bfs(i, j)
                count += 1 # 빙산 개수 증가

    # bfs 다 돌린 후 빙산의 높이 감소 시키기
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                iceberg[i][j] -= visited[i][j] - 1
                if iceberg[i][j] < 0:
                    iceberg[i][j] = 0

    time += 1
    if count == 0: # 분리된 빙산이 없는 경우
        break
    if count >= 2:
        flag = True
        break

if flag:
    print(time - 1)
else:
    print(0)
```

## 2. 백준\_두 용액 (2470)

### 💡 Idea

투 포인터를 사용하는데, 각각을 0번째 인덱스와 n-1 번째 인덱스로 우선 설정한다.

그 후로 매번 합을 계산해서 절댓값이 작다면 갱신한다.

시작포인터(start) 는 +1 을 해서 오른쪽으로 진행하고, 끝포인터(end) 는 -1 을 해서 왼쪽으로 진행한다.

`start < end` 일 동안만 진행한다.

### 🧑🏻‍💻 Code

```python
import sys

read = sys.stdin.readline

n = int(read())
lst = sorted(list(map(int, read().split())))


start = 0
end = n - 1
minn = float("inf")

while start < end: # 등호 들어가면 안 됨!
    cur_sum = lst[start] + lst[end]

    if abs(cur_sum) < minn:
        cur = [lst[start], lst[end]]
        minn = abs(cur_sum)
        if minn == 0:
            break

    if cur_sum < 0:
        start += 1
    else:
        end -= 1

print(cur[0], cur[1])
```

## 3. 프로그래머스\_단어 변환 (43163)

### 💡 Idea

풀이참고 : https://naa0.tistory.com/153

처음에는 백트래킹을 이용한 dfs 풀이로 시도를 하였는데 실패하였다.

bfs 에서 깊이 값을 저장하면서 방문한 노드에 대해서는 그냥 지나간다 는 방식으로 풀 수 있었다.
어려웠다..

![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzAQMQ%2FbtrGfoAzPT4%2FjFB1TxaweeYcl2LGzvALfk%2Fimg.png)

### 🧑🏻‍💻 Code

```python
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])    # [단어, 깊이]
    V = [0] * (len(words))  # 방문 노드 여부 확인 리스트
    while q:
        word, depth = q.popleft()
        if word == target:
            answer = depth
            break
        for i in range(len(words)):
            word_diff_cnt = 0
            if not V[i]:  # 만약 방문 안 한 단어라면
                # 단어의 한 글자씩 비교하면서 다른 글자 수 세기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        word_diff_cnt += 1

                if word_diff_cnt == 1:   # 만약 다른 글자 개수가 1개라면
                    q.append([words[i], depth+1])
                    V[i] = 1 # 방문 처리

    return answer
```
