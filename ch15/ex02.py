class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'{self.age}살 {self.name}입니다.')

    def __str__(self):  # print()
        return f'<Human {self.age}, {self.name}>'

    def __repr__(self): # list에 있는 print()
        return f'<Human {self.name}>'

kim = Human("김상형", 29)
kim.intro()

lee = Human("이승우", 45)
lee.intro()

print(kim)
print(lee)

li = [kim, lee]
print(li)