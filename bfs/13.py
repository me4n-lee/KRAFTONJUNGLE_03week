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

# print(graph)

dx = [1, -1, 0, 0]  # 오른쪽 왼쪽
dy = [0, 0, 1, -1]  # 아래 위

# visit = [[0] * m for _ in range(n)]

# print(visit)

# print(cnt)

def bfs(x,y):

    que = deque()
    que.append([x,y]) #?

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #i=1 / 오른쪽
            #i=2 / 왼쪽
            #i=3 / 아래
            #i=4 / 위

            #행렬 외부로 가는곳은 전부다 안됨
            if nx<0 or nx>= n or ny<0 or ny>=m:
                continue
            
            #0인곳은 안됨
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                #cnt를 따로 설정 안하고, 그 그래프에데가 이전 그래프의 값을 넣어주는거임
                graph[nx][ny] = graph[x][y] + 1
                que.append([nx,ny])

    return graph[n-1][m-1]

print(bfs(0,0))