import sys
input = sys.stdin.readline

trees = []
while True:
    tree = input().rstrip('\n')
    if not tree:
        break
    trees.append(tree)

name = {}
for tree in trees:
    name[tree] = name.get(tree,0) + 1
name_sorted= sorted(name.items(),key=lambda x: x[0])

total = len(trees)
for n, p in name_sorted:
    ratio = p / total * 100
    print(f"{n} {ratio:.4f}")