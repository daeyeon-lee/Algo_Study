def binary_search(M, A):
    start = 1 			    # 최소 시간
    end = max(A) * M     	# 최대 시간
    ans = end               # 정답 갱신
    while start < end:
        mid = (start + end) // 2 # 중간값
        ballons_sum = 0     # 만들 수 있는 풍선의 개수
        for time in A:
            ballons_sum += mid // time
        if ballons_sum >= M:
            end = mid
            if end <= ans:
                ans = end
        else:
            start = mid + 1
    return ans

N, M = map(int,input().split())
A = list(map(int,input().split()))
print(binary_search(M,A))


