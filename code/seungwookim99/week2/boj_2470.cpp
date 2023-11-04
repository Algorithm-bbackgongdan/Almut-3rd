#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int N;

int main(void) {
  cin >> N;
  vector<int> plus, minus;
  for (int i = 0 ; i < N ; i++) {
    int tmp;
    cin >> tmp;
    if (tmp > 0) plus.push_back(tmp);
    else minus.push_back(tmp);
  }

  sort(plus.begin(), plus.end());
  sort(minus.rbegin(), minus.rend()); // 내림차순 정렬

  /* 산성 없음 (음수만)*/
  if (plus.empty()) {
    cout << minus[1] << " " << minus[0] << endl;
    return 0;
  }
  /* 알칼리성 없음 (양수만)*/
  else if (minus.empty()) {
    cout << plus[0] << " " << plus[1] << endl;
    return 0;
  }

  /* 산성, 알칼리성 둘 다 있음 */
  int i = 0, j = 0;
  int answer[2] = {minus[i], plus[j]};
  while ((i < minus.size()) && (j < plus.size())) {
    if (abs(minus[i] + plus[j]) < abs(answer[0] + answer[1])) {
      answer[0] = minus[i], answer[1] = plus[j];
    }
    if (minus[i] + plus[j] > 0) i++;
    else j++;
  }

  if ((plus.size() >= 2) && (plus[0] + plus[1] < abs(answer[0] + answer[1])))
    cout << plus[0] << " " << plus[1] << endl;
  else if ((minus.size() >= 2) && (abs(minus[0] + minus[1]) < abs(answer[0] + answer[1])))
    cout << minus[1] << " " << minus[0] << endl;
  else
    cout << answer[0] << " " << answer[1] << endl;
  return 0;
}