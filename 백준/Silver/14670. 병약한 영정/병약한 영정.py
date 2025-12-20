N = int(input())
medicions = {}
for _ in range(N):
    m,n = map(int,input().split())
    medicions[m] = n

R = int(input())

for _ in range(R):
    ans = []
    symptoms = list(map(int,input().split()))
    # print(symptoms)
    for i in range(1,len(symptoms)):
        if symptoms[i] not in medicions:
            print("YOU DIED")
            break
        else:
            ans.append(medicions[symptoms[i]])
    else:
        print(*ans)



