name = "한결"
age = 16
height = 162.5


print("이름: {}, 나이: {}, 키: {}".format(name, age, height))
print("이름: {:s}, 나이: {:d}, 키: {:f}".format(name, age, height))
print("이름: {:4s}, 나이: {:3d}, 키: {:.2f}".format(name, age, height))

#python 3.7부터 지원하는 새로운 방법(f-string)
print(f"이름: {name}, 나이: {age}, 키: {height}")
print(f"이름: {name:4s}, 나이: {age:3d}, 키: {height:.2f}")

user1 = f"이름: {name}, 나이: {age}, 키: {height}"
print(user1)