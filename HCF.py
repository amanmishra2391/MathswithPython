def HCF(x,y):
    N=1
    a=2
    while (x!=1 or y!=1) and(x>=a or y>=a) :
        if x%a==0 and y%a==0:
            x=x/a
            y=y/a
            N*=a
        else :
            a+=1
    return N
