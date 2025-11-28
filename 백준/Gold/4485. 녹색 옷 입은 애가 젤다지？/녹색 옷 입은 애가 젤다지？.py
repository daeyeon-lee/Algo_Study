from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
ans = []
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[2e21] * N for _ in range(N)]

    q = deque()
    dist[0][0] = arr[0][0] # 시작점
    q.append([0,0])

    while q:
        r,c = q.popleft()

        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr<N and 0<=nc<N:
                # 비용은 지금 칸 + 다음 칸
                cost = dist[r][c] + arr[nr][nc]
                # 그 값이 더 작으면 갱신
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    q.append([nr,nc])


    ans.append(dist[N-1][N-1])


for i in range(len(ans)):
    print(f'Problem {i+1}: {ans[i]}')