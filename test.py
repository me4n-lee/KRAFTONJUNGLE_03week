#https://www.acmicpc.net/problem/2573
#빙산
#2573

import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    m_list = list(map(int, input().split()))
    graph.append(m_list)

# print(graph)

visit= [[0] * m for _ in range(n)]
land= [[0] * m for _ in range(n)]

# print(visit)

dx = [1, -1, 0, 0] #위아래
dy = [0, 0, 1, -1] #오른쪽왼쪽

#년수를 카운트 해야함

def continent(graph, land, n, m): #year

    stack = []
    # stack.append((a, b))
    visit_stack = []

    #1년이 지날때마다 0이 아닌곳을 주변의 상황에 따라 -1,-2,-3 해줘야함
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                stack.append((i,j))
                land[i][j] = 1
                
    while stack:
        
        x, y = stack.pop()
        # land[x][y] = 1

        visit[x][y] = 1

        for i in range(4):

            nx = x + dx[i] # 0일때 아래로, 1일때 위로
            ny = y + dy[i] # 2일때 오르쪽, 3일때 왼쪽
        

            if land[nx][ny] == 0:
                graph[x][y] -= 1
                if graph[x][y] < 0:
                    graph[x][y] = 0
            else:
                continue

    return land

# dfs(land, start,)

da = [1, -1, 0, 0] #위아래
db = [0, 0, 1, -1] #오른쪽왼쪽

def dfs(land, n, m, visit):

    visit_stack = []
    value = 0

    for x in range(n):
        for y in range(m):
            if land[x][y] == 1 and visit[x][y] == 0:
                visit_stack.append((x, y))
                visit[x][y] = 1

                while visit_stack:
                    a, b = visit_stack.pop()

                    for i in range(4):
                        na = a + da[i]
                        nb = b + db[i]

                        if 0 <= na < n and 0 <= nb < m and land[na][nb] == 1 and visit[na][nb] == 0:
                            visit[na][nb] = 1
                            visit_stack.append((na, nb))
                value += 1
    return value

land= [[0] * m for _ in range(n)]
visit= [[0] * m for _ in range(n)]
conti = continent(graph, land, n, m)
answer = dfs(conti, n, m, visit)
print(conti)
print(answer)