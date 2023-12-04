#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int c[30];
int b[7];
int dp[31][40001];

void sol(int n, int w){
    if(n > N || dp[n][w]) return;
    dp[n][w] = 1;
    sol(n + 1, w + c[n]);
    sol(n + 1, abs(w - c[n]));
    sol(n + 1, w);
}

int main()
{
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> c[i];
    }
    
    cin >> M;
    for(int i=0; i<M; i++){
        cin >> b[i];
    }
    
    sol(0,0);
    
    for(int i=0; i<M; i++){
        if(dp[N][b[i]]) cout << "Y ";
        else cout << "N ";
    }
    return 0;
}