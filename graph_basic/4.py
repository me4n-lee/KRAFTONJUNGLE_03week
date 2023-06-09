#https://www.acmicpc.net/problem/1260
#DFS와 BFS
#1260

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# print(graph)

# visit = [0] * (n+1)

def dfs(graph, v, visit):

    visit[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, i, visit)

def bfs(graph, start, visit):

    que = deque([start])
    visit[start] = 1

    while que:
        v = que.popleft()
        print(v, end=' ')
    
        for i in graph[v]:
            if visit[i] == 0:
                que.append(i)
                visit[i] = 1

visit = [0] * (n+1)
dfs(graph, v, visit)
print()
visit = [0] * (n+1)
bfs(graph, v, visit)
