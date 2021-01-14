def calcsum(n):
    def add(a, b):
        return a+b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total 

print("~10 = ", calcsum(10))
