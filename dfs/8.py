#https://www.acmicpc.net/problem/1707
#이분 그래프
#1707

import sys
# input = sys.stdin.readline

k = int(input())

full_graph = []

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)
    full_graph.append(graph)

# print(full_graph)

# visit = [0] * (v+1)
# color = [0] * (v+1)

def dfs(graph, start, visit, colors): #color은 트리거 / 1은 1집합, -1은 2집합

    # for i in graph[start]:
    #     if visit[i] == 0:
    #         visit[i] = 1
    #         color[i] = color 
    #         dfs(graph, i, visit, -color)

    stack = [(start, 1)]
    
    while stack:
        
        node, color = stack.pop()

        if visit[node] == 0:
            visit[node] = 1
            colors[node] = color
            for value in graph[node]:
                stack.append((value, -color))
        
        #no가 나오는경우는 그전의 색과 같을때!
        elif colors[node] == -color: 
            return "NO"
        
        else:
            continue

    # print(visit)
    # print(colors)

    return "YES"

# for graph in full_graph:
#     v = len(graph) - 1
#     visit = [0] * (v+1)
#     colors = [0] * (v+1)

#     print(dfs(graph, 1, visit, colors))

for graph in full_graph:
    v = len(graph) - 1
    visit = [0] * (v+1)
    colors = [0] * (v+1)

    answer = "YES"

    #1에서만 체크하는게 아니라, 모든 점에서 만족하는지의 여부를 알아야 하기에,
    #for문을 활용해 모두 체크해준다
    for node in range(1, v+1):
        if visit[node] == 0:
            result =dfs(graph, node, visit, colors)
            if result == "NO":
                answer = "NO"
    
    print(answer)

#Bipartite Graphs는 tree나 even cycle일 때 성립된다.
#모든 노드에 대해서 탐색해야 하기떄문에, 1로 시작해선 안된다.
