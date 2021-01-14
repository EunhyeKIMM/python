# 모델(Model) 객체
class Configuration:
    # csv 파일 경로명. encoding, ... -> 설정 파일에 분석해서 초기화...
    def __init__(self):
        config = self.load()
        self.fname = config['FNAME']
        self.encoding = config['ENCODING']

    def load(self):
        config ={}
        with open('config.ini', 'rt') as f:
            entries = f.readlines()
            for entry in entries:
                key, value = entry.split('=')
                config[key.strip()] = value.strip()
        return config 

    def __str__(self):
        return f'<Configuration fname: {self.fname}. encoding: {self.encoding}>'


import sys
class MenuItem:
    def __init__(self, title, func):
        self.title = title
        self.func = func

    def __str__(self):
        return f'(MenuItem {self.title}'

    def __repr__(self):
        return f'(MenuItem {self.title}'

class Menu:
    def __init__(self):
        self.menu_items = []

    def add(self, title, func):
        menu_item = MenuItem(title, func)
        self.menu_items.append(menu_item)

    def select_menu(self):
        for ix, menu_item in enumerate(self.menu_items):
            print(f'{ix}){menu_item.title}', end=' ')
        print()
        menu = int(input('입력: '))
        return menu

    def run(self, menu):
        if 0 <= menu < len(self.menu_items):
            menu_item = self.menu_items[menu]
            menu_item.func()
        else: 
            print('잘못된 메뉴입니다.')


# 탬플릿 패턴 
class Application:
    def __init__(self):
        self.config = Configuration()
        self.menu = Menu()
        self.create_menu(self.menu)
    
    def create_menu(self, menu):
        pass

    def run(self):
        while True: 
            menu = self.menu.select_menu()
            self.menu.run(menu) 

    def destroyed(self):
        pass 

    def exit(self):
        ans = input(f'종료할까요? (Y/N)')
        if ans == 'Y':
            self.destroyed()
            sys.exit(0)