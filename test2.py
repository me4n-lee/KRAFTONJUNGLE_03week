#https://www.acmicpc.net/problem/1388
#바닥 장식
#1388

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

visit = [[0] * m for _ in range(n)]
count = [[1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b):
    que = deque()
    que.append((a,b))
    visit[a][b] = 1

    while que:
        x, y = que.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[x][y] == '|':
                    if graph[nx][ny] == '|':
                        visit[nx][ny] = 1
                        count[nx][ny] = 0
                        que.append((nx, ny))
                else:
                    visit[nx][ny] = 1
                    que.append((nx, ny))

        for i in range(2, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if graph[x][y] == '-':
                    if graph[nx][ny] == '-':
                        visit[nx][ny] = 1
                        count[nx][ny] = 0
                        que.append((nx, ny))
                else:
                    visit[nx][ny] = 1
                    que.append((nx, ny))


    return

dfs(0,0)

print(visit)
print(count)

print(sum(sum(count)))