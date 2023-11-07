## prog_64062
이진탐색으로 풀이.
순차적으로 징검다리를 건너는 경우를 생각할 필요 없이, 일정한 범위만큼을 건너뛰는 이진탐색이 유리할 것으로 판단,
여러 시도 끝에 정답.
k 개 이상 0 을 찾기 위해 check 변수를 뒀는데, for loop 밖에서 check 를 초기화 해야 하는데
for loop 안에서 초기화 해서 디버깅 하는데 오래 걸림.
그 외에 특이한 것은 없었던 문제였던 것 같다.

## 1149
단순한 점화식을 만들어서 점화식을 바탕으로 쉽게 풀이했다.
min_cost(N) = min(N_min(R), N_min(G), N_min(B))
N_min(R) = min(N-1_min(G)+N(R), N-1_min(B)+N(R))


## 16434
이진탐색으로 접근.

```python
import sys

# 주어진 용사의 체력으로 clear 할 수 있는지 체크하는 함수
def success(hp, pow):
    max_hp = hp
    for roomtype, atk, heal in map_list:
        # 1 : 몬스터
        if roomtype == 1:
            while heal-pow > 0:
                heal -= pow
                hp -= atk
                if hp <= 0:
                    return False
        # 2 : 포션
        else:
            hp = min(hp+heal, max_hp)
            pow += atk

    return True


N, power = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

# 용사의 초기 체력
answer = 0
# start, end = 1, sys.maxsize
start, end = 1, int(1e6*1e6*N)

# 이진탐색
while start <= end:
    mid = (start+end) // 2
    
    # 성공함 -> hp 를 줄여봄
    if success(mid, power):
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)
```

시간초과. 최대 체력도 N 으로 최대한 줄였고,
이진탐색으로 최대 체력을 바꾸는 로직도 깔끔한 것 같다.
문제는 그렇다면 클리어가 가능한지 체크하는 함수를 더 줄여야 한다.

몬스터와 싸울 때 기본 로직을 턴 마다 서로 공격해서 체력을 확인하지 말고,
몬스터를 죽이기 위해 몇 번의 공격을 하고, 그 횟수-1 만큼 본인은 몬스터에게 맞아야 하기 때문에
이 방법으로 연산량을 줄이기로 했다.

이전 방법
```python
while heal-pow > 0:
    heal -= pow
    hp -= atk
    if hp <= 0:
        return False
```
변경 후 1트
```
python
hit_count = (heal // pow) + 1
hp -= (hit_count - 1) * atk
```
변경 후 N트
```
python
hit_count = (heal // pow) + 1 if heal % pow else heal//pow
hp -= (hit_count - 1) * atk
```

나누어 떨어질 때와 그렇지 않을 때 맞는 횟수가 딱 떨어지지 않는다는 걸 print로 디버깅 하면서 발견했다...

사소한 거지만 미리 당해봐서 다행이다.