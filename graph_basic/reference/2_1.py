import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []
while True:
    try:
        a = int(input())
        graph.append(a)
    except:
        break

def LAB_tree_diction(graph):
    if not graph:
        return None

    root = graph[0]

    # 왼쪽 하위 트리와 오른쪽 하위 트리로 나눈다.
    left_subtree = [x for x in graph if x < root]
    right_subtree = [x for x in graph if x > root]

    left = LAB_tree_diction(left_subtree)
    right = LAB_tree_diction(right_subtree)

    return {"root": root, "left": left, "right": right}

def ABL(tree):
    result = []
    if tree:
        result.extend(ABL(tree["left"]))
        result.extend(ABL(tree["right"]))
        result.append(tree["root"])
    return result           

###########################################################

tree = LAB_tree_diction(graph)
result_list = ABL(tree)

for i in range(len(result_list)):
    print(result_list[i])