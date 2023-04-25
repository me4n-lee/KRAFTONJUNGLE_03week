#https://www.acmicpc.net/problem/14888
#연산자 끼워넣기
#14888

import sys
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

math_list = list(map(int, input().split()))

print(n_list)
print(math_list)

visit = [0] * (n+1)

#math_list = [a,b,c,d]

result = []

def dfs(n_list, math_list, start, visit):

    stack = []
    stack.append(n_list[start])

    while stack:
        number = stack.pop()

        for i in range(n):

            if math_list[i] != 0:

                if i == 0:
                    math_list[0] = math_list[0] - 1
                    total = start + number
                    stack.append(total)

                elif i == 1:
                    math_list[1] = math_list[1] -1
                    total = start - number
                    stack.append(total)

                elif i == 2:
                    math_list[2] = math_list[2] -1
                    total = start * number
                    stack.append(total)

                elif i == 3:
                    math_list[3] = math_list[3] -1
                    total = start / number
                    stack.append(total)

            else:
                result.append(number)

            print(math_list)
            print(result)




dfs(n_list, math_list, 0, visit)