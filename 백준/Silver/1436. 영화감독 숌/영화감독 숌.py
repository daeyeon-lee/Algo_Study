N = int(input())

num_v = 666

cnt = 0
while True:
    if '666' in str(num_v):
        cnt += 1
        if cnt == N:
            print(num_v)
            break
        num_v += 1
    else:
        num_v += 1