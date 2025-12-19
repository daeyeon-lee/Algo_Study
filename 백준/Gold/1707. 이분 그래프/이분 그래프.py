from collections import deque
import sys
input = sys.stdin.readline
K = int(input())

def is_graph(start, group_num):
    q = deque([start])
    visited[start] = group_num # 그룹 정하기(1/-1)
    while q:
        node = q.popleft()

        for next_node in arr[node]:
            if not visited[next_node]: # 다음 노드가 방문하지 않았다면
                q.append(next_node) # 큐에 추가
                visited[next_node] = -1 * visited[node] # 다른 그룹 배치
            elif visited[next_node] == visited[node]: # 다음 노드가 이미 방문했는데 그룹이 같다면
                return False # 그래프 불가
    return True

for _ in range(K):
    V, E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,input().split())
        arr[u].append(v)
        arr[v].append(u)

    visited = [False] * (V+1) # 방문여부 체크
    ans = True

    for start in range(1,V+1):
        if visited[start] == False:
            result = is_graph(start,1)
            if result == False:
                ans = False
                break
    if ans == True:
        print("YES")
    else:
        print("NO")

