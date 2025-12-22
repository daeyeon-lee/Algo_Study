from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

R, C = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(R)]

time = 0
prev = 0

while True:
    # 현재 치즈 개수 세기
    cheese = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 1:
                cheese += 1
    if cheese == 0:
        break
    prev = cheese # 다 녹기 직전 치즈 개수

    # BFS - 0,0부터 시작해서 바깥공기를 닿았는지 판단
    visited = [[False] * C for _ in range(R)]
    q = deque()
    q.append([0,0])
    visited[0][0] = True

    melt = [] # 이번 시간에 녹을 치즈 좌표들

    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                visited[nr][nc] = True
                if arr[nr][nc] == 0:
                    q.append([nr,nc]) # 공기면 계속 확장
                else:
                    melt.append([nr,nc])
    # 외부 공기와 맞닿았으면 녹이기
    for r, c in melt:
        arr[r][c] = 0
    time += 1

print(time) # 치즈 녹는데 걸리는 시간
print(prev) # 바로 직전 치즈조각들의 개수

