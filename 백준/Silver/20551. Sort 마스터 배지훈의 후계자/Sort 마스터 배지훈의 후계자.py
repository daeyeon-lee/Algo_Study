import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort() # 정렬

dict = {}
for idx, num in enumerate(arr):
    if num in dict: # 이미 dict에 있으면 패스
        continue
    else:
        dict[num] = idx

nums = []
for _ in range(M):
    nums.append(int(input()))

ans = []
for num in nums:
    if num in dict: # dict에 있으면 idx값
        ans.append(dict.get(num))
    else:
        ans.append(-1) # 없으면 - 1

print('\n'.join(map(str,ans)))