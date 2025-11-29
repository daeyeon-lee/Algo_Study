N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())


arr.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0])) # 내림차순은 -로 하면 됨


for i in range(N):
    print(arr[i][0])