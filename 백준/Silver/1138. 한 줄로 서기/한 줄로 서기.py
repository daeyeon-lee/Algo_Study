N = int(input())
arr = list(map(int,input().split()))

line = []
for i in range(N,0,-1):
    line.insert(arr[i-1],i)
print(*line)