from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(sorted(s))
    for i,j in c.most_common(3):
        print(i,j) 



# most_common() : The Counter() function returns a dictionary which is unordered. You can sort it according to the number of counts in each element using most_common() function of the Counter object.    