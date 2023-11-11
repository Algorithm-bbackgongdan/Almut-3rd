const readline = require("readline");
const lines = [];

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function solution(n, m, items, graph) {
    let answer = 0;

    for (let k = 1; k < n + 1; k++) {
        for (let i = 1; i < n + 1; i++) {
            for (let j = 1; j < n + 1; j++) {
                if (i === j) {
                    graph[i][j] = 0;
                    continue;
                }
                graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    for (let node = 1; node < n + 1; node++) {
        let itemSum = 0;

        for (let adjacent = 1; adjacent < n + 1; adjacent++) {
            if (graph[node][adjacent] <= m) {
                itemSum += items[adjacent];
            }
        }

        answer = Math.max(answer, itemSum);
    }

    return answer;
}

rl.on("line", (line) => {
    lines.push(line);
}).on("close", () => {
    const [line1, line2, ...restLines] = lines;
    const [n, m, _] = line1.split(" ").map((c) => Number(c));
    const items = [0, ...line2.split(" ").map((c) => Number(c))];

    const graph = Array(n + 1)
        .fill()
        .map(() => Array(n + 1).fill(Number.MAX_SAFE_INTEGER));

    restLines.forEach((l) => {
        const [a, b, dist] = l.split(" ").map((c) => Number(c));
        graph[a][b] = dist;
        graph[b][a] = dist;
    });

    const answer = solution(n, m, items, graph);
    console.log(answer);

    process.exit();
});
