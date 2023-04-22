#https://www.acmicpc.net/problem/1260
#DFS와 BFS
#1260

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

#인접리스트 구현
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# print(graph)


dfs_result = []
bfs_result = []

def dfs(graph, v, visit):
    global dfs_result

    visit[v] = 1
    dfs_result.append(v)

    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, i, visit)

def bfs(graph, start, visit):
    global bfs_result

    que = deque([start])
    visit[start] = 1

    while que:
        v = que.popleft()
        bfs_result.append(v)
    
        for i in graph[v]:
            if visit[i] == 0:
                que.append(i)
                visit[i] = 1


visit = [0] * (n+1)
dfs(graph, v, visit)
# print(dfs_result)
for i in range(len(dfs_result)):
    print(dfs_result[i], end=' ')

print()

visit = [0] * (n+1)
bfs(graph, v, visit)
# print(bfs_result)
for i in range(len(bfs_result)):
    print(bfs_result[i], end=' ')