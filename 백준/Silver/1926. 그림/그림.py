from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0 # 그림의 개수
max_picture = 0  # 그림의 넓이 최대값 비교

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append([i,j])
            visited[i][j] = True

            cnt += 1 # 시작점(그림)의 개수 늘리기
            picture = 1 # 그림의 넓이 1로 시작

            # 시작점 넣고 bfs
            while q:
                r,c = q.popleft()
                for d in range(4):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                        if arr[nr][nc] == 1:
                            q.append([nr,nc])
                            picture += 1
                            visited[nr][nc] = True

            # 그림의 넓이 최대값 비교
            if picture >= max_picture:
                max_picture = picture
print(cnt)
print(max_picture)