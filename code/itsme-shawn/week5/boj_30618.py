n = int(input())

lst = [0] * n

if n % 2 == 0:  # 짝수일때
    temp = n
    for i in range(n // 2, n):
        lst[i] = temp  # 오른쪽 대칭 부분
        temp -= 1

        lst[n - 1 - i] = temp  # 왼쪽 대칭 부분
        temp -= 1
else:  # 홀수일 때
    temp = n
    lst[n // 2] = temp  # 정중앙 값 채우기
    temp -= 1

    for i in range(n // 2 + 1, n):
        lst[i] = temp  # 오른쪽 대칭 부분
        temp -= 1

        lst[n - 1 - i] = temp  # 왼쪽 대칭 부분
        temp -= 1

print(*lst)
