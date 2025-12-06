N = int(input())
tops = list(map(int,input().split()))


ans = [0] * N
stack = [] # 번호, 높이
for i in range(N):
    # 현재 탑보다 낮은 탑들 제거
    while stack and stack[-1][1] < tops[i]:
        stack.pop()
    # 수신한 탑 기록
    if stack:
        ans[i] = stack[-1][0]
    else:
        ans[i] = 0

    # 현재 탑 스택에 추가
    stack.append([i+1, tops[i]])

print(*ans)