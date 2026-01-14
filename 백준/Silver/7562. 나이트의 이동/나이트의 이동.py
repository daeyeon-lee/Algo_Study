from collections import deque

dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

T = int(input())
for _ in range(T):
    I = int(input())
    x, y = map(int,input().split()) # 현 위치
    gx, gy = map(int,input().split()) # 가야하는 위치

    dist = [[-1] * I for _ in range(I)]
    cnt = 0
    q = deque()
    q.append((x,y))
    dist[x][y] = 0 # 시작점 거리 초기화

    while q:
        r, c = q.popleft()
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<I and 0<=nc<I and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                if nr == gx and nc == gy:
                    q.clear() # 도착지점이면 큐 비우고 끝
                    break
                q.append((nr,nc))
    print(dist[gx][gy])