import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = []
for _ in range(n):
    m_list = list(map(int, input().split()))
    graph.append(m_list)

visit = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]  # 위아래
dy = [0, 0, 1, -1]  # 오른쪽왼쪽

def melt(graph, n, m):
    new_graph = [[0] * m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0:
                cnt = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        cnt += 1
                new_graph[x][y] = max(graph[x][y] - cnt, 0)
    return new_graph

def dfs(graph, n, m, visit, x, y):
    visit[x][y] = 1
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and visit[nx][ny] == 0:
            dfs(graph, n, m, visit, nx, ny)

def count_land(graph, n, m):
    visit = [[0] * m for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] != 0 and visit[x][y] == 0:
                count += 1
                dfs(graph, n, m, visit, x, y)
    return count

year = 0
while True:
    land = count_land(graph, n, m)
    if land >= 2:
        print(year)
        break
    elif land == 0:
        print(0)
        break
    else:
        graph = melt(graph, n, m)
        year += 1
