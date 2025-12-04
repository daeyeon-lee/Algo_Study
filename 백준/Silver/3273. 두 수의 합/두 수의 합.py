N = int(input())
arr = list(map(int,input().split()))
x = int(input())

left = 0
right = N-1

arr.sort()

cnt = 0
while left < right:
    if arr[left] + arr[right] == x:
        cnt += 1
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
    elif arr[left] + arr[right] > x:
        right -= 1
print(cnt)