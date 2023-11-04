//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int house[1000][3];

int main(void) {
    int cost[3];
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> cost[0] >> cost[1] >> cost[2];
        for (int j = 0; j < 3; j++) {
            house[i][j] = min(house[i - 1][(j + 1) % 3], house[i - 1][(j + 2) % 3]) + cost[j];
        }
    }
    cout << min(min(house[N - 1][0], house[N - 1][1]), house[N - 1][2]) << endl;
    return 0;
}