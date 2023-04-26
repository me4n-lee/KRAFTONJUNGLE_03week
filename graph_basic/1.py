#https://www.acmicpc.net/problem/1991
#트리 순회
#1991

import sys
input = sys.stdin.readline

n = int(input())

tree = {}
for _ in range(n):
    a, b, c = input().split()
    tree[a] = b, c

print(tree)

def LAB(root):

    if root != '.':
        print(root, end='')
        LAB(tree[root][0])
        LAB(tree[root][1])

def ALB(root):

    if root != '.':
        ALB(tree[root][0])
        print(root, end='')
        ALB(tree[root][1])

def ABL(root):

    if root != '.':
        ABL(tree[root][0])
        ABL(tree[root][1])
        print(root, end='')

LAB('A')
print()
ALB('A')
print()
ABL('A')

# sub_graph = []
# for _ in range(n):
#     a = list(map(str, input().split()))
#     sub_graph.append(a)

# print(sub_graph)

# graph = []
# for _ in range(n):
#     a = list(input().split())
#     graph.append(a)

# print(graph)