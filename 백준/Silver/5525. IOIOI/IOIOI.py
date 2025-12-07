N = int(input())
M = int(input()) # S의 길이
S = input()
search ='I' + 'OI'* N


i = 0 # 자릿수
cnt = 0 # IOI의 갯수
ans = 0 # 실제 search 개수
while i < M - 2:
    if S[i] == "I" and S[i+1] == "O" and S[i+2] == "I":
        cnt += 1 # IOI 개수 세기
        if cnt >= N:
            ans += 1 # search 개수 세기
        i += 2 # 세글자씩 보면 되니까
    else:
        cnt = 0 # IOI 구조가 깨지면
        i += 1
print(ans)