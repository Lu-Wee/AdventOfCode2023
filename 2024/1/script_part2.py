f = open("input.txt", "r")
data = [l.strip().split() for l in f.readlines()]
listA = [int(l[0]) for l in data if len(l) > 1]
listB = [int(l[1]) for l in data if len(l) > 1]

dict = {}
for b in listB:
    if b in dict.keys():
            dict[b] += 1
    else:
            dict[b] = 1


similarityScore = 0
for a in listA:
    if a in dict.keys():
        similarityScore += a*dict[a]

print(similarityScore)
