T = int(input())
for _ in range(T):
    n = int(input())
    wearings = {}
    for _ in range(n):
        name, category = input().split()
        wearings[category] = wearings.get(category,0) + 1


    # 각 카테고리마다 선택지는 카테고리의 개수 + 1(안 입는 경우)
    # 알몸인 경우 제외 -1
    ans = 1

    for nums in wearings.values():
        ans *= (nums + 1)

    print(ans-1)
