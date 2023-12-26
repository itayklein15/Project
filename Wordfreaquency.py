import sys
with open('file.txt', 'r') as file:
    lines = file.readlines()
for l in lines:
    lines=l.split()
counts = dict()
for i in lines:
    counts[i] = counts.get(i, 0) + 1
sorted_words=sorted(counts.items(),key=lambda sort :sort[1],reverse=True)

N=sys.argv
if(sys.argv>N):
    for i in range (N):
        print(i+1," -the word",sorted_words[i][0],"apeard",sorted_words[i][1],"times")