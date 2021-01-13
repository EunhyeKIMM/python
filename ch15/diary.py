class DiaryApp(Applicatoin):
    def __init__(self):
        super().__init()

    def create_menu(self, menu):
        menu.add('쓰기', self.writeToday)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)

    def writeToday(self):
        print('오늘 일기 쓰기')

    def update(self):
        print('일기 수정')

    def delete(self):
        print('일기 삭제')

    def main():
        app = DiaryApp()
        app.run()