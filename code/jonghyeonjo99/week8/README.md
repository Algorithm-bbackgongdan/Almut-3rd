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