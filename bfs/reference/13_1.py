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

visit = [0][0] * n*m

print(visit)

dx = [1,-1] #오른쪽 왼쪽
dy = [1,-1] #아래 위

def bfs(graph, start, visit, cnt):

    que = deque([start])
    visit[start] = 1

    while que:
        start = que.popleft()
        cnt += 1

        for i in range(n):
            for j in range(m):
                
                # if graph[i][j] == 0:
                    
                # 오른쪽으로 갔을때 
                if start + dx[0] == visit and visit == 0:
                    que.append()
                    visit[start + dx[0]] = 1
                    bfs(graph, [start + dx[0]], visit, cnt)

                # 왼쪽으로 갔을때
                elif start + dx[1] == visit and visit == 0:
                    que.append()
                    visit[start + dx[1]] = 1
                    bfs(graph, [start + dx[1]], visit, cnt)

                # 아래로 갔을때
                elif start + dy[0] == visit and visit == 0:
                    que.append()
                    visit[start + dy[0]] = 1
                    bfs(graph, [start + dy[0]], visit, cnt)

                # 위로 갔을떄
                elif start + dy[1] == visit and visit == 0:
                    que.append()
                    visit[start + dy[1]] = 1
                    bfs(graph, [start + dy[1]], visit, cnt)


# def bfs(graph, start, visit):

#     que = deque([start])
#     visit[start] = 1

#     while que:
#         v = que.popleft()
#         print(v, end=' ')
    
#         for i in graph[v]:
#             if visit[i] == 0:
#                 que.append(i)
#                 visit[i] = 1

# 상하좌우

#오른쪽으로 갔을때
#왼쪽으로 갔을때
#아래로 갔을때
#위로 갔을떄

