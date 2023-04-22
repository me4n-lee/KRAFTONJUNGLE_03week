#https://www.acmicpc.net/problem/18352
#특정 거리의 도시 찾기
#18352

from collections import deque
import sys
input = sys.stdin.readline

# n = 도시개수 / m = 도로개수 / k = 거리 정보 / x = 출발도시 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].sort()

# print(graph)

# visit = [0] * n*n
visit = [-1] * (n+1)

def bfs(graph, start, visit, k):

    result = []
    
    que = deque()
    que.append(start)
    visit[start] = 0
    
    while que:
        start = que.popleft()

        for i in graph[start]:
            if visit[i] == -1:
                que.append(i)
                visit[i] = visit[start] + 1
        
            if visit[i] == k:
                result.append(i)

    return result

result = bfs(graph, x, visit, k)

# if ans:
#     for i in range(len(ans)):
#         print(ans[i])
# else:
#     print(-1) 

# print(visit)

ans = sorted(result)  # 정렬

if ans:
    for i in ans:
        print(i)
else:
    print(-1)