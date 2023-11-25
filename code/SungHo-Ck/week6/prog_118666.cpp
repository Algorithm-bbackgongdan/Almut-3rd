#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<string> servey, vector<int> choices) {
    int mbti[2][4] = { {0,0,0,0},{0,0,0,0} };
    char mbti_char[2][4] = { {'R','C','J','A'},{'T','F','M','N'} };
    string answer = "";
    for (int i = 0; i < servey.size(); i++) {
        if (choices[i] < 4) {
            switch (servey[i][0]) {
            case 'R': mbti[0][0] += 4 - choices[i]; break;
            case 'T': mbti[1][0] += 4 - choices[i]; break;
            case 'C': mbti[0][1] += 4 - choices[i]; break;
            case 'F': mbti[1][1] += 4 - choices[i]; break;
            case 'J': mbti[0][2] += 4 - choices[i]; break;
            case 'M': mbti[1][2] += 4 - choices[i]; break;
            case 'A': mbti[0][3] += 4 - choices[i]; break;
            case 'N': mbti[1][3] += 4 - choices[i];
            }
        }
        else if (choices[i] > 4) {
            switch (servey[i][1]) {
            case 'R': mbti[0][0] += choices[i] - 4; break;
            case 'T': mbti[1][0] += choices[i] - 4; break;
            case 'C': mbti[0][1] += choices[i] - 4; break;
            case 'F': mbti[1][1] += choices[i] - 4; break;
            case 'J': mbti[0][2] += choices[i] - 4; break;
            case 'M': mbti[1][2] += choices[i] - 4; break;
            case 'A': mbti[0][3] += choices[i] - 4; break;
            case 'N': mbti[1][3] += choices[i] - 4;
            }
        }
    }
    for (int i = 0; i < 4; i++) {
        if (mbti[0][i] >= mbti[1][i]) {
            answer.append(1, mbti_char[0][i]);
        }
        else {
            answer.append(1, mbti_char[1][i]);
        }
    }
    return answer;
}

int main(void) {
    vector<string> servey = { "AN", "CF", "MJ", "RT", "NA" };
    vector<int> choices = { 5, 3, 2, 7, 5 };
    string ans = solution(servey, choices);
    cout << ans << endl;

    servey = { "TR", "RT", "TR" };
    choices = { 7, 1, 3 };
    ans = solution(servey, choices);
    cout << ans << endl;
    return 0;
}