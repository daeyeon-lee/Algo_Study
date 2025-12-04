import sys
input = sys.stdin.readline

letter = input().rstrip()
N = int(input())
left = [] # 커서 왼쪽 값
for i in letter:
    left.append(i)
right = [] # 커서 오른쪽 값

for _ in range(N):

    commends = (input().split())
    if commends[0] == 'L':
        if left:
            right.append(left.pop()) # 커서 왼쪽으로 이동 -> left의 맨 오른쪽 원소를 right에 추가
    elif commends[0] == 'D':
        if right:
            left.append(right.pop()) # 커서 오른쪽으로 이동 -> right의 맨 왼쪽 원쪽 원소를 left에 추가
    elif commends[0] == 'P':
        left.append(commends[1]) # 커서 왼쪽에 문자 추가
    elif commends[0] == 'B':
        if left:
            left.pop()

print(''.join(left+right[::-1]))