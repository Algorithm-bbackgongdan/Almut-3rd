// C++ 풀이
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
  int N;
  cin >> N;
  int place[N];
  for (int i = 0; i < N; i++)
    cin >> place[i];

  int maxVal = 0;
  int cumulativeSumFromLeft[N];
  cumulativeSumFromLeft[0] = place[0];
  for (int i = 1; i < N; i++)
    cumulativeSumFromLeft[i] = place[i] + cumulativeSumFromLeft[i - 1]; // 누적합 계산
  int cumulativeSumFromRight[N];
  cumulativeSumFromRight[N - 1] = place[N - 1];
  for (int i = N - 2; i >= 0; i--)
    cumulativeSumFromRight[i] = place[i] + cumulativeSumFromRight[i + 1]; // 누적합 계산

  // 맨 왼쪽(0번째 인덱스)이 벌통
  for (int i = 1; i < N - 1; i++)
    maxVal = max(maxVal, cumulativeSumFromLeft[N - 1] + cumulativeSumFromLeft[i] - 2 * place[i] - place[N - 1]);

  // 맨 오른쪽(마지막 인덱스)이 벌통
  for (int i = N - 2; i > 0; i--)
    maxVal = max(maxVal, cumulativeSumFromRight[0] + cumulativeSumFromRight[i] - 2 * place[i] - place[0]);

  // 중간 인덱스가 벌통
  for (int i = 1; i < N - 1; i++)
    maxVal = max(maxVal, cumulativeSumFromLeft[i] + cumulativeSumFromRight[i] - place[0] - place[N - 1]);
  cout << maxVal << endl;
  return 0;
}