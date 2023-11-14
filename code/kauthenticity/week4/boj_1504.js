const readline = require("readline");
const lines = [];

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const MAX_VALUE = Number.MAX_SAFE_INTEGER;

function dijkstra(start, n, graph) {
    const dists = Array(n + 1).fill(MAX_VALUE);
    const visited = new Map();

    for (let node = 1; node <= n; node++) {
        dists[node] = graph[start][node];
    }
    dists[start] = 0;

    visited.set(start, true);

    while (visited.size < n) {
        // 방문하지 않은 제일 가까운 노드 찾기
        let [cur, minDist] = [-1, Number.MAX_SAFE_INTEGER];

        for (let node = 1; node <= n; node++) {
            if (!visited.get(node) && dists[node] < minDist) {
                minDist = dists[node];
                cur = node;
            }
        }

        if (cur === -1) {
            break;
        }
        visited.set(cur, true);

        // 이웃 노드들에 대해서 거리 갱신
        for (let adjacent = 1; adjacent <= n; adjacent++) {
            if (dists[adjacent] > dists[cur] + graph[cur][adjacent]) {
                dists[adjacent] = dists[cur] + graph[cur][adjacent];
            }
        }
    }
    return dists;
}

function solution(n, v1, v2, graph) {
    const startFrom1 = dijkstra(1, n, graph);
    const startFromV1 = dijkstra(v1, n, graph);
    const startFromV2 = dijkstra(v2, n, graph);

    let [path1, path2] = [MAX_VALUE, MAX_VALUE];

    // 1 - v1 - v2 - n
    if (
        startFrom1[v1] !== MAX_VALUE &&
        startFromV1[v2] !== MAX_VALUE &&
        startFromV2[n] !== MAX_VALUE
    ) {
        path1 = startFrom1[v1] + startFromV1[v2] + startFromV2[n];
    }

    // 1 - v2 - v1 - n
    if (
        startFrom1[v2] !== MAX_VALUE &&
        startFromV2[v1] !== MAX_VALUE &&
        startFromV1[n] !== MAX_VALUE
    ) {
        path2 = startFrom1[v2] + startFromV2[v1] + startFromV1[n];
    }

    return Math.min(path1, path2) === MAX_VALUE ? -1 : Math.min(path1, path2);
}

rl.on("line", (line) => {
    lines.push(line);
}).on("close", () => {
    const [line1, ...restLines] = lines;

    const [n, e] = line1.split(" ").map((c) => Number(c));
    const graph = Array(n + 1)
        .fill()
        .map(() => Array(n + 1).fill(Number.MAX_SAFE_INTEGER));

    const [v1, v2] = restLines[restLines.length - 1]
        .split(" ")
        .map((c) => Number(c));

    restLines.forEach((l, idx) => {
        if (idx === restLines.length - 1) {
            return;
        }
        const [a, b, c] = l.split(" ").map((c) => Number(c));
        graph[a][b] = c;
        graph[b][a] = c;
    });
    const answer = solution(n, v1, v2, graph);

    console.log(answer);
    process.exit();
});
