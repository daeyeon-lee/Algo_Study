from collections import deque

N, K = map(int,input().split())

arr = deque()
for i in range(1,N+1):
    arr.append(i)
cnt = 0
ans = []
while cnt < N:
    arr.rotate(-K)
    ans.append(arr.pop())
    cnt += 1

print('<'+', '.join(map(str,ans))+'>')

