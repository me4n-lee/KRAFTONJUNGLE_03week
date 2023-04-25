#https://www.acmicpc.net/problem/2606
#바이러스
#2606

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visit = [0] * (n+1)

def dfs(graph, start, visit, count):

    stack = []
    stack.append(start)
    visit[start] = 1

    while stack:
        root = stack.pop()

        for node in graph[root]:

            if visit[node] == 0:
                visit[node] = 1
                count += 1
                stack.append(node)

            if visit[node] == 1:
                continue
    
    return count

result = dfs(graph, 1, visit, 0)

print(result)