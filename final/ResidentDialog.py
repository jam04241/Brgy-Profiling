# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResidentDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector
from random import randint
from datetime import datetime


class Ui_ResidentsDialog(QDialog):
    def _init_(self, parent=None):
        super().__init__(parent)
        
            
            
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
" \n"
"background-color:white;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"border: 1px solid gray;\n"
"border-radius:6px;\n"
"padding-left: 15px;\n"
"height: 35px;\n"
"}\n"
"\n"
"QDateEdit{ \n"
"border: 1px solid gray;\n"
"border-radius:6px;\n"
"padding-left: 15px;\n"
"height: 35px;\n"
"}\n"
"\n"
"QComboBox{ \n"
"border: 2px solid white;\n"
"border-radius:6px;\n"
"padding-left: 1px 18px 1px 3px;\n"
"height: 35px;\n"
"background-color:black;\n"
"color:white;\n"
"padding-left:15px;\n"
"selection-background-color: #298089;\n"
"}")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 541, 21))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 261, 31))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 90, 491, 431))
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.firstname_lineEdit = QLineEdit(self.widget)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")

        self.verticalLayout.addWidget(self.firstname_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lastname_lineEdit = QLineEdit(self.widget)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")

        self.verticalLayout_2.addWidget(self.lastname_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_10)

        self.age_lineEdit = QLineEdit(self.widget)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.verticalLayout_9.addWidget(self.age_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.PWD_comboBox = QComboBox(self.widget)
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.setObjectName(u"PWD_comboBox")
        self.PWD_comboBox.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.PWD_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.widget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.birthplace_lineEdit = QLineEdit(self.widget)
        self.birthplace_lineEdit.setObjectName(u"birthplace_lineEdit")

        self.verticalLayout_3.addWidget(self.birthplace_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.address_lineEdit = QLineEdit(self.widget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")

        self.verticalLayout_8.addWidget(self.address_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.contact_lineEdit = QLineEdit(self.widget)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")

        self.verticalLayout_4.addWidget(self.contact_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_11)

        self.emailaddress_lineEdit = QLineEdit(self.widget)
        self.emailaddress_lineEdit.setObjectName(u"emailaddress_lineEdit")

        self.verticalLayout_10.addWidget(self.emailaddress_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(330, 541, 191, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancel_button = QPushButton(self.widget1)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
" background-color: #585858;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.add_button = QPushButton(self.widget1)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.add_button)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, ResidentsDialog):
        ResidentsDialog.setWindowTitle(QCoreApplication.translate("ResidentsDialog", u"ResidentDialog", None))
        self.label.setText(QCoreApplication.translate("ResidentsDialog", u"Add New Official", None))
        self.label_2.setText(QCoreApplication.translate("ResidentsDialog", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("ResidentsDialog", u"Last Name", None))
        self.label_10.setText(QCoreApplication.translate("ResidentsDialog", u"Age", None))
        self.label_6.setText(QCoreApplication.translate("ResidentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("ResidentsDialog", u"GENDER", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("ResidentsDialog", u"Select", None))
        self.PWD_comboBox.setItemText(0, QCoreApplication.translate("ResidentsDialog", u"PWD's", None))
        self.PWD_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Yes", None))
        self.PWD_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"No", None))

        self.label_8.setText(QCoreApplication.translate("ResidentsDialog", u"Date of Birth", None))
        self.label_4.setText(QCoreApplication.translate("ResidentsDialog", u"Birth Place", None))
        self.label_9.setText(QCoreApplication.translate("ResidentsDialog", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("ResidentsDialog", u"Contact", None))
        self.label_11.setText(QCoreApplication.translate("ResidentsDialog", u"Email Address", None))
        self.cancel_button.setText(QCoreApplication.translate("ResidentsDialog", u"Cancel", None))
        self.add_button.setText(QCoreApplication.translate("ResidentsDialog", u"Add Official", None))
    # retranslateUi
    
    #Add new resident when toplokon ang button
        self.add_button.clicked.connect(self.add_resident)
        self.cancel_button.clicked.connect(self.close)
        
    
    
    # Create Database connection
    def create_connection(self):
        # Replace these with your actual MySQL server details
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "your_database_name"

        try:
            # Establish connection to MySQL server
            mydb = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=mypassword,
            )
            
            # Create a cursor to execute SQL queries
            cursor = mydb.cursor()

            # Create the database if it doesn't exist
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
            cursor.close()  # Close cursor after database creation
            
            # Connect to the created database
            mydb = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=mypassword,
                database=database_name,
            )

            return mydb
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
        #INSERT NEW RESIDENT
        def insert_new_resident(self):
            
            try:
                cursor = self.create_connection().cursor()
                
                gender = self.gender_comboBox.currentText()
                resident_id = self.generate_residentId(gender)
                
                birthday_self.handleDateChange()
                
                #birthday is a Qdate  objext
                birth_date = self.dob_dateEdit()
                age = self.calculate_age(birth_date)
                
                #Create list of resident information
                self.new_resident = [
                    self.firstname_lineEdit.text(),
                    self.lastname.lineEdit.text(),
                    resident_id,
                    self.gender_comboBox.currentText(),
                    birthday,
                    age,
                    self.birthplace_lineEdit.text(),
                    self.address_lineEdit.text(),
                    self.contact_lineEdit.text(),
                    self.emailaddress_lineEdit.text(),
                    
                ]
                
                # to insert multiple rows in the mysql database
                insert_resident_query = f"""INSERT INTO residents_table(ID,FirstName,LastName,Age,Gender,PWD,DateofBirth,BirthPlace,Address,Contact,Email Address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
                
                cursor.execute(insert_resident_query, self.new_residents)
                self.show_inserted_message()
                self.mydb.commit()
                self,mydb.close
            
            except mysql.connector.Error as err:
                #Handle ERRORS
                print(f"Error: {err}")
              
            
        def generate_residentId(self, gender):
            
            cursor = self.create_connection().cursor()
            
            while True:
                if gender == "Male":
                    id_start_value = '24' + '/U/M'
                else:
                    id_start_value = '24' + '/U/F'  
                      
                random_value = self.generate_randomNumber()
                resident_id = id_start_value + random_value
        
                curser.execute(f"SELECT  resident_id FROM residents_table WHERE resident_id = %s",(resident_id))
                existing_id = curson.fetchone()
                
                if not existing_id:
                    return resident_id
        
        
        
        def generate_randomNumber(self):
            
            number = randint(1,1000)
            random_number = f"{number:04d}"
            return random_number
        
        def handleDateChange(self):
            
            #convert Qdate  to a string format "YYY-mm-dd"
            selected_date = self.dob_dateEdit.date()
            self.date_string = selected_date.toString(Qt.ISODate)
            
            return self.date_string
        
        def calculate_age(self,birth_date):
            
            #get the current date
            current_date = datetime.now().date()
            
            #create a daTE OBJECT for the birthdate
            birth_datetime = datetime(birth_date.year(), birth_date.monnth(),birth_date.day()).date()
            
            #calculate the difference in years
            age = current_date.year - birth_datetime.year 
            
            #check if birithday has occured this year
            if (current_date.month,current_date.day ) < (birth_date.month, birth_date.day):
                age-= 1
                
            return age
        
        def show_inserted_message(self):
            
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Success")
            msg_box.setText(self.firstname_lineEdit.text(), self.lastname_lineEdit.text() + "inserted into the database")
            msg_box.exec()
            
        def add_resident(self):
            self.insert_new_resident()
            self.accept()
                                