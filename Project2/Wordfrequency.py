import sys
with open('file.txt', 'r') as file:
    lines = file.readlines()
for l in lines:
    lines=l.split()
counts = dict()
for i in lines:
    counts[i] = counts.get(i, 0) + 1
sorted_words=sorted(counts.items(),key=lambda sort :sort[1],reverse=True)
N=int(sys.argv[1])
for r in range (N):
    print(r+1," -the word",sorted_words[r][0],"apeard",sorted_words[r][1],"times")