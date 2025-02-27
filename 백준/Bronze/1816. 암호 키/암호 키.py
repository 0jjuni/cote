import sys

N = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline()) for _ in range(N)]


for num in num_list:
    for i in range(2, 1000001):
        if num % i == 0:
            print('NO')
            break
        if i == 1000000:
            print('YES')