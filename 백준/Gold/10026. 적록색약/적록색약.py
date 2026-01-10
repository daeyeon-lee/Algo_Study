from collections import deque
dr, dc = [-1,1,0,0], [0,0,-1,1]


N = int(input())
arr = [list(input()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]


## 적록 색약이 아닌 사람이 봤을 때의 구역
no_RGCD = 0
for i in range(N):
    for j in range(N):
        if visited1[i][j] == False:
            q = deque()
            q.append([i,j])
            visited1[i][j] = True
            no_RGCD += 1

            while q:
                r,c = q.popleft()
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and not visited1[nr][nc] and arr[r][c] == arr[nr][nc]:
                        q.append([nr,nc])
                        visited1[nr][nc] = True


## 적록 색약인 사람이 봤을 때의 구역
RGCD = 0
arr2 = arr

## 빨강이랑 초록을 둘 중에 하나의 색깔로 바꿔버림
for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

for k in range(N):
    for l in range(N):
        if visited2[k][l] == False:
            q = deque()
            q.append([k,l])
            visited2[k][l] = True
            RGCD += 1

            while q:
                r,c = q.popleft()
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and not visited2[nr][nc] and arr2[r][c] == arr2[nr][nc]:
                        q.append([nr,nc])
                        visited2[nr][nc] = True
print(no_RGCD, RGCD)