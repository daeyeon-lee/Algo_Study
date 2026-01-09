N = int(input())
nums = set()
for _ in range(N):
    nums.add(int(input()))


# x + y + z = k 일 때, x + y = k - z 임을 이용
two_sums = set()
# (x+y) 가능한 모든 합을 미리 저장
for i in nums:
    for j in nums:
        two_sums.add(i+j)


max_sum = 0
ans=[]
# i-j가 two_sums에 들어가는지 확인
for i in nums:
    for j in nums:
        if (i-j) in two_sums:
            ans.append(i)
print(max(ans))