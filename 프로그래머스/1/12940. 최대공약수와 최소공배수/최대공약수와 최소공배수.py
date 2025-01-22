
def solution(n, m):
    min_v = min(n, m)
    max_v = max(n, m)
    
    for i in range(min_v, 0, -1):
        if (max_v % i==0) & (min_v % i ==0):
            break
    if i:
        gcd = i
    else:
        gcd = 1
    
    if gcd==1:
        lcm = n * m
    else:
        lcm = int((n * m / gcd))
    
    return([gcd, lcm])
