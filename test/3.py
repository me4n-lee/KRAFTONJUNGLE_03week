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

# print(graph)

s, x, y = map(int, input().split())

visit = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

time = [[0] * n for _ in range(n)]

def bfs(graph):

    que = deque()
    # que.append((a,b))

    for i in range(1, k+1):
        for a in range(n):
            for b in range(n):
                if graph[a][b] == i:
                    que.append((a,b))
                    # que.append((a,b,0))
    while que:
        x, y = que.popleft()
        # x, y, second= que.popleft()
        
        # if second == s:
        #     break
        visit[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    time[nx][ny] = time[x][y] + 1
                    que.append((nx, ny))
                    # que.append((nx, ny, second + 1))

    return graph

result = bfs(graph)
# print(result)
# print(time)

#함수는 0부터 사직하기 떄문에!
ans_x = x-1
ans_y = y-1
if time[ans_x][ans_y] <= s:
    print(result[ans_x][ans_y])

else:
    print(0)
