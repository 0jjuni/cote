import sys

num_list = list(map(int, sys.stdin.readline().split()))
result = 0

for x in range(-999,1000):
    for y in range(-999,1000):
        if num_list[0] * x + num_list[1] * y == num_list[2] and num_list[3] * x + num_list[4] * y == num_list[5]:
            print(x, y)
            break
    

