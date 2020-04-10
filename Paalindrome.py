def isPalindrom(n):
    N=str(n)
    L=len(N)
    for i in range(L//2):
        if N[i]!=N[L-1-i]:
            return False
    return True
