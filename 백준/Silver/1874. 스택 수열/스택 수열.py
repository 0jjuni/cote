import sys

n = int(sys.stdin.readline())
stack = []
result = []
num_list = [int(sys.stdin.readline()) for _ in range(n)]

num = 1

for i in num_list:
    while i >= num:
        result.append('+')
        stack.append(num)
        num += 1

    if stack and stack[-1] == i:
        result.append('-')
        stack.pop()
    else:
        result = ['NO']
        break


print(*result, sep='\n')