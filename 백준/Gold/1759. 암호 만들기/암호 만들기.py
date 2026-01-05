def backtracking(start,depth):
    global vowel_num, consonant_num

    if depth == L:
        if vowel_num >= 1 and consonant_num >= 2: # 최소 한 개의 모음과 최소 두 개의 자음으로 구성
            print(''.join(ans))
        return

    for i in range(start,C):
        if arr[i] in ('a','e','i','o','u'): # 모음이면
            ans.append(arr[i])
            vowel_num += 1
            backtracking(i+1, depth+1)
            vowel_num -= 1
        else: # 자음이면
            ans.append(arr[i])
            consonant_num += 1
            backtracking(i+1, depth+1)
            consonant_num -= 1

        ans.pop()



L, C = map(int,input().split())
arr = list(input().split())

arr.sort()

ans = []
vowel_num = 0  # 모음 개수 (a,e,i,o,u)
consonant_num = 0  # 자음 개수
backtracking(0,0)