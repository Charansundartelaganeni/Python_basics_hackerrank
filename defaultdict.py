from collections import defaultdict
d = defaultdict(list)
l=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    l+=[input()]  

for word in l: 
    print(*d[word]) if word in d else print(-1)