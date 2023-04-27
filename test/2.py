#https://www.acmicpc.net/problem/2667
#단지번호붙이기
#2667

n = int(input())

graph = []
for _ in range(n):
    a = list(map(int, input().strip()))
    graph.append(a)

# print(graph)

visit = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

house = []

def dfs(graph, visit):

    stack = []
    # visit[a][b] == 1
    # stack.append((a,b))
    value = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visit[i][j] == 0:
                value += 1  # 대륙을 발견할 때마다 value를 증가시킵니다.
                house_count = 0
                stack.append((i, j))
                visit[i][j] = 1

                while stack:
                    x, y = stack.pop()

                    for k in range(4):

                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                            if graph[nx][ny] == 1:
                                visit[nx][ny] = 1
                                house_count += 1
                                stack.append((nx,ny))

                house.append(house_count)
                # print(house)

    return value



print(dfs(graph, visit))
house.sort()
for i in range(len(house)):
    print(house[i])
    

# print(visit)
