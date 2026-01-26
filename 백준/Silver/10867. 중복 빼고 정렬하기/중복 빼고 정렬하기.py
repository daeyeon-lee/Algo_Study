N = int(input())
nums = set(map(int,input().split()))


ans = []
for num in nums:
    ans.append(num)
ans.sort()
print(*ans)