// 백준 1149 : RGB거리
// C++ 풀이
#include <iostream>
#include <cstdio>
#define R 0
#define G 1
#define B 2
#define MAX 1000
using namespace std;

int main(int argc, char **argv) {
  int N;
  int costs[MAX][3];
  int dp[MAX][3];
  cin >> N;
  for (int i = 0 ; i < N ; i++)
    cin >> costs[i][R] >> costs[i][G] >> costs[i][B];
  dp[0][R] = costs[0][R];
  dp[0][G] = costs[0][G];
  dp[0][B] = costs[0][B];

  for (int i = 1 ; i < N ; i++) {
    dp[i][R] = costs[i][R] + min(dp[i-1][G], dp[i-1][B]);
    dp[i][G] = costs[i][G] + min(dp[i-1][R], dp[i-1][B]);
    dp[i][B] = costs[i][B] + min(dp[i-1][R], dp[i-1][G]);
  }

  cout << min(dp[N-1][R], min(dp[N-1][G], dp[N-1][B])) << endl;
  return 0;
}