#https://www.acmicpc.net/problem/11724
#연결 요소의 개수
#11724

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # graph.sort(b)

# print(graph) 

visit = [0] * (n+1)

def bfs(graph, start, visit):
    
    que = deque()
    que.append(start)

    if visit[start] == 1:
        return 0

    else:
        while que:
            root = que.popleft()
            for node in graph[root]:
                if visit[node] == 0:
                    visit[node] = 1
                    que.append(node)

                if visit[node] == 1:
                    continue
        
        return 1
    
result = [0] * (n+1)
for i in range(1, n+1):
    result[i] = bfs(graph, i, visit)

answer = sum(result)

print(answer)