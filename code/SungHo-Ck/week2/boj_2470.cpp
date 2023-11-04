#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

int N;
int arr[100000];

int main(void) {
    int i, j;
    int a, b;
    char c;
    long long  min = 2000000000;
    long long temp_min;

    std::cin >> N;
    for (i = 0; i < N; i++) {
        std::cin >> arr[i];
    }
    i = 0;
    j = N - 1;
    std::sort(arr, arr + N);
    while (i != j) {
        temp_min = arr[i] + arr[j];
        if (abs(temp_min) < min) {
            min = abs(temp_min);
            a = arr[i];
            b = arr[j];
        }
        if (temp_min == 0)
            break;
        if (temp_min < 0)
            i++;
        else
            j--;
    }
    std::cout << a << " " << b << std::endl;
    return 0;
}