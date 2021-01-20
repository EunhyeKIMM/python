from app_base import Application
import MySQLdb
from dao import AddressBookDao
from models import AddressBookEntry

class AddrBookApp(Application):
    def __init__(self):
        super().__init__()
        print(self.config)
        self.db = MySQLdb.connect(db=self.config['db'],
                                host=self.config['host'],
                                user=self.config['user'], 
                                passwd=self.config['passwd'], 
                                charset='utf8', use_unicode=True)
        self.cursor = self.db.cursor()
        self.PERPAGE = 20   # 한 페이지 당 출력 건수 
        self.addrbook_dao = AddressBookDao(self.cursor)

    def create_menu(self, menu):
        menu.add('목록', self.print_list)
        menu.add('상세보기', self.print_detail)
        menu.add('검색', self.search)
        menu.add('추가', self.add)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)


    def print_list(self):
        page = int(input('페이지:'))
        pagination = self.addrbook_dao.get_page(page, self.PERPAGE)
        print('='*60)
        print('주소록')
        print('='*60)
        for e in pagination.datas:
            print(f'{e.num:8d} {e.name:20s} {e.phone:16s} {e.email:20s} {e.addr}')
        print('='*60)
        print(f'{page}/{pagination.total_page} (총 {pagination.total_count} 건)')
        print('='*60)
        # 현재페이지/전체페이지수 (총 데이터 건수)


    def print_detail(self):
        num = int(input('번호:'))
        row = self.addrbook_dao.get(num)
    
        # row 출력
        if not row:
            print(f'{num}은 없습니다.')
            return 
        print(f'num: {row.num}')
        print(f'이름: {row.name}')
        print(f'전화번호: {row.phone}')
        print(f'mail: {row.email}')
        print(f'주소: {row.addr}')


    def search(self):
        keyword = input('검색어:')
        rows = self.addrbook_dao.search(keyword)
        # rows 출력
        print('='*60)
        print(f'검색결과({keyword})')
        print('='*60)
        for e in rows:
            print(f'{e.num:8d} {e.name:20s} {e.phone:16s} {e.email:20s} {e.addr}')
        print('='*60)

    def add(self):
        print('새 주소록 항목 추가')
        name = input('이름:')
        phone = input('전화번호:')
        email = input('email:')
        addr = input('주소:')
        self.addrbook_dao.add(name, phone, email, addr)
        self.db.commit()

    def update(self):
        num = int(input('번호:'))
        row = self.addrbook_dao.get(num)
        
        print('주소록 항목 수정')
        name = input(f'이름({row.name}):')
        if name.strip() == '':
            name = row.name
        phone = input(f'전화번호({row.phone}):')
        if phone.strip() == '':
            phone = row.phone
        email = input(f'email({row.email}):')
        if email.strip() == '':
            email = row.email
        addr = input(f'주소({row.addr}):')
        if addr.strip() == '':
            addr = row.addr
        self.addrbook_dao.update(num, name, phone, email, addr)
        self.db.commit()

    def delete(self):
        num = int(input('번호:'))
        row = self.addrbook_dao.get(num)

        ans = input(f'{row.name}을 삭제할까요?(Y/N)')
        if ans == 'Y':
            self.addrbook_dao.delete(num)
            self.db.commit()

    def destroyed(self):
        self.cursor.close()
        self.db.close()    

if __name__ == "__main__":
    app = AddrBookApp()    
    app.run()