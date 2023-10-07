#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int a, b, N, M;
int pass = 1;

struct robot {
    int x;
    int y;
    int num;
    char dir;
};

struct robot robots[100];
int map[101][101];

void wallB(int num) {
    printf("Robot %d crashes into the wall", num + 1);
	pass = 0;
}

void robotB(int num) {
	printf("Robot %d crashes into robot %d", num + 1, map[robots[num].x][robots[num].y] + 1);
	pass = 0;
}

void left(struct robot* robot) {
    switch (robot->dir) {
		case 'N':
			robot->dir = 'W';
			break;
		case 'W':
			robot->dir = 'S';
			break;
		case 'S':
			robot->dir = 'E';
			break;
		case 'E':
			robot->dir = 'N';
			break;
	}
}

void right(struct robot* robot) {
    switch (robot->dir) {
        case 'N':
            robot->dir = 'E';
            break;
        case 'W':
            robot->dir = 'N';
            break;
        case 'S':
            robot->dir = 'W';
            break;
        case 'E':
            robot->dir = 'S';
            break;
    }
}

void front(struct robot* r) {
    switch (r->dir) {
        case 'N':
            r->y++;
            if (r->y > b) {
                wallB(r->num);
                return;
            }
            else {
                if (map[r->x][r->y] != 0) {
                    robotB(r->num);
                    return;
                }
                else {
                    map[r->x][r->y] = r->num;
                    map[r->x][r->y - 1] = 0;
                }
            }
            break;
        case 'W':
            r->x--;
            if (r->x < 1) {
                wallB(r->num);
                return;
            }
            else {
                if (map[r->x][r->y] != 0) {
                    robotB(r->num);
                    return;
                }
                else {
                    map[r->x][r->y] = r->num;
                    map[r->x + 1][r->y] = 0;
                }
            }
            break;
        case 'S':
            r->y--;
            if (r->y < 1) {
                wallB(r->num);
                return;
            }
            else {
                if (map[r->x][r->y] != 0) {
                    robotB(r->num);
                    return;
                }
                else {
                    map[r->x][r->y] = r->num;
                    map[r->x][r->y + 1] = 0;
                }
            }
            break;
        case 'E':
            r->x++;
            if (r->x > a) {
                wallB(r->num);
                return;
            }
            else {
                if (map[r->x][r->y] != 0) {
                    robotB(r->num);
                    return;
                }
                else {
                    map[r->x][r->y] = r->num;
                    map[r->x - 1][r->y] = 0;
                }
            }
            break;
    }
}

int main(void) {
    scanf("%d %d", &a, &b);
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) {
        int x, y;
        char dir;
        scanf("%d %d %c", &x, &y, &dir);
        robots[i].x = x;
        robots[i].y = y;
        robots[i].num = i;
        robots[i].dir = dir;
        map[x][y] = i;
    }
    for (int i = 0; i < M; i++) {
        if (!pass) break;
        int num, cnt;
        char order;
        scanf("%d %c %d", &num, &order, &cnt);
        switch (order) {
            case 'L':
                for (int i = 0; i < cnt; i++) {
                    if (!pass)
                        break;
                    left(&robots[num-1]);
                }
                break;
            case 'R':
                for (int i = 0; i < cnt; i++) {
                    if (!pass)
                        break;
                    right(&robots[num-1]);
                }
                break;
			case 'F':
                for (int i = 0; i < cnt; i++) {
                    if (!pass)
                        break;
                    front(&robots[num-1]);
                }
        }
    }

    if (pass) {
		printf("OK");
	}
    return 0;
}