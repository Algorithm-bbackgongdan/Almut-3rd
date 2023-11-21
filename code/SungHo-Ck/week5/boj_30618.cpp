#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int N;
int A[200001];

int main(void) {
    cin >> N;
    for (int i = 0; i <= N; i++) {
        if (i % 2 == 0) {
            A[i / 2] = i;
        }
        else {
            A[N - i / 2] = i;
		}
    }
    for (int i = 1; i <= N; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}