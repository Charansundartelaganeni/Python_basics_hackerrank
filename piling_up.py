for _ in range(int(input())):
        n, lst = (int(input()), list(map(int, input().split())))
        for i in range(1, int((n/2))+1):
            if lst[-(i+1)] > lst[-i] and lst[i-1] < lst[i]:
                print("No")
                break
        else:
            print("Yes")