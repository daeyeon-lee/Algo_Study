def backtracking(start,len):
    if len == M:
        print(*ans)
        return
    for i in range(start,N+1):
        ans.append(i)
        backtracking(i,len+1)
        ans.pop() # 선택을 되돌리고 다른 선택지로 가기

N, M = map(int,input().split())
ans = []

backtracking(1,0)