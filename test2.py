#https://www.acmicpc.net/problem/2665
#미로만들기
#2665

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    first, last, cost = map(int, input().split())
    # graph[first].append([last, cost])
    graph[first].append((cost, last))

start, end = map(int, input().split())

# print(graph)

inf = sys.maxsize
visit = [inf] * (n+1)

def dijkstra(start):
    stack = []
    #튜플의 첫 번째 원소를 기준으로 최소 힙이 구성됩니다.
    stack.append((0, start))
    visit[start] = 0

    while stack:
        cost, city = stack.pop()

        if visit[city] < cost:
            continue

        for value in graph[city]:
            new_cost = cost + value[0]

            if new_cost < visit[value[1]]:
                visit[value[1]] = new_cost
                stack.append((new_cost, value[1]))

dijkstra(start)

print(visit[end])