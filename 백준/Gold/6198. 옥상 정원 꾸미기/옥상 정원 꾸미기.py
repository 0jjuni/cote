import sys

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
stack = []

for i in num_list:
    if not stack or stack[-1] > i:
        stack.append(i)
    else:
        while stack and stack[-1] <= i: #새로들어올값이 기존 스택보다 큰경우
            stack.pop()
            result += len(stack)
        stack.append(i)

if stack:
    while stack and stack[-1] < float('inf'):
        stack.pop()
        result += len(stack)

print(result)