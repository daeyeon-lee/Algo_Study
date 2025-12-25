N = int(input())
nums = [[] for _ in range(N+1)]
ans = []
for i in range(1,N+1):
    nums[int(input())].append(i)

for i in range(1,N+1):
    visited = [0] * (N+1)
    q = []
    q.append(i)
    visited[i] = 1

    while q:
        num = q.pop()
        for next_num in nums[num]:
            if visited[next_num] == False: # 방문 안했다면 그래프 계속 탐색
                q.append(next_num)
                visited[next_num]
            elif visited[next_num] and next_num == i: # 이미 방문했고 다시 i의 값과 같다면 정답
                ans.append(next_num)
print(len(ans))
print('\n'.join(map(str,ans)))



