# Python 풀이
import sys
import math

# constant
TYPE, ATK, HP = 0, 1, 2
MONSTER, POTION = 1, 2

# get input
N, atk = map(int, sys.stdin.readline().rstrip().split())
rooms = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


# search if possible (O(N))
def isPossible(max_HP):
    curr_hp, curr_atk = max_HP, atk
    for i in range(N):
        if rooms[i][TYPE] == MONSTER:
            mon_hp, mon_atk = rooms[i][HP], rooms[i][ATK]
            my_atk_count = math.ceil(mon_hp / curr_atk)
            monster_atk_count = math.ceil(curr_hp / mon_atk)
            if my_atk_count <= monster_atk_count:
                # win
                curr_hp -= (my_atk_count - 1) * mon_atk
            else:
                # lose
                return False
        else:
            curr_atk += rooms[i][ATK]
            if rooms[i][HP] + curr_hp > max_HP:
                curr_hp = max_HP
            else:
                curr_hp += rooms[i][HP]
    return True


left, right = 1, int(1e20)
answer = 0
while left <= right:  # binary search (O(logN))
    mid = (left + right) // 2
    if isPossible(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)
