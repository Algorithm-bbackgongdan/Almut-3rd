# WEEK 5

## PROGRAMMERS 42579

### Code

```javascript
function solution(genres, plays) {
    var answer = [];
    const playCntPerGenre = {}; // [장르]: 플레이 횟수
    const playCntPerSong = {}; // [장르]: [횟수, 번호]

    genres.forEach((genre, i) => {
        if (playCntPerSong[genre]) {
            playCntPerSong[genre].push([plays[i], i]);
        } else {
            playCntPerSong[genre] = [[plays[i], i]];
        }

        if (playCntPerGenre[genre]) {
            playCntPerGenre[genre] += plays[i];
        } else {
            playCntPerGenre[genre] = plays[i];
        }
    });

    Object.keys(playCntPerSong).forEach((key) => {
        playCntPerSong[key].sort(([cnt1, idx1], [cnt2, idx2]) => {
            if (cnt1 == cnt2) {
                return idx1 - idx2;
            }
            return cnt2 - cnt1;
        });
    });

    Object.entries(playCntPerGenre)
        .sort(([_, cnt1], [__, cnt2]) => {
            return cnt2 - cnt1;
        })
        .forEach(([genre]) => {
            if (playCntPerSong[genre].length == 1) {
                answer.push(playCntPerSong[genre][0][1]);
            } else {
                answer.push(
                    playCntPerSong[genre][0][1],
                    playCntPerSong[genre][1][1]
                );
            }
        });

    return answer;
}
```

### Approach

1. `playCntPerGenre` -> 장르 별 총 재생 횟수, `playCntPerSong` -> 장르 별 [노래의 재생 횟수, 노래 번호] 로 두 객체를 정의한다.
2. `genres` 배열을 돌면서 `playCntPerGenre`와 `playCntPerSong`을 갱신해 준다.
3. 장르 별 노래 재생 횟수를 재생 횟수의 내림차순으로 정렬한다.
4. 장르 별 총 재생 횟수를 내림차순으로 정렬한다.
5. 장르 별 총 노래 재생 횟수를 순회하면서, 해당 장르에 속한 노래가 1개면 하나의 곡만 선택하고, 두 개 이상이면 재생횟수가 제일 많은 두 가지 노래를 선택한다.

### TIL

별다른 알고리즘이 필요 없는 구현 문제였다. Object.entries, Object.keys를 요긴하게 써먹을 수 있는 문제였다.

## PROGRAMMERS 42627

### Code

```python
from heapq import heappush, heappop, heapify


def solution(jobs):
    answer = 0
    heap = []
    end, i = 0, 0
    start = -1

    while len(jobs) > i :
        for job in jobs :
            if start < job[0] <= end :
                heappush(heap, (job[1], job[0]))

        if len(heap) > 0 :
            take, request = heappop(heap)

            start = end
            end += take
            answer += end - request
            i += 1
        else :
            end += 1
    answer = answer//len(jobs)
    return answer
```

### Approach

1. '종료 시간 - 요청 시간'의 합을 작게 만들어야 한다.
2. 종료 시간은 작업의 처리 시간에 의존한다. -> 따라서 처리 시간이 짧은 것부터 처리하자!
3. 디스크가 작업 중일 때 들어온 작업을 priority queue에 추가해 준다.
4. priority queue에서 처리 시간이 제일 작은 job을 꺼낸다,
5. 그 job에 대해 디스크 처리 시간, 평균 시간을 갱신해 준다.

### TIL

문제를 열심히 째려봤지만 결국에는 풀이를 봤다. 하지만 풀이를 보니 간결했다. "종료 시간 - 요청 시간"을 작게 만드는 방법을 따라가면 됐다.
모르겠으면 구해야할 것을 보고, 구해야할 것을 만들기 위해서는 어떻게 해야할지 생각하는 습관을 기르자.

## PROG 774856

### Code

```python
def setNumbers(matrix, query, numbers):
    minNum = 10001


    x1, y1, x2, y2 = query

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    idx = 0


    for i in range(y1, y2+1) :
        matrix[x1][i] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1

    for i in range(x1+1, x2+1) :
        matrix[i][y2] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1

    for i in range(y2-1, y1-1, -1) :
        matrix[x2][i] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1


    for i in range(x2-1, x1, -1):
        matrix[i][y1] = numbers[idx]
        minNum = min(minNum, numbers[idx])
        idx += 1

    return minNum


def getNumbers(matrix, query) :
    x1, y1, x2, y2 = query
    numbers = []

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1


    for i in range(y1, y2+1) :
        numbers.append(matrix[x1][i])

    for i in range(x1+1, x2+1) :
        numbers.append(matrix[i][y2])

    for i in range(y2-1, y1-1, -1) :
        numbers.append(matrix[x2][i])

    for i in range(x2-1, x1, -1):
        numbers.append(matrix[i][y1])

    return numbers


def move(matrix, query):
    numbers = getNumbers(matrix, query)

    last = numbers[-1]
    numbers = [last] + numbers[0:-1]

    minNum = setNumbers(matrix, query, numbers)


    return minNum

def solution(rows, columns, queries):
    answer = []

    matrix = []

    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(i * columns + j + 1)
    for query in queries:
        answer.append(move(matrix, query))

    return answer

```

### Approach

1. 회전해야할 부분을 1차원으로 flattening하자.
2. flattening할 때에는 위 -> 오른쪽 -> 아래 -> 왼쪽 순서로 flattening한다.
3. flattening 후에는 오른쪽으로 한 칸 씩 밀어준다.
4. 그리고 다시 위 -> 오른쪽 -> 아래 -> 왼쪽 순서로 2차원으로 저장한다.

### TIL

n이 100이고 query도 10^4여서 n^2\*query = 10^8이므로, 2차원 루프를 돌려도 시간초과가 발생하지 않아서 이중 루프를 돌렸다.
이렇게 사용하는 알고리즘의 시간 복잡도를 명확히 계산한 다음에 문제를 푸는게 삽질의 시간을 줄일 수 있는 것 같다.
