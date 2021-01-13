class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __eq__(self, other):
        return self.data == other.data 

    def __iter__(self): 
        return self
    
    def __next__(self):
        self.index += 2
        if self.index >= len (self.data):
            self.index = -2
            raise StopIteration

        return self.data[self.index:self.index+2]

solarterm1 = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
solarterm2 = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

print(solarterm1.__dict__)  # 개발자가 만든 것만 

# for k in solarterm1:
#     print(k, end = ',')

# print()
# # for k in solarterm:
# #     print(k, end = ',')

# print(dir(solarterm1))