def isprime(n):
    if n < 2:
        return
    for i in range(2,(int(n**0.5))+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())
    while not isprime(n):
        n += 1
    print(n)