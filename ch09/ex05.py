nums = [n*2 for n in range(1, 11) if n % 2 == 0]
for i in nums:
    print(i, end = ', ')

nums = []
for  n in range(1, 11):
    nums.append(n*2)

print(nums)
print()

# 랜덤 정수 50개를 리스트에 담아라.
import random   # random.randrange(1, 101)
random_numbers = [ random.randrange(1, 101) for n in range(50)]
print(random_numbers)

random_numbers = []
for _ in range(50):
    random_numbers.append(random.randrange(1, 101))