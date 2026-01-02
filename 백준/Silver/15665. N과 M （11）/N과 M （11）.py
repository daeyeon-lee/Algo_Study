def backtracking(len):
    if len == M:
        print(*ans)
        return
    remember = 0
    for i in range(N):
        if remember != nums[i]:
            ans.append(nums[i])
            remember = nums[i]

            backtracking(len+1)

            ans.pop()



N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans = []

backtracking(0)