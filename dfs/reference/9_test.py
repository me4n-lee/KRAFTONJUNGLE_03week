import sys
input = sys.stdin.readline

def dfs(graph, start, visit, inout):
    cnt = 0
    stack = []

    if inout[start] == 0:
        return 0

    stack.append(start)

    while stack:
        place = stack.pop()

        if visit[place] == 0:
            visit[place] = 1

            for new_place in graph[place]:
                if visit[new_place] == 0:
                    if inout[new_place] == 1:
                        cnt += 1
                    elif inout[new_place] == 0:
                        stack.append(new_place)
                else:
                    continue
        elif visit[place] == 1:
            continue

    return cnt

n = int(input())
a_list = list(map(int, input().strip()))

graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

inout = [0] *(n+1)
for i in range(len(a_list)):
    inout[i+1] = a_list[i]

# 서브태스크 3의 조건을 확인하고 이에 따라 시작점을 선택합니다.
indoor_count = sum(a_list)
start_points = [i+1 for i in range(n)] if indoor_count > 2 else [i+1 for i, x in enumerate(a_list) if x == 1]

total = 0
for i in start_points:
    visit = [0] * (n+1)
    result = dfs(graph, i, visit, inout)
    total += result

print(total)
