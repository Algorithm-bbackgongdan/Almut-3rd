function solution(n, paths, gates, summits) {
  const maps = Array.from({ length: n + 1 }, () => []);
  const visit = Array.from({ length: n + 1 }, () => 0);
  for (let i = 0; i < paths.length; i++) {
    const path = paths[i];
    maps[path[0]].push([path[1], path[2]]);
    maps[path[1]].push([path[0], path[2]]);
  }
}

solution(
  6,
  [
    [1, 2, 3],
    [2, 3, 5],
    [2, 4, 2],
    [2, 5, 4],
    [3, 4, 4],
    [4, 5, 3],
    [4, 6, 1],
    [5, 6, 1],
  ],
  [1, 3],
  [5]
);
