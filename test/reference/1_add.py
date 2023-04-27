#https://www.acmicpc.net/problem/1388
#바닥 장식
#1388

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph =[]
for _ in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

print(graph)

visit = [[0] * m for _ in range(n)]
count = [[0] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a,b):

    stack = []
    # visit[a][b] == 1
    stack.append((a,b))

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue 

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:

                if graph[x][y] == "-":
                    if graph[nx][ny] == "-":
                        count[nx][ny] = 1
                        stack.append((nx,ny))
                    else:
                        count[nx][ny] = 0
                        stack.append((nx,ny))
                elif graph[nx][ny] == "|":
                    if graph[nx][ny] == "|":
                        count[nx][ny] = 0
                        stack.append((nx,ny))
                    else:
                        count[nx][ny] = 1
                        stack.append((nx,ny))
                        
                    # if graph[nx][ny] == graph[a][b]:
                    #     visit[nx][ny] = 1
                    #     count[nx][ny] = count[a][b]
                    #     stack.append((nx,ny))

                    # elif graph[nx][ny] != graph[a][b]: 
                    #     visit[nx][ny] = 1
                    #     count[nx][ny] = count[a][b] + 1
                    #     stack.append((nx,ny))

            if visit[nx][ny] == 1:
                continue

dfs(0,0)
print(count)