L = int(input())
letter = input()

ans = 0
for i in range(len(letter)):
    if letter[i] == 'a':
        num_v = 1
    elif letter[i] == 'b':
        num_v = 2
    elif letter[i] == 'c':
        num_v = 3
    elif letter[i] == 'd':
        num_v = 4
    elif letter[i] == 'e':
        num_v = 5
    elif letter[i] == 'f':
        num_v = 6
    elif letter[i] == 'g':
        num_v = 7
    elif letter[i] == 'h':
        num_v = 8
    elif letter[i] == 'i':
        num_v = 9
    elif letter[i] == 'j':
        num_v = 10
    elif letter[i] == 'k':
        num_v = 11
    elif letter[i] == 'l':
        num_v = 12
    elif letter[i] == 'm':
        num_v = 13
    elif letter[i] == 'n':
        num_v = 14
    elif letter[i] == 'o':
        num_v = 15
    elif letter[i] == 'p':
        num_v = 16
    elif letter[i] == 'q':
        num_v = 17
    elif letter[i] == 'r':
        num_v = 18
    elif letter[i] == 's':
        num_v = 19
    elif letter[i] == 't':
        num_v = 20
    elif letter[i] == 'u':
        num_v = 21
    elif letter[i] == 'v':
        num_v = 22
    elif letter[i] == 'w':
        num_v = 23
    elif letter[i] == 'x':
        num_v = 24
    elif letter[i] == 'y':
        num_v = 25
    elif letter[i] == 'z':
        num_v = 26
    ans += num_v * 31**i
print(ans % 1234567891)
