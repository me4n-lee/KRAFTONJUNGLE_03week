#https://www.acmicpc.net/problem/21606
#아침 산책
#21606

import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().strip()))
# print(a_list)

graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

# visit = [0] * (n+1)

inout = [0] *(n+1)
for i in range(len(a_list)):
    inout[i+1] = a_list[i]

# print(inout)

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

            for new_place in graph[place]:
                
                if visit[new_place] == 0:#대체 이걸 왜 생각 못했지??

                    if inout[new_place] == 1: # 실내라면
                        cnt += 1

                    elif inout[new_place] == 0: #실외라면
                        stack.append(new_place)
                
                else:
                    continue

        elif visit[place] == 1: #방문했다면
            continue

    return cnt

sum = 0
for i in range(n):

    visit = [0] * (n+1)

    result = dfs(graph, i+1, visit, inout)
    sum += result
    # print(result)

print(sum)