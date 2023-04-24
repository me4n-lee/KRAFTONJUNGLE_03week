#https://www.acmicpc.net/problem/3055
#탈출
#3055

from collections import deque
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

graph = []

for i in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

print(graph)

# n 첫번째
# c 두번째

#고슴도치는 물이 찰 예정인 칸으로 이동할수 없다. 즉, 물이 먼저차고 고슴도치가 이동한다

da = [1, -1, 0, 0] #첫번째를 바꿈
db = [0, 0, 1, -1] #두번째를 바꿈

dx = [1, -1, 0, 0] #첫번째를 바꿈
dy = [0, 0, 1, -1] #두번째를 바꿈

def bfs(n, c):

    D = []
    S_que = deque() #고슴도치
    W_que = deque() #물

    for i in range(n):
        for j in range(c):

            if graph[i][j] == 'S':
                S_que.append([graph[i][j]])

            if graph[i][j] == '*':
                W_que.append([graph[i][j]])

            if graph[i][j] == 'D':
                D = [i,j]

    while S_que:

        a, b = W_que.popleft()
        
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]

        if na<0 or na>= n or nb<0 or nb>= c:
            continue

        if graph[na][nb] == '.':
            W_que.append([na,nb])
            graph[na][nb] = 'X'

        x, y = S_que.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= n or ny<0 or ny>= c:
                continue

            if graph[nx][ny] == 'X':
                continue

            if graph[nx][ny] == '.':
                W_que.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1
            
    return graph[D]


print(bfs(n, c))