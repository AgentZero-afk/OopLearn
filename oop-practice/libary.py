class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self._author = author
        self._year = year

    def get_info(self):
        return f'"{self.title}" ({self._author}, {self._year})'


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def get_info(self):
        return f'{super().get_info()}, ISBN: {self.isbn}'


class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number):
        super().__init__(title,editor,year)
        self.issue_number = issue_number

    # Используется конструкция временой подмены, (мутация не оч хорошо, лучше переписать базовый класс)
    def get_info(self):
        original_author = self._author
        try:
            self._author = f"Ред. {original_author}"
            base_info = super().get_info()
        finally:
            self._author = original_author
        return f'{base_info}, Выпуск №{self.issue_number}'



book = Book("Война и мир", "Лев Толстой", 1869, "978-5-389-06254-2")
magazine = Magazine("National Geographic", "Сьюзан Голдберг", 2021, 8)

publications = [book, magazine]
for pub in publications:
    print(pub.get_info())
