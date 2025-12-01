from collections import deque
N = int(input())
ballons = list(map(int,input().split()))

q = deque()

for idx, ballon_num in enumerate(ballons,start = 1):
    q.append((idx,ballon_num))

ans = [] # 풍선 idx 담기

# 1번 풍선부터 시작
idx, ballon_num = q.popleft()
ans.append(idx)

while q:
    if ballon_num > 0: # 양수면
        q.rotate(-(ballon_num-1)) # 왼쪽으로 move -1 이동
    if ballon_num < 0: # 음수면
        q.rotate(-ballon_num) # 양수로 만들고 오른쪽으로 이동
    idx, ballon_num = q.popleft()
    ans.append(idx)

print(*ans)