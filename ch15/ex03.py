# 주소록 앱 ---> 객체 지향적으로...

# 1. 문제 파악
# 2. 문제 해결을 위해 필요한 객체가 뭐냐?
# 2.1 어떤 정보를 다루느냐?
#     1) 이름, 이메일, 전화번호, 주소--> 주소록 정보
#     2) 설정 정보(파일명, encoding 방식..)
# 2.2 단위 데이터의 형태가 어떻게 되는가?
#     1) 하나의 주소록 정보: 이름, 이메일, 전화번호, 주소 --> 단위 데이터
#     2) 설정 정보
# 2.3 데이터의 개수, 어떻게 관리할 것인가?
#     1) 주소록 정보 N개 --> 콜렉션
#     2) 설정 정보 1개 -> 단일 변수


class AddressBookEntry:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def __str__(self):
        return f'<AddressBookEntry {self.name}, {self.phone}, {self.email}, {self.addr}>'

    def __repr__(self):
        return f'<AddressBookEntry {self.name}>'

# config = Configuration()
# print(config)

# entry = AddresBookEntry('홍길동', '010-1111-1111', 'hong@naver.com', '서울')
# print(entry)
# print([entry])

class AddressBook:  # 프로토타입 객체 
    def __init__(self):
        self.book = []

    def load(self, config):
        with open(config.fname, 'rt') as f:
            lines = f.readlines()[1:]   # 헤더(맨 윗줄)는 제외하겠다.
            for line in lines:
                name, phone, email, addr = line.split(',')
                # AddressBookEntry를 생성하여 self.book에 추가
                entry = AddressBookEntry(name, phone, email, addr)
                self.book.append(entry)
        # 정렬
        self.book.sort(key=lambda a: a.name)

    def save(self, config):
        with open(config.fname, 'wt') as f:
            f.write('이름, 전화번호, email, 주소\n')
            for entry in self.book:
                # line = ','.join(entry)
                line = f'{entry.name}, {entry.phone}, {entry.email}, {entry.addr}'
                f.write(line + '\n')

    def add(self, name, phone, email, addr):
        entry = AddressBookEntry(name, phone, email, addr)
        self.book.append(entry)
        self.book.sort(key=lambda a: a.name)

    def delete(self, index):
        del self.book[index]

    def update(self, index, name, phone, email, addr):
        self.book[index].name = name
        self.book[index].phone = phone
        self.book[index].email = email
        self.book[index].addr = addr

        self.book.sort(key=lambda a: a.name)

    def search(self, keyword):
        # result = []
        # for entry in self.book:
        #     if entry.name.find(keyword) !=-1:
        #         result.append(entry)
        #     return result 
        return list(filter(lambda entry: entry.name.find(keyword) != -1, self.book))
        

    def __str__(self):
        return f'<AddressBook {self.book}>'

import sys
# Configuration  설정 정보 담당
# AddressBookEntry 한 사람 주소 정보 담당
# AddressBook 목록 관리

# 객제 지향 설계 원칙
# 1) SRP(Single Resposibity Principle) 단일 책임의 원칙
# 2) OCP(Open Close Principle): 확장에는 열려 있고, 변화에는 닫혀있음을 의미




class Application:
    def __init__(self):
        self.config = Configuration()
        self.addressbook = AddressBook()
        self.addressbook.load(self.config)

        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self, menu):    
        # 메뉴를 구성해야 합니다.
        menu.add('목록', self.print_book)
        menu.add('상세보기', self.print_detail)
        menu.add('검색', self.search)
        menu.add('추가', self.add)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)

    # def select_menu(self):
    #     print('1)목록, 2)상세보기, 3)추가, 4)수정, 5)삭제, 6)종료')
    #     menu = int(input('입력: '))
    #     return menu

    def run(self):
        while True: 
            menu = self.menu.select_menu()
            self.menu.run(menu)
    
    def print_book(self):
        print('='*50)
        print('주소록')
        print('='*50)
        for index, entry in enumerate(self.addressbook.book, 1):
            print(f'{index:02d}{entry.name}: {entry.phone}, {entry.email}, {entry.addr}', end = '')

        print('-'*50)

    def print_detail(self):
        index = int(input('대상 선택(번호): '))
        entry = self.addressbook.book[index-1]
        # entry 포맷팅해서 출력 
        print(f'이름: {entry.name}')
        print(f'전화번호: {entry.phone}')
        print(f'email: {entry.email}')
        print(f'주소: {entry.addr}')

    # 검색방법: 키워드 검색... '길동' --> [홍길동, 고길동]
    def search(self):
        keyword = input('검색어: ')
        result = self.addressbook.search(keyword)
        # result 출력
        print('='*50)
        print(f'검색결과 ({len(result)}건)')
        print('='*50)
        for index, entry in enumerate(result, 1):
            print(f'{index:02d}{entry.name}: {entry.phone}, {entry.email}, {entry.addr}', end = '')

        print('-'*50)

    def add(self):
        print('새 주소록 항목 추가')
        name = input('이름:')
        phone = input('전화번호:')
        email = input('email:')
        addr = input('주소:')
        self.addressbook.add(name, phone, email, addr)

    def update(self):
        index = int(input('대상 선택(번호): '))
        entry = self.addressbook.book[index-1]
        print('주소록 항목 수정')
        name = input(f'이름({entry.name}):')
        if name.strip() == '':
            name = entry.name
        phone = input(f'전화번호({entry.phone}):')
        if phone.strip() == '':
            phone = entry.phone
        email = input(f'email({entry.email}):')
        if email.strip() == '':
            email = entry.email
        addr = input(f'주소({entry.addr}):')
        if addr.strip() == '':
            addr = entry.addr

        self.addressbook.update(index-1, name, phone, email, addr)

    def delete(self):
        index = int(input('대상 선택(번호): '))
        entry = self.addressbook.book[index-1]
        ans = input(f'{entry.name}을 삭제할까요?(Y/N)')
        if ans == 'Y':
            self.addressbook.delete(index-1)
            # del self.addressbook[index-1] 도 가능 하지만 단일 책임의 원칙을 위반 
        
    def exit(self):
        ans = input(f'종료할까요? (Y/N)')
        if ans == 'Y':
            sys.exit(0)

def main():
    app = Application()
    app.run()


main()

# 기존 방법: 절차 중심 --> Top down
# OOP: 객체지향 방법 --> Bottoom up
# Application
#       configuration
# 
