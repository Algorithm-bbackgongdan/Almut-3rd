# 구슬의 최대 무게 40000
MAX=40001
# MAX=11
n = int(input())
weight = list(map(int, input().split()))
weight.sort()

# 구슬의 개수는 7 이하
m = int(input())
target_list = list(map(int, input().split()))

# 추를 이용해서 만들 수 있는 무게가 target 과 같은가?
"""
dp[i][j] = i번째 추를 사용했을 때, j 무게를 만들 수 있는가?
dp[i][j] = dp[i-1][j-w]
"""
dp = [[0]*MAX for _ in range(len(weight))]
def construct():
    # 초기화
    for idx, w in enumerate(weight):
        dp[idx][0] = 1
        dp[idx][w] = 1

    # dp 출력
    # print("before")
    # for d in dp:
    #     print(d)

    for idx, w in enumerate(weight):
        for j in range(MAX):
            for k in range(idx):
                if dp[k][j] == 1:
                    # 지금 무게 제외
                    temp_weight = abs(w - j)
                    dp[idx][temp_weight] = 1

                    # 지금 무게 추가 
                    temp_weight = j + w
                    if temp_weight < MAX:
                        dp[idx][temp_weight] = 1

    # dp 출력
    # print("after")
    # for d in dp:
    #     print(d)

def check(target):
    for idx in range(len(weight)):
        if dp[idx][target] == 1:
            return "Y"
    
    return "N"
    
answer = []
# dp 테이블 만들기
construct()
for target in target_list:
    # Y, N 을 리턴하는 check 함수
    answer.append(check(target))


for a in answer:
    print(a, end=' ')
print('')