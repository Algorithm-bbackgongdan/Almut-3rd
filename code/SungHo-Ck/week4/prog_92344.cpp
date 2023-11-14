#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;

    vector<vector<int>> dmg(board.size() + 1, vector<int>(board[0].size() + 1));

    for (int i = 0; i < skill.size(); i++) {
        int d = skill[i][5] * (skill[i][0] == 1 ? -1 : 1);
        dmg[skill[i][1]][skill[i][2]] += d;
        dmg[skill[i][1]][skill[i][4] + 1] -= d;
        dmg[skill[i][3] + 1][skill[i][2]] -= d;
        dmg[skill[i][3] + 1][skill[i][4] + 1] += d;
    }

    for (int i = 0; i < board[0].size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            dmg[j][i + 1] += dmg[j][i];
        }
    }
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            dmg[i + 1][j] += dmg[i][j];
        }
    }

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            board[i][j] += dmg[i][j];
            if (board[i][j] > 0)
                answer++;
        }
    }
    return answer;
}

int main(void) {
    vector<vector<int>> board = { {5, 5, 5, 5, 5}, {5, 5, 5, 5, 5}, {5, 5, 5, 5, 5}, {5, 5, 5, 5, 5} };
    vector<vector<int>> skill = { {1, 0, 0, 3, 4, 4}, {1, 2, 0, 2, 3, 2 }, { 2, 1, 0, 3, 1, 2 }, { 1, 0, 1, 3, 3, 1 } };
    int ans = solution(board, skill);
    cout << ans << endl;

    board = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    skill = { {1, 1, 1, 2, 2, 4}, {1, 0, 0, 1, 1, 2 }, { 2, 2, 0, 2, 0, 100} };
    ans = solution(board, skill);
    cout << ans << endl;
    return 0;
}