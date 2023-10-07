#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int N;
int honey[100000];
int sumArray[100000];

int maxI;
int answer;

int maxf(int a, int b) {
	return a > b ? a : b;
}

int main(void) {

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &honey[i]);
    }
    sumArray[0] = honey[0];
    for (int i = 1; i < N; i++) {
        sumArray[i] = sumArray[i - 1] + honey[i];
        if (honey[maxI] < honey[i]) {
            maxI = i;
        }
    }

    //left side
    for (int i = N - 2; i > 0; i--) {
        int s = sumArray[N - 1] + sumArray[i] - honey[N - 1] - 2 * honey[i];
        answer = maxf(answer, s);
    }
    //printf("left:%d\n", answer);

    //right side
    sumArray[N - 1] = honey[N - 1];
    for (int i = N - 2; i >= 0; i--) {
        sumArray[i] = sumArray[i + 1] + honey[i];
    }
    for (int i = 1; i < N; i++) {
        int s = sumArray[0] + sumArray[i] - honey[0] - 2 * honey[i];
        answer = maxf(answer, s);
    }
    //printf("right:%d\n", answer);

    //middle
    if (maxI != 0 && maxI != N - 1) {
        int s = 0;
        for (int i = 1; i <= maxI; i++) {
            s += honey[i];
        }
        for (int i = N - 2; i >= maxI; i--) {
            s += honey[i];
        }
        answer = maxf(answer, s);
	}

    printf("%d", answer);
    return 0;
}