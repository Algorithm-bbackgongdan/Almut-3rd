from collections import defaultdict

def solution(genres, plays):
    # 총 재생 횟수, 곡 저장
    genres_dict = defaultdict(list)
    res = []

    for idx, song in enumerate(genres):
        if song in genres_dict:
            genres_dict[song][0] += plays[idx]
            genres_dict[song][1].append((idx,  plays[idx]))
        else:
            time = plays[idx]
            songs = [(idx, plays[idx])]
            genres_dict[song] = [time, songs]

    genres_dict = sorted(genres_dict.items(), key=lambda x: -x[1][0])

    for _, (_, candits) in genres_dict:
        cnt = 0
        candits = sorted(candits, key=lambda x: (-x[1], x[0]))
        while cnt < 2 and cnt < len(candits):
            res.append(candits[cnt][0])
            cnt += 1

    return res


# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))