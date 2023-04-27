#https://www.acmicpc.net/problem/1388
#바닥 장식
#1388

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

visit = [[0] * m for _ in range(n)]

def dfs(x, y):
    visit[x][y] = 1
    if graph[x][y] == '-':
        if y + 1 < m and graph[x][y + 1] == '-' and visit[x][y + 1] == 0:
            dfs(x, y + 1)
    elif graph[x][y] == '|':
        if x + 1 < n and graph[x + 1][y] == '|' and visit[x + 1][y] == 0:
            dfs(x + 1, y)

count = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)