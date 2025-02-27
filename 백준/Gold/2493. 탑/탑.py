import sys
N = sys.stdin.readline()
top = map(int, sys.stdin.readline().strip().split())


idx_st= []
stack = []
for idx, num in enumerate(top):
    while stack and stack[-1][-1] < num:
        stack.pop()

    if not stack: #stack에 아무것도 없을 때
        idx_st.append(0)
        stack.append((idx+1,num))
    
    elif stack[-1][-1] < num: # 새로들어오는 숫자가 기존스택보다 큰 경우
        idx_st.append(idx_st[-1])
        stack.append((idx+1,num))
    
    elif stack[-1][-1] > num:  # 새로들어오는 숫자가 기존스택보다 작은경우
        idx_st.append(stack[-1][0])
        stack.append((idx+1,num))


print(*idx_st)