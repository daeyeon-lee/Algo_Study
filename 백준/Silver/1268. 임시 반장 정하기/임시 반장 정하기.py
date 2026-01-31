N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = [0] * N
for i in range(N): # i번째 학생
    for j in range(N): # 나머지 학생과 비교
        if i == j:
            continue
        for k in range(5): # 학년
            if arr[i][k] == arr[j][k]:
                cnt[i] += 1
                break # 같은 반 한 적 있으면 다른 학년 볼 필요 없이 끝

ans = []
best = max(cnt)
for i in range(N):
    if cnt[i] == best:
        ans.append(i+1)
    elif cnt[i] > best:
        ans = [i+1]

ans.sort()
print(ans[0])