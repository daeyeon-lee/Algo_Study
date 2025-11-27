letter1 = input()
letter2 = input()

cnt = 0
i = 0
while i <= len(letter1)-len(letter2) + 1:
    if letter1[i:i+len(letter2)] == letter2:
        cnt += 1
        i += len(letter2)
    else:
        i+= 1
print(cnt)