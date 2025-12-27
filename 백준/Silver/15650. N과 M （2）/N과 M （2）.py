def backtracking(num, len):
    if len == M:
        print(*ans)
        return

    for i in range(1,N+1):
        if not visited[i] and i > num:
            visited[i] = True
            ans.append(i)

            backtracking(i, len+1)

            ans.pop()
            visited[i] = False



N, M = map(int,input().split())
ans = []
visited = [False] * (N+1)
backtracking(0,0)