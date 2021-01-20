# ORM(Object Telationshop Model) 웹서버 작업할 때 쓸 기법 다오는 너무 클래식한 기법  

class AddressBookEntry:
    def __init__(self, num, name, phone, email, addr):
        self.num = num
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr 

    def __str__(self):
        return f'<AddressBookEntry {self.num}, {self.name}, {self.phone}, {self.email}, {self.addr}>'

    def __repr__(self):
        return f'<AddressBookEntry {self.num}, {self.name}>'
    