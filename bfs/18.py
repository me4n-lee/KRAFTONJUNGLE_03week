from collections import deque
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

graph = []

for i in range(n):
    a = list(map(str, input().strip()))
    graph.append(a)

da = [1, -1, 0, 0]
db = [0, 0, 1, -1]

def bfs(n, c):
    D = []
    S_que = deque()
    W_que = deque()

    for i in range(n):
        for j in range(c):
            if graph[i][j] == 'S':
                S_que.append([i, j, 0])
            if graph[i][j] == '*':
                W_que.append([i, j])
            if graph[i][j] == 'D':
                D = [i, j]

    while S_que:

        for _ in range(len(W_que)):
            a, b = W_que.popleft()
            for i in range(4):
                na = a + da[i]
                nb = b + db[i]

                if na < 0 or na >= n or nb < 0 or nb >= c:
                    continue

                if graph[na][nb] == '.':
                    W_que.append([na, nb])
                    graph[na][nb] = '*'

        for _ in range(len(S_que)):
            x, y, cnt = S_que.popleft()

            if [x, y] == D:
                return cnt

            for i in range(4):
                nx = x + da[i]
                ny = y + db[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= c:
                    continue
                
                if graph[nx][ny] == '*':
                    continue

                if graph[nx][ny] == '.' or graph[nx][ny] == 'D':
                    S_que.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

    return "KAKTUS"

print(bfs(n, c))

#각 for 문은 현재 길이를 기준으로 돌기 떄문에, 처음엔 한번만 돈다.
#또는 append가 된만큼만돈다.
#