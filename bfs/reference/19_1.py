#https://www.acmicpc.net/problem/2294
#동전 2
#2294

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for _ in range(n):
    a = int(input())
    graph.append([a,0])

graph.sort(reverse=True)

print(graph)

visit = []

def bfs(graph, start, k):
    visit = set()
    que = deque()
    que.append(start)

    while que:
        
        sum, count = que.popleft()

        if sum == k:
            return count

        for i in range(len(graph)):
            
            new_total = sum + graph[i]

            if new_total <= k and new_total not in visit:
                visit.add(new_total)
                que.append([new_total, count + 1])

            # if sum + graph[i][0] == k:
            #     graph[i][1] += 1
            #     break
            # elif sum + graph[i][0] >= k and len(graph) != 0:
            #     continue
            # elif sum + graph[i][0] <= k:
            #     graph[i][1] += 1
            #     que.append(new_total, count + 1)

    return -1

print(bfs(graph, [0,0], k))