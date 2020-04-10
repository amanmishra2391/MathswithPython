def isPrime(N):
    a=2
    k=N//2
    while k>=a:
        if N%a==0:
            return False
        a+=1
        k=N//a
    return True
