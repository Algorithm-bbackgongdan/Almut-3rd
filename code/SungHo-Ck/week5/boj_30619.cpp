#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int N, M, L, R;
int A[301];
int I[301];
int ans[301];

int main(void) {
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        I[A[i]] = i;
    }
    cin >> M;
    for (int i = 0; i < M; i++) {
        for (int j = 1; j <= N; j++) {
            I[A[j]] = j;
        }
        cin >> L >> R;

        sort(I+L,I+R+1);

        for (int j = 1; j <= N; j++) {
            ans[I[j]] = j;
        }
        for (int j = 1; j <= N; j++) {
            cout << ans[j] << " ";
        }
        cout << endl;
    }

    return 0;
}