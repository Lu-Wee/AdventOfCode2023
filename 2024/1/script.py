f = open("input.txt", "r")
data = [l.strip().split() for l in f.readlines()]
listA = [int(l[0]) for l in data if len(l) > 1]
listB = [int(l[1]) for l in data if len(l) > 1]
listA.sort()
listB.sort()
diffList = [abs(listA[i] - listB[i]) for i in range(len(listA))]
answer = sum(diffList)

