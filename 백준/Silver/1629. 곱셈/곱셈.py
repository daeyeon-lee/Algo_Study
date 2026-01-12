def solution(num,cnt):
    if cnt == 0:
        return 1 % C
    elif cnt == 1:
        return num % C

    half = solution(num, cnt // 2)
    half_sq = (half * half) % C

    if cnt % 2 == 0:
        return half_sq
    else:
        return (half_sq * num) % C

A, B, C = map(int,input().split())
print(solution(A,B))

