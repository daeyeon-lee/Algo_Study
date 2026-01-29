N = int(input())
nums = list(map(int,input().split()))

ans = [-1] * N
stack = [] # 원소의 인덱스 값
for i in range(N):
    while stack and nums[stack[-1]] < nums[i]: # stack이 비어있지 않고 stack 맨 위 인덱스 값이 nums[i] 보다 작으면
        ans[stack.pop()] = nums[i] # 스택 맨 위를 꺼내서 그 인덱스의 오큰수를 nums[i]로 지정
    stack.append(i)
print(*ans)