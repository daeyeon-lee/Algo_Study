def backtracking(start,len):
    if len == M:
        print(*ans)
        return
    for i in range(start,N):
        ans.append(nums[i])
        backtracking(i, len+1)

        ans.pop()



N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = []
backtracking(0,0)