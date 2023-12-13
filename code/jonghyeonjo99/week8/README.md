# prog_42579 : 베스트앨범
### code
```python
def solution(genres, plays):
    answer = []
    dic = {}

    #(장르, 번호, 횟수)
    info = []

    for i in range(len(genres)):
        dic[genres[i]] = 0

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i]) + plays[i]
        info.append((genres[i], i, plays[i]))
    
    #플레이 횟수 내림차순 정렬
    dic = dict(sorted(dic.items(), key=lambda x : -x[1]))

    #장르, 플레이횟수 내림차순, 고유번호 오름차순 정렬
    info.sort(key=lambda x : (x[0], -x[2], x[1]))

    for key in dic.keys():
        count = 0
        for i in range(len(info)):
            if count >= 2:
                break

            if(key == info[i][0]):
                answer.append(info[i][1])
                count += 1
                
    return answer
  ```
## 결과
### 성공
## 접근
1. 장르의 개수를 알지 못하기 때문에 처음 genres list를 돌면서 장르를 딕셔너리 구조에 넣어준다.
2. 이후 다시한번 genres list를 돌면서 장르별 총 플레이 횟수를 위에서 만든 딕셔너리의 value값으로 넣어주고, 노래별 (장르, 고유번호, 플레이 횟수)를 info list에 넣어준다.
3. 이후 장르가 담긴 딕셔너리와 info list를 문제의 조건에 맞게 정렬한다.
4. 장르별로 가장 많이 플레이된 2곡을 answer list에 넣어주고, 출력한다.
## 문제 회고
딕셔너리 구조를 사용해본 경험이 많이 없어서 장르를 처리할 때 많이 헤맸다.
2가지 이상의 조건으로 데이터를 정렬하는 법을 배울 수 있었다.

# prog_42627 : 디스크컨트롤러
### code
```python

  ```
## 결과
### 고민 중입니다,,
## 접근

## 문제 회고


# prog_77485 : 행렬 테두리 회전하기
### code
```python
def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1

    for start_x, start_y, end_x, end_y in queries:
        min_num = arr[start_x-1][start_y-1]

        #위쪽 테두리
        for i in range(end_y-1,start_y,-1):
            arr[start_x-1][i] = arr[start_x-1][i-1]
            min_num = min(min_num, arr[start_x-1][i])

        #우측 테두리
        for i in range(end_x-1,start_x,-1):
            arr[i][end_y-1] = arr[i-1][end_y-1]
            min_num = min(min_num, arr[i][end_y-1])

        #아래 테두리
        for i in range(start_y,end_y):
            arr[end_x-1][i-1] = arr[end_x-1][i]
            min_num = min(min_num, arr[end_x-1][i])

        #좌측 테두리
        for i in range(start_x,end_x):
            arr[i-1][start_y-1] = arr[i][start_y-1]
            min_num = min(min_num, arr[i][start_y-1])

        answer.append(min_num)
    return answer
  ```
## 결과
### 실패
## 접근
완전탐색하여 문제가 시키는대로 시계방향으로 숫자를 돌리기로 하였다.
## 문제 회고
숫자가 시계방향으로 돌기 때문에 숫자의 이동을 시계반대방향부터 처리해주어야한다.
그렇지 않으면 각 테두리의 맨 앞의 숫자가 계속해서 이동하는 결과가 발생한다.
그래서 시계반대방향으로 숫자의 이동을 처리하였는데 틀렸다..

코드 중간에 실수가 있는 것 같은데, 나중에 천천히 복기해봐야겠다ㅠ