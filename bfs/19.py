#https://www.acmicpc.net/problem/2294
#동전 2
#2294

from collections import deque
# import sys
# input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for _ in range(n):
    a = int(input())
    graph.append(a)

graph = sorted(list(set(graph)), reverse=True)

# print(graph)

def bfs(graph, start, k):
    
    visit = [0] * (k+1)
    que = deque()
    que.append(start)

    while que:
        
        total, count = que.popleft()

        if total == k:
            return count

        for i in range(len(graph)):
            coin = graph[i]
            sum = total + coin

            if sum <= k and visit[sum] == 0:
                # count += 1
                visit[sum] = 1
                que.append([sum,count + 1])

            elif sum > k:
                 continue

        # for i in range(len(graph)):
        #     coin = graph[i]

        #     if total + coin <= k and total + coin not in visit:
        #         # count += 1
        #         sum = total + coin
        #         visit.append(sum)
        #         que.append([sum,count + 1])

        #     if sum + coin >= k:
        #         continue

        # print(que)
        
    return -1

print(bfs(graph, [0,0], k))