#https://www.acmicpc.net/problem/1916
#최소비용 구하기
#1916

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    
start, end = map(int, input().split())

# print(graph)

# visit = [0] * (n+1)

result = [[] for _ in range(n+1)]

def dijkstra(graph, start, end):
    result = [float('INF')] * (n+1)
    # result[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))    

    while heap:
        dist, root = heapq.heappop(heap)

        #루트가 end라면 끝내버리고 다시 while문을 돌림 / 시간아끼기
        if root == end:
            break

        for range, node in graph[root]:
            new_dist = dist + range

            #더 작은값만 추가해 주기 위해서. 더 작다면 그 노드에 new_dist를 추가해줌
            if new_dist < result[node]:
                result[node] = new_dist
                heapq.heappush(heap, (new_dist, node))
            
            # print(heap)
    return result[end]

answer = dijkstra(graph, start, end)

print(answer)
