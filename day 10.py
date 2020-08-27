import math
import numpy as np


def calc_pearson_coef(x,y):
    try:
        coef = SS(x, y)/math.sqrt(abs(SS(x,x)*SS(y,y)))
    except:
        coef = 0
    return coef

def SS(x,y):
    return (sum([i*j for (i,j) in zip(x,y)])-(sum(x)*sum(y))/len(x))

def main():
    t = int(input())
    for i in range(t):
        n = input()
        gpa = [float(a) for a in input().split()]
        coeflist = []
        for j in range(5):
            marks = [float(x) for x in input().split()]
            temp = calc_pearson_coef(marks,gpa)
            coeflist.append(temp)
        print(np.argmax(coeflist)+1)

if(__name__=="__main__"):
    main()
