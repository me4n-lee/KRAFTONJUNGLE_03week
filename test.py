

from collections import deque
import sys
input = sys.stdin.readline


m, n, h = map(int, input().split())

graph = []

for _ in range(h):
    graph_sub = []
    for i in range(n):
        a = list(map(int, input().split()))
        graph_sub.append(a)
    graph.append(graph_sub)

da = [1, -1, 0, 0, 0, 0]
db = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

def bfs(n, m, h): #h가 첫번째, n이 두번째, m이 세번째

    que = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    que.append([i, j, k])

    while que:
        a, b, c = que.popleft() # a = h / b = n / c = m

        for i in range(6):
            na = a + da[i]
            nb = b + db[i]
            nc = c + dc[i]

            if 0 <= na < h and 0 <= nb < n and 0 <= nc < m and graph[na][nb][nc] == 0:
                graph[na][nb][nc] = graph[a][b][c] + 1
                que.append([na, nb, nc])

    result = 0
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                #만약 그래프에 아직도 0이 남아있다면 전부 다 익지 않았다는 의미!
                if graph[i][j][k] == 0:
                    return -1
                result = max(result, graph[i][j][k])

    ans = result - 1 #문제 설정에서 처음 1은 0일차이기에, 일수를 구하기 위해서는 1을 빼줘야 한다.

    return ans

result = bfs(n, m, h)

print(result)