# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RESIDENTDIALOG_FINALE.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget,QMessageBox)
import mysql.connector


class Ui_ResidentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(523, 762)
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
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 261, 31))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 230, 511, 67))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_14.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_14)

        self.middle_lineEdit = QLineEdit(self.layoutWidget)
        self.middle_lineEdit.setObjectName(u"middle_lineEdit")

        self.verticalLayout_13.addWidget(self.middle_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_10)

        self.age_lineEdit = QLineEdit(self.layoutWidget)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.verticalLayout_9.addWidget(self.age_lineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.sex_comboBox = QComboBox(self.layoutWidget)
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.setObjectName(u"sex_comboBox")
        self.sex_comboBox.setMinimumSize(QSize(150, 0))

        self.verticalLayout_5.addWidget(self.sex_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")
        self.dob_dateEdit.setMinimumSize(QSize(150, 0))

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(14, 590, 511, 67))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_12)

        self.bloodtype_lineEdit = QLineEdit(self.layoutWidget1)
        self.bloodtype_lineEdit.setObjectName(u"bloodtype_lineEdit")

        self.verticalLayout_11.addWidget(self.bloodtype_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.PWD_comboBox = QComboBox(self.layoutWidget1)
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.setObjectName(u"PWD_comboBox")
        self.PWD_comboBox.setMinimumSize(QSize(150, 0))
        self.PWD_comboBox.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.PWD_comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_13)

        self.Civilstatus_comboBox = QComboBox(self.layoutWidget1)
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.addItem("")
        self.Civilstatus_comboBox.setObjectName(u"Civilstatus_comboBox")
        self.Civilstatus_comboBox.setMinimumSize(QSize(200, 0))
        self.Civilstatus_comboBox.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.Civilstatus_comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(12, 300, 511, 272))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.birthplace_lineEdit = QLineEdit(self.layoutWidget2)
        self.birthplace_lineEdit.setObjectName(u"birthplace_lineEdit")

        self.verticalLayout_3.addWidget(self.birthplace_lineEdit)


        self.verticalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.contact_lineEdit = QLineEdit(self.layoutWidget2)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")

        self.verticalLayout_4.addWidget(self.contact_lineEdit)


        self.verticalLayout_15.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_11)

        self.emailaddress_lineEdit = QLineEdit(self.layoutWidget2)
        self.emailaddress_lineEdit.setObjectName(u"emailaddress_lineEdit")

        self.verticalLayout_10.addWidget(self.emailaddress_lineEdit)


        self.verticalLayout_15.addLayout(self.verticalLayout_10)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.address_lineEdit = QLineEdit(self.layoutWidget2)
        self.address_lineEdit.setObjectName(u"address_lineEdit")

        self.verticalLayout_8.addWidget(self.address_lineEdit)


        self.verticalLayout_15.addLayout(self.verticalLayout_8)

        self.layoutWidget3 = QWidget(self)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(14, 91, 511, 128))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.firstname_lineEdit = QLineEdit(self.layoutWidget3)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")

        self.verticalLayout.addWidget(self.firstname_lineEdit)


        self.verticalLayout_14.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lastname_lineEdit = QLineEdit(self.layoutWidget3)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")

        self.verticalLayout_2.addWidget(self.lastname_lineEdit)


        self.verticalLayout_14.addLayout(self.verticalLayout_2)

        self.layoutWidget4 = QWidget(self)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(300, 686, 211, 52))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancel_residentbutton = QPushButton(self.layoutWidget4)
        self.cancel_residentbutton.setObjectName(u"cancel_residentbutton")
        self.cancel_residentbutton.setMinimumSize(QSize(0, 50))
        self.cancel_residentbutton.setStyleSheet(u"QPushButton{\n"
" background-color: #585858;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.cancel_residentbutton.setCheckable(True)
        self.cancel_residentbutton.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.cancel_residentbutton)

        self.save_residentbutton = QPushButton(self.layoutWidget4)
        self.save_residentbutton.setObjectName(u"save_residentbutton")
        self.save_residentbutton.setMinimumSize(QSize(0, 50))
        self.save_residentbutton.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.save_residentbutton.setCheckable(True)
        self.save_residentbutton.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.save_residentbutton)


        self.retranslateUi(self)
        


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, ResidentsDialog):
        ResidentsDialog.setWindowTitle(QCoreApplication.translate("ResidentsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ResidentsDialog", u"Add New Resident", None))
        self.label_14.setText(QCoreApplication.translate("ResidentsDialog", u"Middle Initial", None))
        self.label_10.setText(QCoreApplication.translate("ResidentsDialog", u"Age", None))
        self.label_6.setText(QCoreApplication.translate("ResidentsDialog", u"Sex", None))
        self.sex_comboBox.setItemText(0, "")
        self.sex_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Male", None))
        self.sex_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"Female", None))

        self.label_8.setText(QCoreApplication.translate("ResidentsDialog", u"Date of Birth", None))
        self.label_12.setText(QCoreApplication.translate("ResidentsDialog", u"Blood Type", None))
        self.label_7.setText(QCoreApplication.translate("ResidentsDialog", u"PWD", None))
        self.PWD_comboBox.setItemText(0, "")
        self.PWD_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Yes", None))
        self.PWD_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"No", None))

        self.label_13.setText(QCoreApplication.translate("ResidentsDialog", u"Civil Status", None))
        self.Civilstatus_comboBox.setItemText(0, "")
        self.Civilstatus_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Single", None))
        self.Civilstatus_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"Married", None))
        self.Civilstatus_comboBox.setItemText(3, QCoreApplication.translate("ResidentsDialog", u"Divorced", None))
        self.Civilstatus_comboBox.setItemText(4, QCoreApplication.translate("ResidentsDialog", u"Separated", None))
        self.Civilstatus_comboBox.setItemText(5, QCoreApplication.translate("ResidentsDialog", u"Widowed", None))

        self.label_4.setText(QCoreApplication.translate("ResidentsDialog", u"Birth Place", None))
        self.label_5.setText(QCoreApplication.translate("ResidentsDialog", u"Contact", None))
        self.label_11.setText(QCoreApplication.translate("ResidentsDialog", u"Email Address", None))
        self.label_9.setText(QCoreApplication.translate("ResidentsDialog", u"Address", None))
        self.label_2.setText(QCoreApplication.translate("ResidentsDialog", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("ResidentsDialog", u"Last Name", None))
        self.cancel_residentbutton.setText(QCoreApplication.translate("ResidentsDialog", u"Cancel", None))
        self.save_residentbutton.setText(QCoreApplication.translate("ResidentsDialog", u"Add", None))
    # retranslateUi
    
    #ADD NEW RESIDENT WHEN PRESSED A BUTTON
        self.save_residentbutton.clicked.connect(self.add_resident)
        self.cancel_residentbutton.clicked.connect(self.close)
    

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
    
    #INSERT NEW RESIDENT
    
    def insert_new_resident(self):
        try:
            connection = self.create_connection()
            if connection is None:
                return

            cursor = connection.cursor()

            # Create list of resident information
            self.new_resident = [
                self.firstname_lineEdit.text(),
                self.lastname_lineEdit.text(),
                self.middle_lineEdit.text(),
                self.age_lineEdit.text(),
                self.sex_comboBox.currentText(),
                self.PWD_comboBox.currentText(),
                self.birthplace_lineEdit.text(),
                self.dob_dateEdit.date().toString("yyyy-MM-dd"),
                self.bloodtype_lineEdit.text(),
                self.Civilstatus_comboBox.currentText(),
                self.contact_lineEdit.text(),
                self.emailaddress_lineEdit.text(),
                self.address_lineEdit.text(),
                'yes'  # Add isactive directly to the list
            ]

            # Insert query for the new resident
            insert_resident_query = '''INSERT INTO residents(resident_id,brgy_id, admin_id,  Fname, Lname, mid_ini, Age, sex, PWD, birthplace, Birth_date, blood_type, Civil_status, contact_no, email, adrrss, isactive)
                                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'''

            cursor.execute(insert_resident_query, self.new_resident)
            connection.commit()  # Commit the transaction
            cursor.close()
            connection.close()
            
            self.show_inserted_message()  # Call the method to show the message
        except mysql.connector.Error as err:
            # Handle MySql Error
            print(f"Error: {err}")

            
              
    def show_inserted_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.firstname_lineEdit.text() + " inserted into the database")
        msg_box.exec()

    def add_resident(self):
        self.insert_new_resident()
        self.accept()
        
    #LOAD STUDENT INFORAMTION
    def load_resident_info(self):
        self.r
    
    def get_data_from_table(self):
        pass        