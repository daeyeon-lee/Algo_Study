from collections import deque

def find_friends(start):
    scores = [-1] * (N + 1)
    q = deque()
    q.append(start)
    scores[start] = 0

    while q:
        node = q.popleft()
        for next_node in friends[node]:
            if scores[next_node] == -1:
                scores[next_node] = scores[node] + 1
                q.append(next_node)
    return max(scores[1:])




N = int(input())
friends = [[] for _ in range(N+1)]


while True:
    u, v = map(int,input().split())
    if u == -1 and v == -1:
        break
    friends[u].append(v)
    friends[v].append(u)

min_value = 2e21
ans = []
for i in range(1,N+1):
    if find_friends(i) < min_value:
        ans.clear()
        ans.append(i)
        min_value = find_friends(i)
    elif find_friends(i) == min_value:
        ans.append(i)
print(min_value, len(ans))
print(' '.join(map(str,ans)))