from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

R, C = map(int,input().split())
arr = [input() for _ in range(R)]

ans = 0

for r in range(R):
    for c in range(C):
        if arr[r][c] == '.': # 길 일때 시작
            cnt = 0 # 4방향 중 길인 수 세기
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr<R and 0<=nc<C and arr[nr][nc] == '.': # 마을을 벗어나지 않으면서 4방향 중 길인 경우
                    cnt += 1
            if cnt <= 1: # 막다른 길이거나 더이상 갈 수 없을 때
                ans = 1
print(ans)