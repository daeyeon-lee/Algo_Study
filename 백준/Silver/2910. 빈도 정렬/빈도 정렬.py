N, C = map(int,input().split())
nums = list(map(int,input().split()))

set_nums = []
for i in range(N):
    if nums[i] in set_nums:
        continue
    else:
        set_nums.append(nums[i])


cnt_v = {}
for num in nums:
    cnt_v[num] = cnt_v.get(num,0) + 1

cnt_v_sorted = sorted(cnt_v.items(), key = lambda x : x[1], reverse= True)


ans = []
for num, cnt in cnt_v_sorted:
    if num in set_nums:
        for _ in range(cnt):
            ans.append(num)
print(*ans)
