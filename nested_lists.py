if __name__ == '__main__':
    a = [] 
    scores =[] 
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())  
        
        a.append([name,score]) 
        scores.append(score) 
        names.append(name) 
    p = sorted(scores)[0] 
    for i in sorted(scores): 
        if i > p: 
            p = i 
            break 
    #print(p)    
    result = [] 
    
    for i in range(len(scores)): 
        
        if scores[i] == p: 
            
            result.append(names[i]) 
            
    result_names = sorted(result) 
    
    for i in result_names: 
        
        print(i)
        
        