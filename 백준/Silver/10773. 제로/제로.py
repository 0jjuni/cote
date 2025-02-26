import sys

K = int(sys.stdin.readline())
stack = []
result = 0

for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for i in stack:
    result+= i
print(result)