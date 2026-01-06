def backtracking(start,depth):
    global cnt
    if depth > 0 and sum(ans) == S: # 공집합도 합이 0이라 방지
        cnt += 1

    for i in range(start,N):
        ans.append(nums[i])

        backtracking(i+1,depth+1)

        ans.pop()


N, S = map(int,input().split())
nums = list(map(int,input().split()))
ans = []
cnt = 0
backtracking(0,0)
print(cnt)
