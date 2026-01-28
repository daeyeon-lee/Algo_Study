import sys
input = sys.stdin.readline

N, M = map(int,input().split())
cnt = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        cnt[word] = cnt.get(word,0) + 1

sorted_cnt = sorted(cnt.items(),key = lambda x:(-x[1],-len(x[0]),x[0]))

for i in sorted_cnt:
    print(i[0])