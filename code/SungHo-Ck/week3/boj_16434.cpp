//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N, Atk;
int room[123456][3];
long long HP;

bool calcHP(long long mid) {
    long long atk = Atk;
    long long hp = mid;
    for (int i = 0; i < N; i++) {
        if (room[i][0] == 1) {
            //monster
            long long atkcnt = (long long)room[i][2] / atk + (room[i][2] % atk != 0) - 1;
            hp -= atkcnt * (long long)room[i][1];
            if (hp <= 0) {
                return false;
            }
        }
        else {
            //heal
            atk += (long long)room[i][1];
            hp = hp + (long long)room[i][2] > mid ? mid : hp + (long long)room[i][2];
        }
    }
    return true;
}

int main(void) {
    cin >> N >> Atk;
    for (int i = 0; i < N; i++) {
        int t;
        cin >> room[i][0] >> room[i][1] >> room[i][2];
    }

    long long left = 1;
    long long right = (long long)N * 1000000 * 1000000;
    while (left <= right) {
        long long mid = (left + right) / 2;
        if (calcHP(mid)) {
            right = mid - 1;
            HP = mid;
        }
        else {
            left = mid + 1;
        }
    }

    cout << HP << endl;
    return 0;
}