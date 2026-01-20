N = int(input())
arr = list(map(int, input().split()))

ans = []
find_num = 1
stack = []  # 옆 줄(스택)

for x in arr:
    # 옆줄 맨 위가 지금 필요한 번호면 계속 빼기
    while stack and stack[-1] == find_num:
        ans.append(stack.pop())
        find_num += 1

    # 본 줄에서 바로 나갈 수 있으면 나가고, 아니면 옆줄로
    if x == find_num:
        ans.append(x)
        find_num += 1
    else:
        stack.append(x)

# 남은 옆줄 처리
while stack and stack[-1] == find_num:
    ans.append(stack.pop())
    find_num += 1

print("Nice" if find_num == N + 1 else "Sad")
