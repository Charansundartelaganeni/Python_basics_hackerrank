n,column,a = int(input()), input().split().index('MARKS') , 0
for i in range(n): 
    result = int(input().split()[column]); a+=result
print(a/n)  

