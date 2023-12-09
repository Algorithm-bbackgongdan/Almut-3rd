def solution(genres, plays):
    answer = []
    dic = {}

    #(장르, 번호, 횟수)
    info = []

    for i in range(len(genres)):
        dic[genres[i]] = 0

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i]) + plays[i]
        info.append((genres[i], i, plays[i]))
    
    #플레이 횟수 내림차순 정렬
    dic = dict(sorted(dic.items(), key=lambda x : -x[1]))

    #장르, 플레이횟수 내림차순, 고유번호 오름차순 정렬
    info.sort(key=lambda x : (x[0], -x[2], x[1]))

    for key in dic.keys():
        count = 0
        for i in range(len(info)):
            if count >= 2:
                break

            if(key == info[i][0]):
                answer.append(info[i][1])
                count += 1
                
    return answer