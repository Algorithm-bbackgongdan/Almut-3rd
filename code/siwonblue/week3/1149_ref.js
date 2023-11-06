const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "/Users/jeonsiwon/Desktop/Almut-3rd/code/siwonblue/week3/input.txt";
const input = require("fs")
  .readFileSync(filePath, "utf-8")
  .toString()
  .trim()
  .split("\n");
const N = +input[0];

const memo = Array.from({ length: N + 1 }, () =>
  Array.from({ length: 3 }, () => 0)
);
memo[0][0] = 0;
memo[0][1] = 0;
memo[0][2] = 0;
for (let i = 1; i <= N; i++) {
  const [R, G, B] = input[i].split(" ").map(Number);
  memo[i][0] = Math.min(memo[i - 1][1], memo[i - 1][2]) + R;
  memo[i][1] = Math.min(memo[i - 1][0], memo[i - 1][2]) + G;
  memo[i][2] = Math.min(memo[i - 1][0], memo[i - 1][1]) + B;
}
console.log(Math.min(...memo[N]));
