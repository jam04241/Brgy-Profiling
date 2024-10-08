# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finalOfficialResident.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ResidentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(547, 584)
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
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(330, 541, 191, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancel_residentbutton = QPushButton(self.layoutWidget)
        self.cancel_residentbutton.setObjectName(u"cancel_residentbutton")
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

        self.save_residentbutton = QPushButton(self.layoutWidget)
        self.save_residentbutton.setObjectName(u"save_residentbutton")
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

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 91, 522, 416))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.firstname_lineEdit = QLineEdit(self.layoutWidget1)
        self.firstname_lineEdit.setObjectName(u"firstname_lineEdit")

        self.verticalLayout.addWidget(self.firstname_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lastname_lineEdit = QLineEdit(self.layoutWidget1)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")

        self.verticalLayout_2.addWidget(self.lastname_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_10)

        self.age_lineEdit = QLineEdit(self.layoutWidget1)
        self.age_lineEdit.setObjectName(u"age_lineEdit")

        self.verticalLayout_9.addWidget(self.age_lineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

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


        self.verticalLayout_13.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget1)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

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
        self.PWD_comboBox.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.PWD_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

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
        self.Civilstatus_comboBox.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.Civilstatus_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_12)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget1)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.birthplace_lineEdit = QLineEdit(self.layoutWidget1)
        self.birthplace_lineEdit.setObjectName(u"birthplace_lineEdit")

        self.verticalLayout_3.addWidget(self.birthplace_lineEdit)


        self.verticalLayout_13.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.address_lineEdit = QLineEdit(self.layoutWidget1)
        self.address_lineEdit.setObjectName(u"address_lineEdit")

        self.verticalLayout_8.addWidget(self.address_lineEdit)


        self.verticalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.contact_lineEdit = QLineEdit(self.layoutWidget1)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")

        self.verticalLayout_4.addWidget(self.contact_lineEdit)


        self.verticalLayout_13.addLayout(self.verticalLayout_4)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_11)

        self.emailaddress_lineEdit = QLineEdit(self.layoutWidget1)
        self.emailaddress_lineEdit.setObjectName(u"emailaddress_lineEdit")

        self.verticalLayout_10.addWidget(self.emailaddress_lineEdit)


        self.verticalLayout_13.addLayout(self.verticalLayout_10)


        self.retranslateUi(self)
        self.cancel_residentbutton.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, ResidentsDialog):
        ResidentsDialog.setWindowTitle(QCoreApplication.translate("ResidentsDialog", u"Add Resident", None))
        self.label.setText(QCoreApplication.translate("ResidentsDialog", u"Add New Residents", None))
        self.cancel_residentbutton.setText(QCoreApplication.translate("ResidentsDialog", u"Cancel", None))
        self.save_residentbutton.setText(QCoreApplication.translate("ResidentsDialog", u"Add Official", None))
        self.label_2.setText(QCoreApplication.translate("ResidentsDialog", u"First Name", None))
        self.label_3.setText(QCoreApplication.translate("ResidentsDialog", u"Last Name", None))
        self.label_10.setText(QCoreApplication.translate("ResidentsDialog", u"Age", None))
        self.label_12.setText(QCoreApplication.translate("ResidentsDialog", u"Blood Type", None))
        self.label_6.setText(QCoreApplication.translate("ResidentsDialog", u"Gender", None))
        self.gender_comboBox.setItemText(0, "")
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("ResidentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("ResidentsDialog", u"Female", None))

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

        self.label_8.setText(QCoreApplication.translate("ResidentsDialog", u"Date of Birth", None))
        self.label_4.setText(QCoreApplication.translate("ResidentsDialog", u"Birth Place", None))
        self.label_9.setText(QCoreApplication.translate("ResidentsDialog", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("ResidentsDialog", u"Contact", None))
        self.label_11.setText(QCoreApplication.translate("ResidentsDialog", u"Email Address", None))
    # retranslateUi

