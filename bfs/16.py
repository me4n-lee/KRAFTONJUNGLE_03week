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
    graph[first].append([cost, last])
start, end = map(int, input().split())

print(graph)

visit = [0] + (n+1)

def dijkstra(start):
    heap = []
    #튜플의 첫 번째 원소를 기준으로 최소 힙이 구성됩니다.
    heapq.heappush(heap, (start,0))
    visit[start]

    while heap:
        city, cost = heapq.heappop(heap)

        if visit[city] < cost:

        for n
    