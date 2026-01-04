def backtracking(depth,start):
    if depth == 6:
        print(*ans)
        return
    for i in range(start,arr[0]+1):
        ans.append(arr[i])

        backtracking(depth+1, i+1)
        ans.pop()



while True:
    arr = list(map(int,input().split()))
    if arr == [0]:
        break
    ans = []
    backtracking(0,1)
    print()