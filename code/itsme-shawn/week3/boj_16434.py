N, A = map(int, input().split())
arr = []
for _ in range(N):
    type, atk, hp = map(int, input().split())
    arr.append((type, atk, hp))


# 던전 클리어 가능 여부를 확인하는 함수
def can_clear(maxHP):
    currentHP = maxHP
    currentATK = A

    for type, atk, hp in arr:
        if type == 1:  # 몬스터가 있는 방
            turns_needed = (hp + currentATK - 1) // currentATK  # 공격으로 몬스터를 쓰러트릴 때 필요한 턴 수 계산
            currentHP -= (turns_needed - 1) * atk  # 생명력 계산
        else:  # 포션이 있는 방
            currentATK += atk
            currentHP = min(maxHP, currentHP + hp)

        if currentHP <= 0:  # 현재 생명력이 0 이하인 경우 클리어 불가능
            return False
    return True


result = 0
start, end = 1, N * int(1e6) * int(1e6)

while start <= end:
    mid = (start + end) // 2

    if can_clear(mid):
        end = mid - 1  # 클리어 가능한 경우, 최소 maxHP를 줄임
        result = mid  # 현재의 mid를 결과로 저장

    else:
        start = mid + 1  # 클리어 불가능한 경우, 최소 maxHP를 늘림

print(result)
