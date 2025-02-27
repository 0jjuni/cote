import sys
N = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().strip().split())

stack = []
result = [-1 for _ in range(N)]

for idx, num in enumerate(A):
    if not stack or (stack and stack[-1][-1] > num):
        stack.append((idx,num))
    
    else:
        while stack and stack[-1][-1] < num:
            result[stack[-1][0]] = num
            stack.pop()
        stack.append((idx,num))


print(*result)
