//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool check(vector<int> stones, int k, int mid) {
    int cnt = 0;
    for (int i = 0; i < stones.size(); i++) {
        if (stones[i] < mid) cnt++;
        else cnt = 0;
        if (cnt == k) return false;
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;
    int left = *min_element(stones.begin(), stones.end()) - 1;
    int right = *max_element(stones.begin(), stones.end()) + 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (check(stones, k, mid)) {
            left = mid + 1;
            answer = mid;
        }
        else {
            right = mid - 1;
        }
    }
    return answer;
}

int main(void) {
    vector<int> stones = {2,4,5,3,2,1,4,2,5,1};
    int k = 3;
    int ans = solution(stones, k);
    cout << ans << endl;
    return 0;
}