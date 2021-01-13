import sys

class Application:
    def __init__(self):
        self.config = Configraton()
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