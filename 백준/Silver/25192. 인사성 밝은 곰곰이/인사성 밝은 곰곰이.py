N = int(input())
chats = []
for _ in range(N):
    chats.append(input())

emoticon = set()
cnt = 0
for i in range(1,N):
    if chats[i] == 'ENTER':
        cnt += len(emoticon)
        emoticon.clear()
    else:
        emoticon.add(chats[i])
cnt += len(emoticon)
print(cnt)