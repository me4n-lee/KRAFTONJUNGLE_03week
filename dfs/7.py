#https://www.acmicpc.net/problem/11725
#트리의 부모 찾기
#11725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # graph.sort([a])

# print(graph)

visit = [0] * (n+1)

def dfs(graph, start, visit):

    # visit[start] = 1

    for i in graph[start]:
        if visit[i] == 0:
            visit[i] = start  
            dfs(graph, i, visit)
        else:
            continue


    # print(visit)

dfs(graph, 1, visit)

for i in range(2,len(visit)):
    print(visit[i])


#pypy가 아닌 python으로 제출 해야지만 문제가 풀림
#재귀를 사용할땐 꼭 python을 활용하자.