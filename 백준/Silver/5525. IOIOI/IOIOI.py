N = int(input())
M = int(input())
S = input()


search ='I' + 'OI'* N


cnt = 0
for i in range(M-len(search)+1):
    if S[i:i+len(search)] == search:
        cnt += 1
print(cnt)