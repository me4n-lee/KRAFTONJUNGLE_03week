from collections import deque

m, n, h = map(int, input().split())

graph = []

for _ in range(h):
    graph_sub = []
    for i in range(n):
        a = list(map(int, input().split()))
        graph_sub.append(a)
    graph.append(graph_sub)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(h, n, m):
    que = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    que.append([i, j, k])

    while que:
        z, x, y = que.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                que.append([nz, nx, ny])

    result = -1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return -1
                result = max(result, graph[i][j][k])

    return result - 1

print(bfs(h, n, m))