from collections import deque
import sys
input = sys.stdin.readline

def hacking_computer(start, mark):
    q = deque()
    q.append(start)
    visited[start] = mark
    cnt = 1

    while q:
        node = q.popleft()
        for next_node in computers[node]:
            if visited[next_node] != mark:
                visited[next_node] = mark
                q.append(next_node)
                cnt += 1
    return cnt

N, M = map(int,input().split())
computers = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    # computers[u].append(v)
    computers[v].append(u)

visited = [0] * (N+1) # visited 배열을 함수에 만들면 시간초과 되기 때문에 바깥쪽에 생성

max_value = 0
ans = []
mark = 0
for i in range(1,N+1):
    mark += 1 # 반복문 돌 때마다 mark 값을 1개씩 늘려 visited 배열의 기본값을 초기화
    hacking_v = hacking_computer(i, mark)
    if hacking_v > max_value:
        ans = [i]
        max_value = hacking_v
    elif hacking_v == max_value:
        ans.append(i)
ans.sort()
print(*ans)
