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
count = [[1] * m for _ in range(n)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a,b):
    
    stack = []
    stack.append((a,b))
    visit[a][b] = 1

    while stack:
        x, y = stack.pop()

        for i in range(2):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[x][y] == '|':
                    if graph[nx][ny] == '|':
                        visit[nx][ny] = 1
                        count[nx][ny] = 0
                        stack.append((nx,ny))
                        
                else:
                    visit[nx][ny] = 1
                    stack.append((nx,ny))


        for i in range(2,4):
        
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[x][y] == '-':
                    if graph[nx][ny] == '-':
                        visit[nx][ny] = 1
                        count[nx][ny] = 0
                        stack.append((nx,ny))
                    
            else:
                visit[nx][ny] = 1
                stack.append((nx,ny))


    return

dfs(0,0)

print(visit)
print(count)

print(sum(sum(count)))

#         if graph[x][y] == '-':
#             if y + 1 < m and graph[x][y + 1] == '-' and visit[x][y + 1] == 0:
#                 dfs(x, y + 1)
        
#         elif graph[x][y] == '|':
#             if x + 1 < n and graph[x + 1][y] == '|' and visit[x + 1][y] == 0:
#                 dfs(x + 1, y)

# count = 0
# for i in range(n):
#     for j in range(m):
#         if visit[i][j] == 0:
#             count += 1
#             dfs(i, j)

# print(count)