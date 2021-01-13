def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num
    
    return total 

print(" ~ 4 =", calcsum(4))
print(" ~ 10 =", calcsum(10))