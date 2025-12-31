def backtracking(len):
    if len == M:
        print(*ans)
        return
    remember = 0 # 중복 순열 방지를 위해 같은 값이 또 나오지 않도록 remeber에 저장
    for i in range(N):
        if not visited[i] and remember != nums[i]:
            ans.append(nums[i])
            visited[i] = True # 했던 값을 또 쓰지 않도록 방문처리
            remember = nums[i] # 동일한 값이 또 나오지 않도록 remember에 저장
            backtracking(len+1)

            ans.pop()
            visited[i] = False


N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited = [False] * N
ans = []
backtracking(0)