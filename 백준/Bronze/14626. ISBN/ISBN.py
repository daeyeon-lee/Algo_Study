isbn = input()

sum_v = 0
star_v = 0
for i in range(len(isbn)):
    if i % 2 == 0:
        if isbn[i] == '*':
            star_v += 1
        else:
            sum_v += (int(isbn[i]) * 1)
    else:
        if isbn[i] == '*':
            star_v += 3
        else:
            sum_v += (int(isbn[i]) * 3)

for x in range(10):
    if (sum_v + (star_v * x)) % 10 == 0:
        print(x)
        break
