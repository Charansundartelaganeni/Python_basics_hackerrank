from collections import deque as dq

num_ops = int(input())

dequer = dq()

for i in range(num_ops):
    
    data = input().split()
    first = data[0]
    
    if len(data) > 1:
        val = data[1]
    
    if first == "append":
        
        dequer.append(val)
    
    elif first == "pop":
        
        dequer.pop()
        
    elif first == "popleft":
        
        dequer.popleft()
        
    elif first == "appendleft":
        
        dequer.appendleft(val)
        
print(" ".join(dequer))

