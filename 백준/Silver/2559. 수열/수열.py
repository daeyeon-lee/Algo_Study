N, K = map(int,input().split())
temp = list(map(int,input().split()))
arr = [0] * (N-K+1)
arr[0] = sum(temp[:K])


for i in range(1, N-K+1):
    arr[i] = arr[i-1] - temp[i-1] + temp[i+K-1] # 앞에꺼 빼고 뒤에꺼 더하고
print(max(arr))