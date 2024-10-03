from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
import sys

#app = QApplication(sys.argv)

#window = MySideBar()

#window.show()
#app.exec()


class App:
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)

        self.window = MySideBar()

        self.window.show()
        self.app.exec()
        
if __name__ == "__main__":
    app = App()