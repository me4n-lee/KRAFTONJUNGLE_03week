#https://www.acmicpc.net/problem/2178
#미로 탐색
#2178

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    a = list(map(int, input().strip()))
    graph.append(a)

print(graph)

visit = [[0] * m for _ in range(n)]

print(visit)

dx = [1, -1, 0, 0]  # 오른쪽 왼쪽
dy = [0, 0, 1, -1]  # 아래 위

def bfs(graph, start, visit, cnt):

    que = deque([start])
    x, y = start
    visit[x][y] = 1

    while que:
        x, y = que.popleft()
        cnt += 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            # 범위를 벗어나지 않는지 확인하고, 방문하지 않은 위치인지 확인합니다.
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and graph[nx][ny] == 1:
                que.append((nx, ny))
                visit[nx][ny] = 1
                cnt += 1

    return cnt

print(bfs(graph, [1,1], visit, 0))