def isArmstrong(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False
