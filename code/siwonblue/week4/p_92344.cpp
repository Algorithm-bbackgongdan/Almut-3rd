#include <string>
#include <vector>

using namespace std;
int map[1010][1010];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    
    int n = board.size();
    int m = board[0].size();
    
    for(auto v : skill) {
        int degree = v[5], r1 = v[1], c1 = v[2],
        r2 = v[3], c2 = v[4];
        if(v[0]==1) degree *= -1;
        
    
        map[r1][c1] += degree;
        map[r1][c2+1] -= degree;
        map[r2+1][c1] -= degree;
        map[r2+1][c2+1] += degree; 
    }
    
    
    for(int i = 1; i < n; i++)
        for(int j = 0; j < m; j++)
            map[i][j] += map[i-1][j];
    
    
    for(int i = 0; i < n; i++)
        for(int j = 1; j < m; j++)
            map[i][j] += map[i][j-1];
    
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++) {
            if(map[i][j] + board[i][j] > 0)
                answer++;
        }
    
    
    
    return answer;
}