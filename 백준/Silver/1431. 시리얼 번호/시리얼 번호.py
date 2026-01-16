N = int(input())
words = []
sum_v = {}
for _ in range(N):
    words.append(input())

def digit_sum(word):
    digit_sum = 0 # 숫자인 각 자리수들의 합
    for i in word:
        if i.isdigit(): # 해당 단어가 숫자라면
            digit_sum += int(i)
    return digit_sum


words.sort(key=lambda x:(len(x),digit_sum(x),x))
print('\n'.join(words))