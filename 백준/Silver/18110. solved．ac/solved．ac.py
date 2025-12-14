import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
else:
    diff = []
    for _ in range(N):
        diff.append(int(input()))
    diff.sort()
    except_v = int(N * 0.15 + 0.5)

    print(int(sum(diff[except_v:N-except_v]) / len(diff[except_v:N-except_v])+0.5) )