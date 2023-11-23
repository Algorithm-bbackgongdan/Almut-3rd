# prog 118666 : 성격 유형 검사하기
### code
```python
def solution(survey, choices):
    answer = ''
    results = [[0 for _ in range(2)] for _ in range(8)]
               
    for i in range(len(choices)):
        if survey[i] == 'RT':
            if 1 <= choices[i] <= 3:
                results[0][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[0][1] += choices[i] - 4
        elif survey[i] == 'TR':
            if 1 <= choices[i] <= 3:
                results[1][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[1][1] += choices[i] - 4
        elif survey[i] == 'FC':
            if 1 <= choices[i] <= 3:
                results[2][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[2][1] += choices[i] - 4
        elif survey[i] == 'CF':
            if 1 <= choices[i] <= 3:
                results[3][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[3][1] += choices[i] - 4
        elif survey[i] == 'MJ':
            if 1 <= choices[i] <= 3:
                results[4][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[4][1] += choices[i] - 4
        elif survey[i] == 'JM':
            if 1 <= choices[i] <= 3:
                results[5][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[5][1] += choices[i] - 4
        elif survey[i] == 'AN':
            if 1 <= choices[i] <= 3:
                results[6][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[6][1] += choices[i] - 4
        elif survey[i] == 'NA':
            if 1 <= choices[i] <= 3:
                results[7][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[7][1] += choices[i] - 4
    
    answer += 'R' if (results[0][0] + results[1][1] >= results[0][1] + results[1][0]) else 'T'
    answer += 'C' if (results[2][0] + results[3][1] <= results[2][1] + results[3][0]) else 'F'
    answer += 'J' if (results[4][0] + results[5][1] <= results[4][1] + results[5][0]) else 'M'
    answer += 'A' if (results[6][0] + results[7][1] >= results[6][1] + results[7][0]) else 'N'
    
    return answer
  ```
## 결과
### 성공
## 접근
타 언어의 switch-case문처럼 8가지 경우의 수를 조건에 맞게 처리해주고, 결과값을 2차원 리스트에 담아 문제 조건에 맞게 answer에 추가해주었다.
## 문제 회고
위 코드로 문제해결은 가능했지만, 모범답안은 아닐 것이라고 생각하였다. 다른 풀이를 참조하여 딕셔너리 자료구조를 활용하면 보다 효율적인 풀이가 있음을 배울 수 있었다.

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