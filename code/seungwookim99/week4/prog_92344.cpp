#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

int res[1001][1001];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    memset(res, 0, sizeof(int)*1001*1001);
    
    for(vector<int> s: skill) {
        int type = s[0], r1 = s[1], c1 = s[2], r2 = s[3], c2 = s[4], deg = s[5];
        deg *= (type == 1) ? -1 : 1;
        res[r1][c1] += deg;
        res[r1][c2+1] -= deg;
        res[r2+1][c1] -= deg;
        res[r2+1][c2+1] += deg;
    }
    
    for(int i = 0; i < board.size(); i++) {
        for(int j = 1; j < board[0].size(); j++) {
            res[i][j] += res[i][j-1];
        }
    }
    
    for(int j = 0; j < board[0].size(); j++) {
        for(int i = 1; i < board.size(); i++) {
            res[i][j] += res[i-1][j];
        }
    }
    
    for(int i = 0; i < board.size(); i++) {
        for(int j = 0; j < board[0].size(); j++) {
            if (res[i][j] + board[i][j] > 0) answer++;
        }
    }
    return answer;
}