N = int(input())
ans = 1

num_v = N
while num_v > 0:
    ans *= num_v
    num_v -= 1


len_v = len(str(ans))
cnt = 0

for i in range(len_v-1,-1,-1):
    if (str(ans)[i]) == '0':
        cnt += 1
    else:
        break
print(cnt)
