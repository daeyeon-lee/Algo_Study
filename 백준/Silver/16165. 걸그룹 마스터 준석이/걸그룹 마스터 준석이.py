N, M = map(int,input().split())
group = {}
for _ in range(N):
    team = input()
    member_num = int(input())

    for _ in range(member_num):
        member = input()
        group.setdefault(team,[]).append(member)


for _ in range(M):
    problem = input()
    problem_num = int(input())

    if problem_num == 0:
        ans = group[problem]
        ans.sort()
        print('\n'.join(ans))
    if problem_num == 1:
        for team, member in group.items():
            if problem in member:
                print(team)