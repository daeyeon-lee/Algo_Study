from collections import deque

N, K = map(int,input().split())

# 수빈이가 갈 수 있는 경우의 수는 3가지 : x-1 x+1 2*x

dist = [-1] * (100001)

q = deque([N])
dist[N] = 0
cnt = 0

# bfs는 층층이 뻗어나가므로 해당 숫자까지 갈 수 있는 거리를 dist배열에 저장하면 그것이 문제에서 요구하는 정답
while q:
    cur = q.popleft()
    for next in (cur-1, cur+1, 2*cur):
        if 0<= next <= 100000 and dist[next] == -1:
            cnt += 1
            dist[next] = dist[cur] + 1
            q.append(next)
print(dist[K])



