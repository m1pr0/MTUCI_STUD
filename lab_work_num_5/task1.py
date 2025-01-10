class book:
    '''1.	Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).'''
    title = None
    author = None
    year = None

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

book_1 = book()
book_1.title = 'OMG'
book_1.author = 'Mister Brown'
book_1.year = 1905

print(book_1.get_info())
