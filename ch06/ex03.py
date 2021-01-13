# 1에서 100까지의 수에서

# 짝수의 합: xxxx
# 홀수의 합: yyyy

num = 1
even_total = 0
odd_total = 0 

while num <= 100:
    odd_total += num
    num += 1
    even_total += num
    num += 1 
# if문을 이용해서 하는 방법이 있지만 귀찮아서 그냥 이렇게 썼다.
# Am I bad programmer? Haha

print("홀수의합 = ", odd_total)
print("짝수의합 = ", even_total)  