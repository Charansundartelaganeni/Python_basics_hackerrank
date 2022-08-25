
from collections import OrderedDict
od = OrderedDict() 
n = int(input())
for i in range(n):
    item,price = input().rsplit(" ",1) 
    #rsplit seperates the values with the punctuation given thiru bro
    od[item] = od.get(item, 0) + int(price)
for key,value in od.items():
    print(key,value)

