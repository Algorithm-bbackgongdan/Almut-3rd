import sys

# 주어진 용사의 체력으로 clear 할 수 있는지 체크하는 함수
def success(hp, pow):
    max_hp = hp
    for roomtype, atk, heal in map_list:
        # 1 : 몬스터
        if roomtype == 1:
            hit_count = (heal // pow) + 1 if heal % pow else heal//pow
            hp -= ((hit_count - 1) * atk)
            # print("hp / max_hp : ", hp, max_hp)
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
# 용사 최소 공격력 * 최대체력 * 방 개수
start, end = 1, int(1e6*1e6*N)

# 이진탐색
while start <= end:
    mid = (start+end) // 2
    # print('mid : ',mid)
    
    # 성공함 -> hp 를 줄여봄
    if success(mid, power):
        # print('success with : ',mid)
        answer = mid
        end = mid-1
    else:
        start = mid+1

print(answer)

