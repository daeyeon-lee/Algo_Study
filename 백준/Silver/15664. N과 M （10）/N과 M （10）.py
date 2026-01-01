def backtracking(start, len):
    if len == M:
        print(*ans)
        return

    remember = 0
    for i in range(start, N):
        if not visited[i] and remember != nums[i]:
            ans.append(nums[i])
            remember = nums[i]
            visited[i] = True

            backtracking(i+1, len+1)

            ans.pop()
            visited[i] = False


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited = [False] * N
ans = []
backtracking(0,0)