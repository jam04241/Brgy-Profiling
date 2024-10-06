# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OfficialDialog2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OfficialDialog(QDialog):
    def __init__(self, parent=None):
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
        self.label_12 = QLabel(self)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 261, 31))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_12.setFont(font)
        self.layoutWidget_7 = QWidget(self)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(30, 90, 491, 431))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.layoutWidget_7)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_13.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_13)

        self.firstname_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.firstname_lineEdit2.setObjectName(u"firstname_lineEdit2")

        self.verticalLayout_13.addWidget(self.firstname_lineEdit2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.layoutWidget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_14)

        self.lastname_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.lastname_lineEdit2.setObjectName(u"lastname_lineEdit2")

        self.verticalLayout_14.addWidget(self.lastname_lineEdit2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.layoutWidget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_15)

        self.age_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.age_lineEdit2.setObjectName(u"age_lineEdit2")

        self.verticalLayout_15.addWidget(self.age_lineEdit2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.layoutWidget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_16)

        self.gender_comboBox2 = QComboBox(self.layoutWidget_7)
        self.gender_comboBox2.addItem("")
        self.gender_comboBox2.addItem("")
        self.gender_comboBox2.addItem("")
        self.gender_comboBox2.setObjectName(u"gender_comboBox2")

        self.verticalLayout_16.addWidget(self.gender_comboBox2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.layoutWidget_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_17)

        self.position_comboBox = QComboBox(self.layoutWidget_7)
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.position_comboBox.setObjectName(u"position_comboBox")
        self.position_comboBox.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.position_comboBox)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.layoutWidget_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_19.addWidget(self.label_19)

        self.birthplace_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.birthplace_lineEdit2.setObjectName(u"birthplace_lineEdit2")

        self.verticalLayout_19.addWidget(self.birthplace_lineEdit2)


        self.verticalLayout_12.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.layoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_20)

        self.address_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.address_lineEdit2.setObjectName(u"address_lineEdit2")

        self.verticalLayout_20.addWidget(self.address_lineEdit2)


        self.verticalLayout_12.addLayout(self.verticalLayout_20)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_21 = QLabel(self.layoutWidget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_21)

        self.contact_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.contact_lineEdit2.setObjectName(u"contact_lineEdit2")

        self.verticalLayout_21.addWidget(self.contact_lineEdit2)


        self.verticalLayout_12.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_22 = QLabel(self.layoutWidget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_22)

        self.emailaddress_lineEdit2 = QLineEdit(self.layoutWidget_7)
        self.emailaddress_lineEdit2.setObjectName(u"emailaddress_lineEdit2")

        self.verticalLayout_22.addWidget(self.emailaddress_lineEdit2)


        self.verticalLayout_12.addLayout(self.verticalLayout_22)

        self.line_2 = QFrame(self)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 50, 541, 21))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_8 = QWidget(self)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(330, 550, 191, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cancel_officialbutton = QPushButton(self.layoutWidget_8)
        self.cancel_officialbutton.setObjectName(u"cancel_officialbutton")
        self.cancel_officialbutton.setStyleSheet(u"QPushButton{\n"
" background-color: #585858;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.cancel_officialbutton.setCheckable(True)
        self.cancel_officialbutton.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.cancel_officialbutton)

        self.save_officialbutton = QPushButton(self.layoutWidget_8)
        self.save_officialbutton.setObjectName(u"save_officialbutton")
        self.save_officialbutton.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.save_officialbutton.setCheckable(True)
        self.save_officialbutton.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.save_officialbutton)


        self.retranslateUi(self)
        self.cancel_officialbutton.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, OfficialDialog):
        OfficialDialog.setWindowTitle(QCoreApplication.translate("OfficialDialog", u"Dialog", None))
        self.label_12.setText(QCoreApplication.translate("OfficialDialog", u"Add New Official", None))
        self.label_13.setText(QCoreApplication.translate("OfficialDialog", u"First Name", None))
        self.label_14.setText(QCoreApplication.translate("OfficialDialog", u"Last Name", None))
        self.label_15.setText(QCoreApplication.translate("OfficialDialog", u"Age", None))
        self.label_16.setText(QCoreApplication.translate("OfficialDialog", u"Select Gender", None))
        self.gender_comboBox2.setItemText(0, QCoreApplication.translate("OfficialDialog", u"GENDER", None))
        self.gender_comboBox2.setItemText(1, QCoreApplication.translate("OfficialDialog", u"Male", None))
        self.gender_comboBox2.setItemText(2, QCoreApplication.translate("OfficialDialog", u"Female", None))

        self.label_17.setText(QCoreApplication.translate("OfficialDialog", u"Position", None))
        self.position_comboBox.setItemText(0, QCoreApplication.translate("OfficialDialog", u"Position", None))
        self.position_comboBox.setItemText(1, QCoreApplication.translate("OfficialDialog", u"Captain", None))
        self.position_comboBox.setItemText(2, QCoreApplication.translate("OfficialDialog", u"Councilor", None))
        self.position_comboBox.setItemText(3, QCoreApplication.translate("OfficialDialog", u"Kagawad", None))
        self.position_comboBox.setItemText(4, QCoreApplication.translate("OfficialDialog", u"Sk Kagawad", None))
        self.position_comboBox.setItemText(5, QCoreApplication.translate("OfficialDialog", u"Tanod", None))

        self.label_19.setText(QCoreApplication.translate("OfficialDialog", u"Status", None))
        self.label_20.setText(QCoreApplication.translate("OfficialDialog", u"Term Start", None))
        self.label_21.setText(QCoreApplication.translate("OfficialDialog", u"Term End", None))
        self.label_22.setText(QCoreApplication.translate("OfficialDialog", u"Email Address", None))
        self.cancel_officialbutton.setText(QCoreApplication.translate("OfficialDialog", u"Cancel", None))
        self.save_officialbutton.setText(QCoreApplication.translate("OfficialDialog", u"Add Official", None))
    # retranslateUi

