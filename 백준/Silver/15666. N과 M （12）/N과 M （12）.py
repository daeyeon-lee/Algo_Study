def backtracking(start,len):
    if len == M:
        print(*ans)
        return
    remember = 0
    for i in range(start,N):
        if remember != nums[i]:
            remember = nums[i]
            ans.append(nums[i])

            backtracking(i,len+1)

            ans.pop()


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
backtracking(0,0)