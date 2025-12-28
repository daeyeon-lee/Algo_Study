def backtracking(len):
    if len == M:
        print(*ans)
        return

    for i in range(N):
        if visited[i] == False:
            ans.append(nums[i])
            visited[i] = True
            backtracking(len+1)

            ans.pop()
            visited[i] = False
            
            


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

ans = []
visited = [False] * (N+1)
backtracking(0)