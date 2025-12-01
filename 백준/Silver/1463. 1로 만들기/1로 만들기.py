X = int(input())
dp = [0] * (X+1)

for i in range(2,X+1):
    dp[i] = dp[i-1] + 1 # 1을 뺴는 경우 기본으로 dp에 저장
    if i % 2 == 0: # 2로 나누었을 때 1로 빼는 거와 비교했을 때 더 작은 값을 dp에 갱신
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # 3으로 나누었을 때 1로 빼는 거와 비교했을 때 더 작은 값을 dp에 갱신
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[X])
