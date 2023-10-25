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
const prices = [null];

for (let i = 1; i <= N; i++) {
  const price = {};
  const temp = input[i].split(" ").map(Number);
  price["R"] = temp[0];
  price["G"] = temp[1];
  price["B"] = temp[2];
  prices.push(price);
}
const colors = ["R", "G", "B"];

function BFS(initColor) {
  const memo = Array.from({ length: N + 1 }, () => Number.MAX_SAFE_INTEGER); // minimum price
  const queue = [];
  memo[1] = prices[1][initColor];
  queue.push({
    color: initColor,
    address: 1,
  });

  while (queue.length) {
    let { color, address } = queue.shift();
    for (let rgb of colors) {
      if (rgb === color) continue;
      if (address >= N) continue;
      const price = memo[address] + prices[address + 1][rgb];
      if (memo[address + 1] > price) {
        memo[address + 1] = price;
        queue.push({ color: rgb, address: address + 1 });
      }
    }
  }
  return memo[N];
}

function solution() {
  let ans = [];
  for (let rgb of colors) {
    ans.push(BFS(rgb));
  }
  return Math.min(...ans);
}
console.log(solution());
