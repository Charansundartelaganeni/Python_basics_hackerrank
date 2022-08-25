if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    #if len(set(arr)) == 1 : print(list(set(arr))[0])
    b = sorted(arr) 
    p = b[-1] 
    
    for i in b[::-1]: 
        
        if i < p: 
            
            print(i)  
            
            break

