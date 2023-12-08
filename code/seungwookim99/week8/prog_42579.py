def solution(genres, plays):
    answer = []
    n = len(genres)
    genres_distinct = list(set(genres))
    total_plays = {g: 0 for g in genres_distinct}
    play_list = [] #(장르 총 플레이 수, 해당 노래 플레이 수, 고유 번호, genre)
    for i in range(n):
        total_plays[genres[i]] += plays[i]
    for i in range(n):
        genre = genres[i]
        play_list.append((total_plays[genre], plays[i], i, genre))
    play_list.sort(key=lambda x: (-x[0], -x[1], x[2]))
    
    curr_genre = ""
    cnt = 0
    for p in play_list:
        if curr_genre == p[3]:
            if cnt == 2:
                continue
            else:
                answer.append(p[2])
                cnt += 1
        else:
            curr_genre = p[3]
            answer.append(p[2])
            cnt = 1
    return answer