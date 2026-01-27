scores = {}
for i in range(8):
    scores[i+1] = int(input())
sorted_scores = sorted(scores.items(), key=lambda x:-x[1])

ans = []
ans_score = 0
for idx, score in sorted_scores[:5]:
    ans.append(idx)
    ans_score += score
ans.sort()
print(ans_score)
print(*ans)