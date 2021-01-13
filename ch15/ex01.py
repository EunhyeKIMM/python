# 누구의 계좌인지..
# 출금 

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            raise Exception('잔액부족')

        self.balance -= money
        return money 

    # def whoacc(self):
    #     print(f'{self.onwer}의 계좌입니다.')

    def inquiry(self):
        print("잔액은 %d원 입니다. " %self.balance)


account = Account("홍길동", 8000)
account.deposit(1000)
account.inquiry()   
  
shinhan = Account("김신한", 8000)
shinhan.deposit(1000)
shinhan.inquiry()

try:
    nonghyup = Account("이농협", 1200000)
    nonghyup.inquiry() 
    nonghyup.withdraw(1230000)
except Exception as e:
    print('예외', e)

#li1 = [1, 2, 3]
#li1.append() 

print(shinhan)
