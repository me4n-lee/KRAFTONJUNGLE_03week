#https://www.acmicpc.net/problem/18405
#경쟁적 전염
#18405

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(int,input().split()))
    graph.append(a)

print(graph)

s, x, y = map(int, input().split())

visit = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph):

    que = deque()
    # que.append((a,b))

    for i in range(k):
        for a in range(n):
            for b in range(n):
                if graph[a][b] == i:
                    que.append((a,b))

    while que:
        x, y = que.popleft()
        visit[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    que.append((nx, ny))

    return graph

print(dfs(graph))
