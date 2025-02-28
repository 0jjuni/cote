import sys

N = int(sys.stdin.readline())

result = 0

for A in range(1, N+1):
    for B in range(1, N+1):
        C = N - A - B
        if A + B + C == N:
            if A >= B + 2:
                if C % 2 == 0 and C > 0:
                    result +=1

print(result)