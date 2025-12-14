N = int(input())
houses = list(map(int,input().split()))

houses.sort()


ans = []
## 최소값이 되기 위해선 중앙값 선택
if len(houses) % 2 != 0: # 홀수개이면
    ans.append(houses[len(houses) // 2])
else: # 짝수개이면
    ans.append(houses[len(houses) // 2 - 1])
    ans.append(houses[len(houses) // 2])
print(ans[0])