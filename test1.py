import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    first, last, cost = map(int, input().split())
    graph[first].append((cost, last))

start, end = map(int, input().split())

print(graph)

inf = sys.maxsize
visit = [inf] * (n+1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    visit[start] = 0

    while heap:
        cost, city = heapq.heappop(heap)

        if visit[city] < cost:
            continue

        for value in graph[city]:
            new_cost = cost + value[0]

            if new_cost < visit[value[1]]:
                visit[value[1]] = new_cost
                heapq.heappush(heap, (new_cost, value[1]))

dijkstra(start)

print(visit[end])