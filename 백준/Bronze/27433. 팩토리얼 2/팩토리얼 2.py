def pactorial(N):
    if N == 0:
        return 1
    ans = 1
    for i in range(1,N+1):
        ans *= i
    return ans
N = int(input())
ans = pactorial(N)
print(ans)