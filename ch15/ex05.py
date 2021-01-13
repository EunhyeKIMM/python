class Human: 
    def __init__(self, age, name):
        self.name = name
        self.age = age
    
    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

class Player:
    def __init__(self, gender):
        self.geder = gender 


class Student(Human, Player):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        #Human.__init__(self, name, age)

        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번: " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을현 누를황")

kim = Human(29, "김상형")
kim.intro()
lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()