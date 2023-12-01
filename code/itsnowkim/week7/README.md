# 외계인의 기타 연주
문제를 이해하면 쉬운 문제였다.
특별한 로직이나 자료구조가 필요하지 않고,
같은 기타 줄을 누르고 있는 가장 높은 손가락을 순서에 맞게 저장하면 되는 문제였다.

stack 자료구조를 사용하여 높은 손가락부터 pop 하는 방식으로 구현할 수 있는데,
python 의 경우 list 로 구현할 수 있으며,
내림차순으로 list 를 관리하였다.
pop 대신 index 를 이용하여 list를 잘라내는 방식을 택했다.

# 양팔저울
dp 로 해결할 수 있는 문제이다.
특정 무게 추를 선택할 때, 구하고자 하는 유리구슬 쪽에 올릴지, 반대쪽에 올릴지, 올리지 않을지 결정하면 된다.

처음에 방법을 떠올리지 못해서 검색한 후에, dp table 을 만드는 방식을 캐치한 후 구현에 성공하였다.

dp 문제의 경우 예시로 "일반화" 를 잘 하는 것이 중요하다.

비슷한 문제로는 베낭 문제가 있다.

# 퍼즐 조각 채우기
구현을 잘 하면 풀 수 있는 문제였다.
반복되는 로직이 많기 때문에, 각각의 기능을 하는 함수를 분리하여 구현에 성공하였다.

처음에는 무식하게 네 방향 전부 rotate 로 검사하기 않기를 바라고 여러 조건에 따라 분기하였지만,
정확한 조건을 분리하지 못하여, 예외 케이스 때문에 전체 테스트 케이스 중 37%만 정답을 맞췄다.

그래서 그냥 무식하게 4 방향 rotate 로 구현했더니, 통과했다.

이 문제의 중요한 포인트는 두 가지 인 것 같다.
1. 동일한 로직의 경우 함수를 모듈화하여 작성할 것
2. index 실수를 하지 않을 것
3. 머릿속으로 구현한 방식이 정말 맞는지 테스트 해볼 것.

실제로 한 번에 통과하지 못하고 코드상의 예외를 찾을 때 질문하기 탭의 예시 input 을 통해 통과할 수 있었다.

생각하지 못했던 예시는 퍼즐의 크기가 커질 경우, 단순히 x,y 좌표의 min부터 max까지 복사할 경우, "연결되지 않지만 분명히 다른 퍼즐의 조각" 임에도 함께 복사가 되는 문제가 있었다.

따라서 퍼즐을 복사하는 알고리즘을 다음과 같이 수정하여 통과할 수 있었다.

기존 방식
```python
"""
N*M 직사각형 크기로 matrix 를 복사하고 return 하는 함수
"""
def make_piece(target, board, N):
    minx, miny = N, N
    maxx, maxy = 0, 0
    
    for x, y in target:
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x

        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    
    x = (maxx-minx+1)
    y = (maxy-miny+1)

    # 빈 값으로 초기화
    temp = [[0]*max(y,1) for _ in range(max(x,1))]

    # board 복사
    for idxi, i in enumerate(range(minx, maxx+1)):
        for idxj, j in enumerate(range(miny, maxy+1)):
            temp[idxi][idxj] = board[i][j]
    return temp

```

바꾼 방식
```python
"""
N*M 직사각형 크기로 matrix 를 복사하고 return 하는 함수
"""
def make_piece(target, board, N):
    minx, miny = N, N
    maxx, maxy = 0, 0
    INIT = board[target[0][0]][target[0][1]]
    VAL = 0
    if INIT == 1:
        INIT = 0
        VAL = 1
    else:
        INIT = 1
        VAL = 0
    
    for x, y in target:
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x

        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    
    x = (maxx-minx+1)
    y = (maxy-miny+1)

    # 빈 값으로 초기화
    temp = [[INIT]*max(y,1) for _ in range(max(x,1))]

    # board 복사 - target 을 순회하며 값을 넣기
    for tx, ty in target:
        i = tx-minx
        j = ty-miny
        temp[i][j] = VAL
    return temp
```

복사해야 하는 값만 temp에 복사하여 return 하는 방식으로, 버그를 없앨 수 있었다.