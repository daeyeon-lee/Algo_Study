from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

# 색칠하기
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

# 색칠 안한 칸 넓이 세기
areas = []
cnt = 0

for k in range(M):
    for l in range(N):
        if arr[k][l] == 0 and not visited[k][l]:
            cnt += 1
            q = deque()
            q.append([k,l])
            visited[k][l] = True
            area = 1 # 시작칸 넓이로 포함

            while q:
                r,c = q.popleft()
                for d in range(4):
                    nr,nc = r+dr[d], c+dc[d]
                    if 0<=nr<M and 0<=nc<N and not visited[nr][nc]:
                        if arr[nr][nc] == 0:
                            visited[nr][nc] = True
                            q.append([nr,nc])
                            area += 1
            areas.append(area)
print(cnt)
areas.sort()
print(*areas)

