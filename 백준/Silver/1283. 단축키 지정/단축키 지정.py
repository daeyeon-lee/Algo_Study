N = int(input())
letters = []
for _ in range(N):
    letters.append(input())


used = set()
for letter in letters:
    found = False

    # 단어의 첫 글자 확인
    for i in range(len(letter)):
        if (i == 0 or letter[i-1] == ' ') and letter[i].isalpha(): # 0번 인덱스이거나 앞에 빈칸이 있을 때 알파벳이 맞을때
            if letter[i].lower() not in used:
                used.add(letter[i].lower())
                new = letter[:i] + '[' + letter[i] + ']' + letter[i + 1:]
                print(new)
                found = True
                break
    # 단어 전체 확인
    if found == False:
        for i in range(len(letter)):
            if letter[i].isalpha():
                if letter[i].lower() not in used:
                    used.add(letter[i].lower())
                    print(letter[:i] + '[' + letter[i] + ']' + letter[i + 1:])
                    found = True
                    break
    # 이래도 단축키 없으면 그냥 단어 출력
    if found == False:
        print(letter)