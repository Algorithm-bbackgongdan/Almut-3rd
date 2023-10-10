const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath, "utf-8").toString().trim().split("\n");
const liquid = input[1].split(" ").map(Number);
const len = liquid.length;
const MAGIC_NUMBER = 0;

function solution() {
  let ans;
  let blending = 10 ** 9;

  // get positive, negative array
  liquid.sort((a, b) => a - b);
  let negative = [];
  let positive = [];
  for (let i = 0; i < len; i++) {
    const src = liquid[i];
    src < 0 ? negative.push(src) : positive.push(src);
  }
  negative = [...negative].reverse();

  // except
  if (positive.length === 0) return `${negative[0]} ${negative[1]}`;
  if (negative.length === 0) return `${positive[0]} ${positive[1]}`;

  // two pointer search
  let nP = 0;
  let pP = 0;
  while (nP < negative.length && pP < positive.length) {
    const blending_ = Math.abs(negative[nP] + positive[pP]);

    if (blending_ === MAGIC_NUMBER) return `${negative[nP]} ${positive[pP]}`;

    if (blending > blending_) {
      ans = [negative[nP], positive[pP]];
      blending = blending_;
    }
    if (Math.abs(negative[nP]) > Math.abs(positive[pP])) pP += 1;
    else nP += 1;
  }

  // except : if answer is in only positive case
  if (positive.length >= 2 && blending > Math.abs(positive[0] + positive[1]))
    return `${positive[0]} ${positive[1]}`;

  // except : if answer is in only negative case
  if (negative.length >= 2 && blending > Math.abs(negative[0] + negative[1]))
    return `${negative[1]} ${negative[0]}`;

  return ans.sort((a, b) => a - b).join(" ");
}
console.log(solution());
