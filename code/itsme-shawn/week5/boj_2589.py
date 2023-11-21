from collections import deque


def bfs(start, map, visited):
    queue = deque([(start, 0)])  # 큐를 이용하여 BFS 수행, (좌표, 거리) 형태로 저장
    visited[start[0]][start[1]] = True  # 방문 여부 체크
    max_distance = 0  # 최단 거리 중 최대 거리를 저장

    while queue:
        current, distance = queue.popleft()  # 현재위치, 거리
        max_distance = max(max_distance, distance)  # 최대 거리 갱신

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = current[0] + dx, current[1] + dy  # 현재 위치에서 4방향으로 이동

            # 지도 범위 내에 있고 육지(L)이며 방문하지 않았다면 큐에 추가
            if (
                0 <= nx < len(map)
                and 0 <= ny < len(map[0])
                and map[nx][ny] == "L"
                and not visited[nx][ny]
            ):
                queue.append(((nx, ny), distance + 1))  # 다음 위치와 거리를 큐에 추가
                visited[nx][ny] = True  # 방문 여부 표시

    return max_distance


def find_treasure_distance(map):
    max_distance = 0

    # 모든 육지 지점에 대해 최단 거리를 계산하고 최대 거리를 갱신
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "L":
                visited = [[False] * len(map[0]) for _ in range(len(map))]
                max_distance = max(max_distance, bfs((i, j), map, visited))

    return max_distance


rows, cols = map(int, input().split())
treasure_map = [input().strip() for _ in range(rows)]

# 보물의 최단 거리 출력
result = find_treasure_distance(treasure_map)
print(result)
