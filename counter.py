from collections import Counter 
i, j = input(), Counter([int(x) for x in input().split()])

total = 0 

for i in range(int(input())):
    
    x, y = list(map(int, input().split()))
    
    if j.get(x) and j.get(x) != 0:
        total += y 
        j[x] = j.get(x) - 1 
    
print(total)