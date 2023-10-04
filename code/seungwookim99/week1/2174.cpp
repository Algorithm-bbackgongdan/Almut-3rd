#include <iostream>
#include <cstdio>
using namespace std;

struct Bot
{
  int x, y, dir;
};

int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int A, B, N, M;
Bot bot[101];

bool out_of_range_(int y, int x)
{
  return (y < 0) || (y >= B) || (x < 0) || (x >= A);
}

int crash_into_robot(int y, int x)
{
  for (int i = 1; i <= N; i++)
  {
    if ((bot[i].y == y) && (bot[i].x == x))
      return i;
  }
  return -1;
}

int main(void)
{
  cin >> A >> B >> N >> M;
  for (int i = 1; i <= N; i++)
  {
    int rx, ry;
    char rdir;
    cin >> rx >> ry >> rdir;
    bot[i].x = rx - 1;
    bot[i].y = ry - 1;
    bot[i].dir = (rdir == 'S' ? 0 : (rdir == 'E' ? 1 : (rdir == 'N' ? 2 : 3)));
  }
  for (int i = 0; i < M; i++)
  {
    int idx, repeat;
    char cmd;
    cin >> idx >> cmd >> repeat;
    for (int j = 0; j < repeat; j++)
    {
      switch (cmd)
      {
      case 'L':
        bot[idx].dir = (bot[idx].dir + 1) % 4;
        break;
      case 'R':
        bot[idx].dir = (bot[idx].dir == 0 ? 3 : bot[idx].dir - 1);
        break;
      case 'F':
        int dir = bot[idx].dir;
        int ny = bot[idx].y + dy[dir], nx = bot[idx].x + dx[dir];
        int crashed;
        if (out_of_range_(ny, nx))
        {
          cout << "Robot " << idx << " crashes into the wall" << endl;
          return 0;
        }
        else if ((crashed = crash_into_robot(ny, nx)) > 0)
        {
          cout << "Robot " << idx << " crashes into robot " << crashed << endl;
          return 0;
        }
        bot[idx].y = ny;
        bot[idx].x = nx;
        break;
      }
    }
  }
  cout << "OK" << endl;
  return 0;
}