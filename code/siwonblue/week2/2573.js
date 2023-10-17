const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let line = fs.readFileSync(filePath, "utf-8");
let input = line.trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const maps = Array.from({ length: N });
const dx = [-1, 0, 1, 0];
const dy = [0, 1, 0, -1];

// get map
for (let i = 0; i < N; i++) {
  const rows = input[i].split(" ").map(Number);
  maps[i] = rows;
}

function checkAllDirection(x, y) {
  let cnt = 0;
  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx > N - 1 || ny > M - 1) continue;
    if (!maps[nx][ny]) cnt += 1;
  }
  return cnt;
}

// to check number of iceberg
function dfs(x, y, visit) {
  if (visit[x][y]) return;
  if (!maps[x][y]) return;
  visit[x][y] = true;

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx > N - 1 || ny > M - 1 || visit[nx][ny]) continue;
    dfs(nx, ny, visit);
  }
  return true;
}

function oneYearLater(year) {
  const counts = Array.from({ length: N }, () => Array(M).fill(0));
  // counts
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < M; y++) {
      if (!maps[x][y]) continue;
      counts[x][y] = checkAllDirection(x, y);
    }
  }

  // update
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < M; y++) {
      if (!counts[x][y]) continue;
      maps[x][y] -= counts[x][y];
      if (maps[x][y] < 0) maps[x][y] = 0;
    }
  }
  return year + 1;
}

function isAllMelted() {
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < M; y++) {
      if (maps[x][y]) return false;
    }
  }
  return true;
}

function getNumberOfIceberg() {
  let numOfIceberg = 0;
  const visit = Array.from({ length: N }, () => Array(M).fill(false));
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < M; y++) {
      if (!maps[x][y]) continue;
      const done = dfs(x, y, visit);
      if (done) numOfIceberg += 1;
    }
  }
  return numOfIceberg;
}

function solution() {
  let year = 0;
  while (true) {
    year = oneYearLater(year);
    const numOfIceberg = getNumberOfIceberg();
    const stop = isAllMelted();
    if (numOfIceberg >= 2) return year;
    if (stop) return 0;
  }
}
console.log(solution());
