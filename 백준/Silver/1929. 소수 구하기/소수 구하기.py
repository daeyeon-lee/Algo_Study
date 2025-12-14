def is_prime(x):
    if x < 2: # 1은 절대 소수가 아님
        return False
    for i in range(2, int(x**0.5) + 1): # 2부터 제곱근까지
        if x % i == 0: # 나누어떨어지는 수가 하나라도 있으면 합성수
            return False
    return True # 나누어떨어지는 수가 없으면 소수

M,N = map(int,input().split())

ans = []
num_v = M
while num_v <= N:
    if is_prime(num_v) == True:
        ans.append(num_v)
        num_v += 1
    else:
        num_v += 1
        continue

print('\n'.join(map(str,ans)))
