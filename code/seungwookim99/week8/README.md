# Week 8

# 42579 : 베스트앨범
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
def solution(genres, plays):
    answer = []
    n = len(genres)
    genres_distinct = list(set(genres))
    total_plays = {g: 0 for g in genres_distinct}
    play_list = [] #(장르 총 플레이 수, 해당 노래 플레이 수, 고유 번호, genre)
    for i in range(n):
        total_plays[genres[i]] += plays[i]
    for i in range(n):
        genre = genres[i]
        play_list.append((total_plays[genre], plays[i], i, genre))
    play_list.sort(key=lambda x: (-x[0], -x[1], x[2]))
    
    curr_genre = ""
    cnt = 0
    for p in play_list:
        if curr_genre == p[3]:
            if cnt == 2:
                continue
            else:
                answer.append(p[2])
                cnt += 1
        else:
            curr_genre = p[3]
            answer.append(p[2])
            cnt = 1
    return answer
```

### ❗️ 결과

성공

### 💡 접근

장르별 총 플레이 수를 dictionary 형태로 저장한다.

그리고 `(장르 총 플레이 수, 노래 플레이 수, 노래 고유 번호, 장르명)` 을 리스트에 저장한 뒤 다음과 같은 기준으로 정렬한다.

1. 장르 총 플레이 수 내림차순
2. 노래 플레이 수 내림차순
3. 노래 고유 번호 오름차순

이후 동일 장르에 대해 최대 두 개씩 베스트 앨범에 수록한다.

## 🥳 문제 회고

정렬 조건이 많은 문제였다. 특히 장르 총 플레이 수를 계산하기 위해 dictionary를 사용해야 했다. 이후에 장르별 최대 두 곡을 수록하기 위해서도 고민해야 했던 문제였다.

# 42627 : 디스크 컨트롤러
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
from collections import deque

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    prev_end = 0
    while jobs:
        selected_job = jobs[0]
        min_length = 1001
        for job in jobs:
            if prev_end < job[0]:
                break
            elif min_length > job[1]:
                selected_job = job
                min_length = job[1]
        
        arrived_at, length = selected_job
        if prev_end < arrived_at:
            prev_end = arrived_at + length
            answer += length
        else:
            answer += (prev_end - arrived_at) + length
            prev_end += length
        jobs.remove(selected_job)
    return answer // n
```

### ❗️ 결과

성공

### 💡 접근

1. 현재 시각(이전 작업이 끝난 시각) 기준, 남은 작업들 중 요청 처리가 가능한 작업들을 구한다.
2. 만약 없다면, 현재 시각 이후 가장 빨리 도착한 요청을 처리하고 1번으로 돌아간다.
3. 요청 처리가 가능한 작업들 중 길이가 가장 짧은 작업을 수행한 뒤 1번으로 돌아간다.

## 🥳 문제 회고

한 요청을 처리할 때마다 현재 시각을 구한 뒤, 처리 가능한 작업들 리스트를 갱신해줘야 하는 까다로운 문제였다. 입출력 예제도 하나밖에 없어서 질문하기 탭에서 예제들 몇 개를 참고했다.

# 77485 : 행렬 테두리 회전하기
- 출처 : 프로그래머스

## 😎 Solved Code

### 💻 Code

```python
def solution(rows, columns, queries):
    answer = []
    board = []
    # 행렬 초기화
    for row in range(rows):
        tmp = []
        for col in range(columns):
            tmp.append(row * columns + col + 1)
        board.append(tmp)
        
    for x1,y1,x2,y2 in queries:
        x1 -=1
        y1 -=1
        x2 -=1
        y2 -=1
        min_num = initial_value = board[x1][y1]
        # 좌측 테두리 갱신
        for i in range(x1,x2):
            board[i][y1] = board[i+1][y1]
            min_num = min(min_num, board[i][y1])
        # 하단 테두리 갱신
        for i in range(y1,y2):
            board[x2][i] = board[x2][i+1]
            min_num = min(min_num, board[x2][i])
        # 우측 테두리 갱신
        for i in range(x2,x1,-1):
            board[i][y2] = board[i-1][y2]
            min_num = min(min_num, board[i][y2])
        # 상단 테두리 갱신
        for i in range(y2,y1,-1):
            board[x1][i] = board[x1][i-1]
            min_num = min(min_num, board[x1][i])
        board[x1][y1+1] = initial_value
        answer.append(min_num)
    return answer
```

### ❗️ 결과

성공

### 💡 접근

행렬을 만든 후, 각 query에 대해 시계 방향으로 회전을 시키며 최솟값을 추적한다.

## 🥳 문제 회고

주어진 요구사항대로 구현하면 되는 간단한 문제였다.