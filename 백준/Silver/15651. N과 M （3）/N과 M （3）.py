def backtracking(len):
    if len == M:
        print(*ans)
        return
    for i in range(1,N+1):
        ans.append(i)
        visited[i] = True
        backtracking(len+1)

        ans.pop()
        visited[i] = False



N, M = map(int,input().split())
ans = []
visited = [False] * (N+1)
backtracking(0)