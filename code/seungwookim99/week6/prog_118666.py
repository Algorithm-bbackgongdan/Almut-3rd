def solution(survey, choices):
    ans = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    for i in range(len(survey)):
        first, second = survey[i]
        choice = choices[i]
        if choice > 4:
            ans[second] += choice - 4
        elif choice < 4:
            ans[first] += 4 - choice
    answer = ''
    # get result
    answer += 'R' if ans['R'] >= ans['T'] else 'T'
    answer += 'C' if ans['C'] >= ans['F'] else 'F'
    answer += 'J' if ans['J'] >= ans['M'] else 'M'
    answer += 'A' if ans['A'] >= ans['N'] else 'N'
    return answer