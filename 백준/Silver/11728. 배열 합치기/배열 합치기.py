N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = []
for i in range(N):
    ans.append(A[i])
for j in range(M):
    ans.append(B[j])
ans.sort()
print(*ans)