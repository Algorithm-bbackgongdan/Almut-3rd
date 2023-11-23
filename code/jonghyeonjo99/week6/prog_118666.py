def solution(survey, choices):
    answer = ''
    results = [[0 for _ in range(2)] for _ in range(8)]
               
    for i in range(len(choices)):
        if survey[i] == 'RT':
            if 1 <= choices[i] <= 3:
                results[0][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[0][1] += choices[i] - 4
        elif survey[i] == 'TR':
            if 1 <= choices[i] <= 3:
                results[1][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[1][1] += choices[i] - 4
        elif survey[i] == 'FC':
            if 1 <= choices[i] <= 3:
                results[2][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[2][1] += choices[i] - 4
        elif survey[i] == 'CF':
            if 1 <= choices[i] <= 3:
                results[3][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[3][1] += choices[i] - 4
        elif survey[i] == 'MJ':
            if 1 <= choices[i] <= 3:
                results[4][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[4][1] += choices[i] - 4
        elif survey[i] == 'JM':
            if 1 <= choices[i] <= 3:
                results[5][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[5][1] += choices[i] - 4
        elif survey[i] == 'AN':
            if 1 <= choices[i] <= 3:
                results[6][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[6][1] += choices[i] - 4
        elif survey[i] == 'NA':
            if 1 <= choices[i] <= 3:
                results[7][0] += 4 - choices[i]
            elif 5 <= choices[i] <= 7:
                results[7][1] += choices[i] - 4
    
    answer += 'R' if (results[0][0] + results[1][1] >= results[0][1] + results[1][0]) else 'T'
    answer += 'C' if (results[2][0] + results[3][1] <= results[2][1] + results[3][0]) else 'F'
    answer += 'J' if (results[4][0] + results[5][1] <= results[4][1] + results[5][0]) else 'M'
    answer += 'A' if (results[6][0] + results[7][1] >= results[6][1] + results[7][0]) else 'N'
    
    return answer