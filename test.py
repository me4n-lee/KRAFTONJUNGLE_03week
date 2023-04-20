from collections import deque
def bfs(graph, v, visited, pred):
global result
q = deque([v])
# 현재 정점을 방문 처리
visited[v] = True
# 큐가 빌 때까지 반복
while q:
v = q.popleft()
result.append(v)
# 현재 정점의 인접 정점 모드 큐에 삽입, 방문
for i in range(7):
if graph[v][i] and (not visited[i]):
q.append(i)
visited[i] = True