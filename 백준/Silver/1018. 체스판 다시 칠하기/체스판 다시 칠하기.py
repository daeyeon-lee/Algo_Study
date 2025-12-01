# 8 * 8에서 색칠해야하는 부분 찾기
def find_painting(r,c):
    # 색칠할 직사각형의 수들의 리스트
    b_cnt = 0
    w_cnt = 0
    for u in range(r, r + 8):
        for v in range(c, c + 8):
            cur = arr[u][v]
            # (u+v)가 짝수면 '시작 색', 홀수면 '반대 색'
            if (u + v) % 2 == 0:  # 짝수 칸
                if cur != 'B':  # B로 시작하는 체스판이면 짝수칸은 B
                    b_cnt += 1
                if cur != 'W':  # W로 시작하는 체스판이면 짝수칸은 W
                    w_cnt += 1
            else:  # 홀수 칸
                if cur != 'W':  # B로 시작하면 홀수칸은 W
                    b_cnt += 1
                if cur != 'B':  # W로 시작하면 홀수칸은 B
                    w_cnt += 1
    return(min(b_cnt, w_cnt))
N, M = map(int,input().split())
arr = [input() * M for _ in range(N)]

ans = 2e21
# 가능한 시작점
for i in range(M-8+1):
    for j in range(N-8+1):
        ans = min(ans,find_painting(j,i))
print(ans)


