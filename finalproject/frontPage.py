from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from final1 import Ui_MainWindow
from finalOfficialResident import Ui_ResidentsDialog
from PySide6.QtWidgets import QDialog


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Barangay Profiling")

        self.icon_only_widget.setHidden(True)
        self.officials_dropdown.setHidden(True)
        self.residents_dropdown.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_page)
        self.dashboard_2.clicked.connect(self.switch_to_page)

        
        self.list_official.clicked.connect(self.switch_to_page3)
        self.official_end.clicked.connect(self.switch_to_page4)
        

        
        self.list_residents.clicked.connect(self.switch_to_page6)
        self.archieve_residents.clicked.connect(self.switch_to_page7)

        self.blotter_1.clicked.connect(self.switch_to_page8)
        self.blotter_3.clicked.connect(self.switch_to_page8)



        self.settings_1.clicked.connect(self.switch_to_page10)
        self.settings_2.clicked.connect(self.switch_to_page10)
        
        #Dialogs
        self.add_residents.clicked.connect(self.open_addResidentDialog_dialog)
        self.add_official.clicked.connect(self.open_addOfficialDialog_dialog)
        
        
        
        

    # Methods to switch to various pages
    def switch_to_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_page3(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_page4(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_page6(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_page7(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_page8(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_page9(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_page10(self):
        self.stackedWidget.setCurrentIndex(8)

    # Methods to show context menu
    def offy_2_context_menu(self):
        self.show_custom_context_menu(self.offy_2, ["Add Official", "List of Official", "Official End Term"])

    def residents_context_menu(self):
        self.show_custom_context_menu(self.residents_2, ["Add Residents", "List of Residents", "Archive Residents"])

    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)
        menu.setStyleSheet(
        """
        QMenu { 
            background-color: black;
            color: white;
        }
        QMenu::selected {
            background-color: white;
            color: #12B298;
        }
        """)

        # Add action for menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        menu.exec(button.mapToGlobal(button.rect().bottomLeft()))

    def handle_menu_item_click(self):
        text = self.sender().text()

        if text == "Add Official":
            self.switch_to_page2()
        elif text == "List of Official":
            self.switch_to_page3()
        elif text == "Official End Term":
            self.switch_to_page4()
        elif text == "Add Residents":
            self.switch_to_page5()
        elif text == "List of Residents":
            self.switch_to_page6()
        elif text == "Archive Residents":
            self.switch_to_page7()
            
            

 
            
            

#Open dialog for inserting residents
#Open dialog for inserting residents
    def open_addResidentDialog_dialog(self):
        
        from finalOfficialResident import Ui_ResidentsDialog
        
        addResident_dialog = Ui_ResidentsDialog(self)
        result = addResident_dialog.exec()
        
        if result == Ui_ResidentsDialog.accepted():
            pass
    
    
    def open_addOfficialDialog_dialog(self):
        
        from finalOfficialDialog import Ui_OfficialDialog
        
        addOffcial_dialog =  Ui_OfficialDialog(self)
        result = addOffcial_dialog.exec()
        
        if result == Ui_OfficialDialog.accepted():
            pass    



    

        
        
        
        
        
            