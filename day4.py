s1=[]
s2=[]
for i in range(int(input())):
    
    x = list(map(int, input().split(" ")))    
    if x[0] == 1:
        s1.append(x[1])
    if x[0] == 2:
        if s2:
            s2.pop()
            continue
        else:
            while s1:
                s2.append(s1.pop())
            s2.pop()
            continue
    if x[0] == 3:
        if not s2:
            print(s1[0])
        else:
            print(s2[-1])

