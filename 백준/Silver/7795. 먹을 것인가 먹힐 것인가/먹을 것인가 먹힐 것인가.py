T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()


    cnt = 0
    index = 0

    for a in A:
        while index < M and B[index] < a:
            index += 1
        cnt += index


    print(cnt)