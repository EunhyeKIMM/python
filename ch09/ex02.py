nums = list(range(0, 10))
print(nums[:])
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 55
print(score[2])

# 주의사항: list는 요소 수정이 가능하지만
# 문자열은 요소 수정이 불가능하다(불변 객체)

nums[2:5] = [20, 30, 40]
print(nums)
nums[6:8] = [60, 70, 80, 90]
print(nums)