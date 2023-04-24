import sys
# input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().strip()))
print(a_list)

graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

inout = [0] * (n+1)
for i in range(len(a_list)):
    inout[i+1] = a_list[i]

def dfs(graph, start, visit, inout):
    cnt = 0
    stack = []
    
    if inout[start] == 0:  # 실외에서 시작할 수 없으므로
        return 0

    stack.append(start)

    while stack:
        place = stack.pop()

        if visit[place] == 0:  # 방문하지 않았다면
            visit[place] = 1

            if inout[place] == 1: # 실내라면
                cnt += 1

            for new_place in graph[place]:
                if visit[new_place] == 0:
                    stack.append(new_place)

        elif visit[place] == 1:
            continue

    return cnt

sum = 0
for i in range(n):
    visit = [0] * (n+1)  # 반복문 내부에서 visit 배열 초기화
    result = dfs(graph, i+1, visit, inout)
    sum += result

print(sum)