import sys

N = int(sys.stdin.readline())
pred = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (a == b) or (b == c) or (a == c):
                continue
            cnt = 0
            for num, st, ball in pred:
                ball_cnt, st_cnt = 0, 0
                

                x = num // 100
                y = (num % 100) // 10
                z = num % 10

                
                if a == x:
                    st_cnt += 1
                if b == y:
                    st_cnt += 1
                if c == z:
                    st_cnt += 1

                if a == y or a == z:
                    ball_cnt += 1
                if b == x or b ==z:
                    ball_cnt += 1
                if c == x or c == y:
                    ball_cnt += 1


                
                if ball == ball_cnt and st == st_cnt:
                    cnt += 1

            if cnt == N:
                answer += 1

print(answer)