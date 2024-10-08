from PySide6.QtWidgets import QMainWindow, QMenu,QTableWidgetItem, QWidget, QHBoxLayout,QPushButton,QVBoxLayout
from PySide6.QtGui import QAction,QIcon
from pinaka_finaleeee_ui import Ui_MainWindow
from RESIDENTDIALOG_FINALE_ui import Ui_ResidentsDialog
from PySide6.QtWidgets import QDialog
import mysql.connector

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

        
        self.list_official.clicked.connect(self.switch_to_page_2)
        self.official_end.clicked.connect(self.switch_to_page_3)
        

        
        self.list_residents.clicked.connect(self.switch_to_page_4)
        self.archieve_residents.clicked.connect(self.switch_to_page_5)

        self.blotter_1.clicked.connect(self.switch_to_page_6)
        self.blotter_3.clicked.connect(self.switch_to_page_6)



        self.settings_1.clicked.connect(self.switch_to_page_7)
        self.settings_2.clicked.connect(self.switch_to_page_7)
        
        #Dialogs
        self.add_residents.clicked.connect(self.open_addResidentDialog_dialog)
        self.add_official.clicked.connect(self.open_addOfficialDialog_dialog)
        
        #CONNECT TO MYSQL SERVER AND CREATE DATABASE IF IT DONEST EXIST
        self.create_connection()
        
        #CREATE RESIDENT TABLE
        self.create_resident_table()
        
        #Load residnet info  to Qtable
        self.load_resident_info()
        self.select_residentgender.currentIndexChanged.connect(self.load_resident_info)

        
        self.residents_table.setColumnWidth(0, 150)
        self.residents_table.setColumnWidth(1, 150)
        self.residents_table.setColumnWidth(2, 150)
        self.residents_table.setColumnWidth(3, 150)
        self.residents_table.setColumnWidth(4, 150)
        self.residents_table.setColumnWidth(5, 150)
        self.residents_table.setColumnWidth(6, 150)
        self.residents_table.setColumnWidth(7, 150)
        self.residents_table.setColumnWidth(8, 150)
        self.residents_table.setColumnWidth(9, 150)
        self.residents_table.setColumnWidth(10, 150)
        self.residents_table.setColumnWidth(11, 150)
        self.residents_table.setColumnWidth(12, 150)
        self.residents_table.setColumnWidth(13, 150)
        self.residents_table.setColumnWidth(14, 150)
        
        
        

    # Methods to switch to various pages
    def switch_to_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_page_2(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_page_3(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_page_4(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_page_5(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_page_6(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_page_7(self):
        self.stackedWidget.setCurrentIndex(6)



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


        if text == "List of Official":
            self.switch_to_page_2()
        elif text == "Archieve Official":
            self.switch_to_page_3()
        elif text == "List of Residents":
            self.switch_to_page_4()
        elif text == "Archive Residents":
            self.switch_to_page_5()
            
#CREATE DATABASE CONNECTION
    def create_connection(self):
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "brgy_profiling"
        
        # Establish connection to MySQL
        self.mydb = mysql.connector.connect(
            host=host_name, 
            user=user_name, 
            password=mypassword
        )
        
        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
        
        # Connect to the created database
        self.mydb = mysql.connector.connect(
            host=host_name, 
            user=user_name, 
            password=mypassword, 
            database=database_name
        )
        
        return self.mydb
    
        #CREATE RESIDENT TABLE SELF
    
    def create_resident_table(self):
        # Get the database connection and create a cursor
        connection = self.create_connection()  # Get the connection object
        cursor = connection.cursor()  # Call cursor() method
        
        # The query
        create_resident_table_query = f"""
    CREATE TABLE IF NOT EXISTS residents (
        `resident_id` INT NOT NULL AUTO_INCREMENT, 
        `brgy_id` INT NOT NULL,                     
        `admin_id` INT NOT NULL,                    
        `Fname` VARCHAR(50) DEFAULT NULL,           
        `Lname` VARCHAR(50) NOT NULL,               
        `mid_ini` CHAR(1) NOT NULL,                 
        `Age` INT(3) NOT NULL,                      
        `sex` ENUM('Male', 'Female') NOT NULL,      
        `PWD` ENUM('yes', 'no') NOT NULL,           
        `birthplace` VARCHAR(50) NOT NULL,          
        `Birth_date` DATE NOT NULL,                 
        `blood_type` VARCHAR(3) NOT NULL,           
        `Civil_status` ENUM('Single', 'Married', 'Divorced', 'Separated', 'Widowed') NOT NULL,  
        `contact_no` BIGINT(14) NOT NULL,           
        `email` VARCHAR(50) NOT NULL,
        `adrrss` VARCHAR(50) NOT NULL,               
        `isactive` ENUM('yes', 'no') NOT NULL,      
        PRIMARY KEY (`resident_id`)                 
    )
"""

        # Execute the query
        cursor.execute(create_resident_table_query)

        # Commit changes and close the connection
        self.mydb.commit()
        self.mydb.close()          
            

 
            
            

#Open dialog for inserting residents
#Open dialog for inserting residents


    def open_addResidentDialog_dialog(self):
        from RESIDENTDIALOG_FINALE_ui import Ui_ResidentsDialog
        from PySide6.QtWidgets import QDialog


        addResident_dialog = Ui_ResidentsDialog(self)
        result = addResident_dialog.exec()

        if result == QDialog.Accepted:  # Check if the dialog was accepted
            print("Dialog accepted")
            # Perform the actions to add the resident here
        else:
            print("Dialog rejected")
        
        
    def open_addOfficialDialog_dialog(self):
            
        from OFFICIALDIALOG_FINAL_ui import Ui_OfficialDialog
            
        addOffcial_dialog =  Ui_OfficialDialog(self)
        result = addOffcial_dialog.exec()
            
        if result == Ui_OfficialDialog.accepted():
            pass    


        #LOAD STUDENT INFORAMTION
    def load_resident_info(self):
        self.residents_table.setRowCount(1)
        
        # Fetch data based on the selected gender in the combo box
        selected_sex = self.select_residentgender.currentText()
        data = self.get_data_from_table(selected_sex)
        
        # Populate the table with the filtered data
        for row_index, row_data in enumerate(data):
            self.residents_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):  # Corrected to use row_data
                item = QTableWidgetItem(str(cell_data))  # Removed colon
                self.residents_table.setItem(row_index, col_index, item)
                
                # Create a custom widget with two buttons, aligned horizontally
                double_button_widget = DoubleButtonWidgetResident(row_index, row_data)
                
                # Set this custom widget in the designated cell
                self.residents_table.setCellWidget(row_index, 14, double_button_widget)

                
                
        
    
    def get_data_from_table(self, selected_sex):
        connection = self.create_connection()  # Create a connection
        cursor = connection.cursor()  # Create the cursor

        # Use a parameterized query to prevent SQL injection and errors
        query = "SELECT resident_id, Fname, Lname, mid_ini, Age, sex, PWD, birthplace, Birth_date, blood_type, Civil_status, contact_no, email, adrrss, isactive FROM residents WHERE sex = %s"
        cursor.execute(query, (selected_sex,))  # Make sure to pass the gender correctly
        data = cursor.fetchall()

        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        return data

             
             
    #Double button claass                 
                    
    

class DoubleButtonWidgetResident(QWidget):    
    def __init__(self, row_index, row_data):
        super().__init__()  
        
        self.row_index = row_index
        self.row_data = row_data
        
        self.resident_name = self.row_data[0]
        
        layout = QHBoxLayout(self)
            
        # Create a blue Edit button
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue;")
        self.edit_button.setFixedSize(61, 31)

        # Create a red Delete button
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)

        # Set icons for the buttons
        edit_icon = QIcon(r"D:\final\images\icons8-edit-24 (1).png")  # Use raw string or forward slashes
        self.edit_button.setIcon(edit_icon)

        delete_icon = QIcon(r"D:\final\images\icons8-delete-30.png")  # Use raw string or forward slashes
        self.delete_button.setIcon(delete_icon)

        # Add buttons to the layout
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)


        
        
        
        
            