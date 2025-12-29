def backtracking(len):
    if len == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(nums[i])
        backtracking(len+1)
        ans.pop()

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = []
backtracking(0)