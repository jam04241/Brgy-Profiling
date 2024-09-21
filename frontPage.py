from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from menu import Ui_MainWindow

class MySideBar (QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Barangay Profiling")
        
        
        self.icon_only_widget.setHidden(True)
        
        self.officials_dropdown.setHidden(True)
        self.residents_dropdown.setHidden(True)
        
        self.dashboard_1.clicked.connect(self.switch_to_page)
        self.dashboard_2.clicked.connect(self.switch_to_page)
        
        self.official_1.clicked.connect(self.switch_to_page2)
        self.official_2.clicked.connect(self.switch_to_page2)    
        self.new_official.clicked.connect(self.switch_to_page3)
        self.list_official.clicked.connect(self.switch_to_page4)
        self.end_term.clicked.connect(self.switch_to_page5)
        
        
        
        self.resident_1.clicked.connect(self.switch_to_page6)
        self.resident_2.clicked.connect(self.switch_to_page6)
        self.new_resident.clicked.connect(self.switch_to_page7)
        self.all_resident.clicked.connect(self.switch_to_page8)
        self.archieve_resident.clicked.connect(self.switch_to_page9)
        
        
        
        
        self.certificate_1.clicked.connect(self.switch_to_page10)
        self.certificate_2.clicked.connect(self.switch_to_page10)
        
        self.blotter_1.clicked.connect(self.switch_to_page11)
        self.blotter_2.clicked.connect(self.switch_to_page11)
        
        self.staff_1.clicked.connect(self.switch_to_page12)
        self.staff_2.clicked.connect(self.switch_to_page12)
        
        
        
    def switch_to_page(self):
            self.stackedWidget.setCurrentIndex(0);
                
    def switch_to_page2(self):
            self.stackedWidget.setCurrentIndex(1);
    def switch_to_page3(self):
            self.stackedWidget.setCurrentIndex(2);
    def switch_to_page4(self):
            self.stackedWidget.setCurrentIndex(3); 
    def switch_to_page5(self):
            self.stackedWidget.setCurrentIndex(4);   
    def switch_to_page6(self):
            self.stackedWidget.setCurrentIndex(5);      
    def switch_to_page7(self):
            self.stackedWidget.setCurrentIndex(6);
    def switch_to_page8(self):
            self.stackedWidget.setCurrentIndex(7);
    def switch_to_page9(self):
            self.stackedWidget.setCurrentIndex(8);  
    def switch_to_page10(self):
            self.stackedWidget.setCurrentIndex(9);  
    def switch_to_page11(self):
            self.stackedWidget.setCurrentIndex(10);  
    def switch_to_page12(self):
            self.stackedWidget.setCurrentIndex(11);  
    def switch_to_page13(self):
            self.stackedWidget.setCurrentIndex(12);
    def switch_to_page14(self):
            self.stackedWidget.setCurrentIndex(13);  
    def switch_to_page15(self):
            self.stackedWidget.setCurrentIndex(14);
    def switch_to_page16(self):
            self.stackedWidget.setCurrentIndex(15);                                    