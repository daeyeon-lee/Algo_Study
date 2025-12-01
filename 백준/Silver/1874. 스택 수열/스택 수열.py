N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

ans = []
stack = []
next_num = 1  # push할 숫자

for num in nums:
    # num이 나올 때까지 push
    while next_num <= num:
        stack.append(next_num)
        ans.append('+')
        next_num += 1

    # 스택이 존재하고 가장 마지막값이 해당 숫자라면
    if stack and stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        # 아니라면 NO
        print('NO')
        break
else:
    print('\n'.join(ans))
