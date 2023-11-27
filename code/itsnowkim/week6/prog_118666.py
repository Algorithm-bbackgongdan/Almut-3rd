def solution(survey, choices):
    answer = ''
    personality = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    scores = [3,2,1,0,1,2,3]

    for idx, choice in enumerate(choices):
        s = scores[choice-1]
        a = survey[idx][0]
        b = survey[idx][1]
        
        if choice <= 3:
            personality[a] += s
        else:
            personality[b] += s

    # 계산
    if personality["R"] >= personality["T"]:
        answer += "R"
    else:
        answer += "T"

    if personality["C"] >= personality["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if personality["J"] >= personality["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if personality["A"] >= personality["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer