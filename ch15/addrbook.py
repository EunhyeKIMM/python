import sys
import traceback

def load_config():
    config ={}
    with open('config.ini', 'rt') as f:
        entries = f.readlines()
        for entry in entries:
            key, value = entry.split('=')
            config[key] = value
    return config

def load(fpath, encoding):
    with open(fpath, "rt", encoding=encoding) as f:    
        return f.readlines()

def init():
    config = load_config()
    lines = load(config['FNAME'], config['ENCODING'])
    book = make_book(lines)
    return book, config 

def make_book(lines):
    book ={}
    for line in lines[1:]:   #헤더 제외
        name, phone, email, addr = line.split(',')
        addr = addr.strip()
        book[name] = [phone, email, addr]
    return book

def select_menu():
    print('1)목록, 2)상세보기, 3)추가, 4)수정, 5)삭제, 6)종료')
    menu = int(input('입력: '))
    return menu

# 주소록 목록 출력
def print_book(book):
    # 정렬해서 출력
    names = list(book.keys())
    names.sort()
    print('='*50)
    print('주소록')
    print('='*50)
    # 실제 데이터 출력
    #for name, info in book.items:
    for name in names:   # .keys(), values(), .items()
        info = book[name]   # 정렬을 위해서
        print(f'{name} : {info[0]}, {info[1]}, {info[2]}')

    print('-'*50)

def print_detail(book):
    name = input('이름: ')  # 검색
    if name not in book:
        print(f'{name}은 목록에 없습니다.')
    else:
        info = book[name]   # get()/ in
        print(f'{name} : {info[0]}, {info[1]}, {info[2]}')

def add_entry(book):
    name = input('이름: ')
    if name in book:
        print(f'{name}은 이미 존재합니다.')
        return

    phone = input('전화번호: ')
    email = input('email: ')
    addr = input('주소: ')
    # 사전에 추가 
    book[name] = [phone, email, addr]   # .update() 매서드 시용가능

def update_entry(book):
    name = input('이름: ')
    if name in book:
        print(f'{name}은 이미 존재합니다.')
        return

    old_phone, old_email, old_addr = book[name]
    print('변경이 없는 경우 그냥 엔터')
    phone = input(f'전화번호({old_phone}): ')
    if phone.strip() == '': # 내용없이 엔터를 친 경우
        phone = old_phone
    email = input(f'email({old_email}): ')
    if email.strip() == '': # 내용없이 엔터를 친 경우
        email = old_email
    addr = input(f'주소({old_addr}): ')
    if addr.strip() == '': # 내용없이 엔터를 친 경우
        addr = old_addr
    # 사전에 추가 
    book[name] = [phone, email, addr]

def delete_entry(book):
    name = input('이름: ')
    if name in book:
        print(f'{name}은 목록에 없습니다.')
        return    
    
    del book[name]

def save(book, fpath, encoding):
    # 문자열 .join(시퀀스)
    # 1 = [1, 2] : ','.join(1) ==> '1, 2'

    with open(fpath, 'wt', encoding=encoding) as f:
        f.write('이름,전화번호,email,주소\n')
        for name, value in book.items():
            scores = ','.join(value)
            line = f'{name},{scores}\n'
            f.write(line)
    

def exit(book, fpath, encoding):
    # 종료 여부 질의, 업데이트된 주소록을 저장, 파일의 경로
    ans = input('종료할까요?(Y/N')
    if ans == 'N':
        return 
    
    save(book, fpath, encoding)
    sys.exit(0)



def run(self, menu):
    # 해당 메뉴를 실행
    if menu == 1:
        self.print_book()
    elif menu == 2:
        self.print_detail()
    elif menu == 3:
        self.add_entry
    elif menu == 4:
        self.update_entry()
    elif menu == 5: # 삭제
        self.delete_entry()
    elif menu == 6: # 종료
        self.exit()
    else:
        print("잘못 선택했습니다.")    

def main():
    try:
        book, config = init()
        while True:
            menu = select_menu()
            run(menu, book, config)
            
    except Exception as e:
        print('예외', e)
        #traceback.print_stack() # 예외 위치까지 오는데 거친 함수 목록 출력
        #traceback.print_exc()   # 구체적인 예외 내용을 출력

main()

