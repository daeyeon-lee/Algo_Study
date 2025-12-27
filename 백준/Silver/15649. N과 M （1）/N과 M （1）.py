def backtracking(len):
    if len == M:
        print(*answer)
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            
            # 재귀 호출 전에는 선택(방문처리 / append)
            backtracking(len + 1)
            
            # 재귀 돌아오면 다시 선택 취소(방문처리 해제 / pop)
            answer.pop() # 방금 넣었던 숫자를 빼서 이전 상태로 복구
            visited[i] = False # 사용됨을 해제



N, M = map(int,input().split())
visited = [False] * (N+1)
answer = []

backtracking(0)