import sys
from PySide6.QtWidgets import QApplication
from frontPage import MySideBar  # Assuming this is where your main window (MySideBar) is

app = QApplication(sys.argv)
 
window = MySideBar()
 
window.show()
app.exec()  