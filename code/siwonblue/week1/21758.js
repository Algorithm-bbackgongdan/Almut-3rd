const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let line = fs.readFileSync(filePath, "utf-8");
let input = line.trim().split("\n")[1].split(" ").map(Number);

const len = input.length;
const firstIndex = 0;
const lastIndex = len - 1;

function bucketIsInMiddle() {
  const bees = [...input].slice(1, lastIndex);
  const sum = bees.reduce((acc, cur) => acc + cur);
  const max = Math.max(...bees);
  return sum + max;
}

function bucketIsInEdge(arr) {
  const bucketEdge = arr[firstIndex];
  const bees = [...arr].slice(1);

  let maxNum = Number.MIN_SAFE_INTEGER;

  // select bee
  for (let i = 0; i < bees.length - 1; i++) {
    let firstLineSum = 0;
    const firstBee = bees[i];
    const firstLine = bees.slice(0, i);
    if (firstLine.length !== 0)
      firstLineSum += firstLine.reduce((acc, cur) => acc + cur);
    // console.log("firstLine", firstLine);

    // select another bee
    for (let j = i + 1; j < bees.length; j++) {
      let sum = 0;
      sum += firstLineSum;

      const secondLine = bees.slice(0, j);
      // console.log("secondLine:", secondLine);
      if (secondLine.length !== 0)
        sum += bees.slice(0, j).reduce((acc, cur) => acc + cur);

      sum -= firstBee;
      sum += bucketEdge * 2;
      // console.log("sum:", sum);
      maxNum = Math.max(maxNum, sum);
    }
    // console.log("bucketEdge:", bucketEdge);
    // console.log("\n\n");
  }

  return maxNum;
}

// console.log("case1:", bucketIsInMiddle());
// console.log("case2:", bucketIsInEdge(input));
// console.log("case2:", bucketIsInEdge([...input].reverse()));

console.log(
  Math.max(
    bucketIsInMiddle(),
    bucketIsInEdge(input),
    bucketIsInEdge([...input].reverse())
  )
);
