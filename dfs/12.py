#https://www.acmicpc.net/problem/2617
#구슬 찾기
#2617

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

max_graph = [[] for _ in range(n+1)]
min_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a , b = map(int, input().split())
    max_graph[a].append(b)
    min_graph[b].append(a)

# print(max_graph)
# print(min_graph)

# visit = [0] * (n+1)
count = [0] * (n+1)

def dfs(graph, start, visit):

    stack = []
    stack.append((start))
    check = []

    while stack:
        value= stack.pop()


        if visit[value] == 0:
            visit[value] = 1

        for node in graph[value]:
            if visit[node] == 0:
                visit[node] = 1
                check.append(node)
                stack.append(node)

        # print(check)
        # print(stack)

    return check

min_count = 0
max_count = 0

for i in range(n):

    visit = [0] * (n+1)
    result = dfs(min_graph, i+1, visit)
    # print(len(result))

    if len(result) >= (n+1)/2:
        min_count +=1

# print(min_count)

for i in range(n):

    visit = [0] * (n+1)
    result = dfs(max_graph, i+1, visit)
    # print(len(result))

    if len(result) >= (n+1)/2:
        max_count +=1

# print(max_count)

answer = min_count + max_count

print(answer)