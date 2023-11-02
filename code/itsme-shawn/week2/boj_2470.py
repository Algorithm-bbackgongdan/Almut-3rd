import sys

read = sys.stdin.readline

n = int(read())
lst = sorted(list(map(int, read().split())))


start = 0
end = n - 1
minn = float("inf")

while start < end: # 등호 들어가면 안 됨!
    cur_sum = lst[start] + lst[end]

    if abs(cur_sum) < minn:
        cur = [lst[start], lst[end]]
        minn = abs(cur_sum)
        if minn == 0:
            break

    if cur_sum < 0:
        start += 1
    else:
        end -= 1

print(cur[0], cur[1])