#https://www.acmicpc.net/problem/2573
#빙산
#2573

import sys
input = sys.stdin.readline

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
            ny = y + dy[i] # 2일때 오른쪽, 3일때 왼쪽
        

            if land[nx][ny] == 0:
                graph[x][y] -= 1
                if graph[x][y] < 0:
                    graph[x][y] = 0
            else:
                continue

    # print(stack)
    # print(graph)
    # print(land)
    return land

da = [1, -1, 0, 0] #위아래
db = [0, 0, 1, -1] #오른쪽왼쪽

def dfs(land, n, m, visit):

    visit_stack = []
    value = 0

    for x in range(n):
        for y in range(m):
            if land[x][y] == 1 and visit[x][y] == 0:
                value += 1  # 대륙을 발견할 때마다 value를 증가시킵니다.
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

    return value

year = 0
while True:
    # 빙산 녹는 과정
    land = [[0] * m for _ in range(n)]
    conti = continent(graph, land, n, m)

    # 대륙 개수 계산
    visit = [[0] * m for _ in range(n)]
    answer = dfs(conti, n, m, visit)

    # 대륙이 분열되었는지 확인
    if answer > 1:
        print(year)
        break

    # 빙산이 모두 녹았는지 확인
    if sum(sum(row) for row in graph) == 0:
        print(0)
        break

    year += 1

    # for i in range(n):
    #     for j in range(m):
    #         if land[i][j] == 1:
    #             visit_stack.append((x,y))

    # while visit_stack:

    #     for i in range(4):

    #         a, b = visit_stack.pop()

    #         na = a + da[i] # 0일때 아래로, 1일때 위로
    #         nb = b + db[i] # 2일때 오르쪽, 3일때 왼쪽

    #         if 0 <= x < n and 0 <= y < m:
    #             if land[na][nb] == 1:
    #                 visit[na][nb] = 1
    #                 visit_stack.append((na,nb))
    #         else:
    #             continue

# land= [[0] * m for _ in range(n)]
# conti = continent(graph, land, n, m)
# visit= [[0] * m for _ in range(n)]
# answer = dfs(conti, n, m, visit)
# print(conti)
# print(answer)

#visit 초기화를 자꾸 이상하게 하고있어서 문제가 안풀렸다...