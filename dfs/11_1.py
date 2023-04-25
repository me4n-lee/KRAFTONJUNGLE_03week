import sys

n, m = map(int, input().split())

graph = []
for _ in range(n):
    m_list = list(map(int, input().split()))
    graph.append(m_list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melt(graph, n, m):
    new_graph = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        cnt += 1

                new_graph[x][y] = max(0, graph[x][y] - cnt)
    return new_graph

def dfs_2(graph, n, m, x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        a, b = stack.pop()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_pieces(graph, n, m):
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0 and not visited[x][y]:
                dfs_2(graph, n, m, x, y, visited)
                cnt += 1

    return cnt

year = 0
while True:
    pieces = count_pieces(graph, n, m)
    
    if pieces >= 2:
        print(year)
        break
    elif pieces == 0:
        print(0)
        break

    graph = melt(graph, n, m)
    year += 1