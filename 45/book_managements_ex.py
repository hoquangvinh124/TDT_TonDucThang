from book_managements import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.books = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def add_book(self, isbn, title, author, year, publisher):
        self.books.append({isbn, title, author, year, publisher})
        return 

    def show(self):
        self.MainWindow.show()