n  = int(input())
d = {}

for i in range(n):
    key = input()
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1
                
print(len(d))
for i in d:
    print(d[i], end= ' ')

