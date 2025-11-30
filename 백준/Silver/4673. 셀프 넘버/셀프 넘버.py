create_num = []
for num in range(1,10001):
    sum = 0
    for i in range(len(str(num))):
        sum += (int(str(num)[i]))
    sum += num
    create_num.append(sum)


for i in range(1,10001):
    if i not in create_num:
        print(i)