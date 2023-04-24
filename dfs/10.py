#https://www.acmicpc.net/problem/14888
#연산자 끼워넣기
#14888

import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
math_list = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(n_list, math_list):
    global min_value, max_value

    stack = [(1, 
            n_list[0],
            math_list[0],
            math_list[1], 
            math_list[2], 
            math_list[3])]

    while stack:
        index, result, plus, minus, multiply, divide = stack.pop()

        if index == n:
            min_value = min(min_value, result)
            max_value = max(max_value, result)
        else:
            if plus:
                stack.append((index + 1,
                            result + n_list[index], 
                            plus - 1, 
                            minus, 
                            multiply, 
                            divide))
            if minus:
                stack.append((index + 1, 
                            result - n_list[index], 
                            plus,
                            minus - 1,
                            multiply, 
                            divide))
            if multiply:
                stack.append((index + 1, 
                            result * n_list[index], 
                            plus, minus, 
                            multiply - 1,
                            divide))
            if divide:
                stack.append((index + 1, 
                            int(result / n_list[index]), 
                            plus, 
                            minus, 
                            multiply, 
                            divide - 1))

dfs(n_list, math_list)

print(max_value)
print(min_value)