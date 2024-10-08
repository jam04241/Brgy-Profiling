# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OFFICIALDIALOG_FINAL.ui'
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

class Ui_OfficialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(548, 583)
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
        self.line_2 = QFrame(self)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-40, 80, 541, 21))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_8 = QWidget(self)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(340, 520, 191, 52))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cancel_officialbutton = QPushButton(self.layoutWidget_8)
        self.cancel_officialbutton.setObjectName(u"cancel_officialbutton")
        self.cancel_officialbutton.setMinimumSize(QSize(0, 50))
        self.cancel_officialbutton.setBaseSize(QSize(0, 50))
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
        self.save_officialbutton.setMinimumSize(QSize(0, 50))
        self.save_officialbutton.setBaseSize(QSize(0, 50))
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

        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 210, 531, 67))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_18.setFont(font1)

        self.verticalLayout_18.addWidget(self.label_18)

        self.age_lineEdit_2 = QLineEdit(self.layoutWidget)
        self.age_lineEdit_2.setObjectName(u"age_lineEdit_2")

        self.verticalLayout_18.addWidget(self.age_lineEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_18)

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

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_11)

        self.dob_dateEdit_off = QDateEdit(self.layoutWidget)
        self.dob_dateEdit_off.setObjectName(u"dob_dateEdit_off")
        self.dob_dateEdit_off.setMinimumSize(QSize(100, 0))

        self.verticalLayout_10.addWidget(self.dob_dateEdit_off)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 440, 531, 63))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.verticalLayout_22.addWidget(self.label_22)

        self.email_lineEdit2 = QLineEdit(self.layoutWidget1)
        self.email_lineEdit2.setObjectName(u"email_lineEdit2")

        self.verticalLayout_22.addWidget(self.email_lineEdit2)

        self.layoutWidget2 = QWidget(self)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 70, 531, 128))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_13)

        self.firstname_lineEdit2 = QLineEdit(self.layoutWidget2)
        self.firstname_lineEdit2.setObjectName(u"firstname_lineEdit2")

        self.verticalLayout_13.addWidget(self.firstname_lineEdit2)


        self.verticalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.layoutWidget2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_14)

        self.lastname_lineEdit2 = QLineEdit(self.layoutWidget2)
        self.lastname_lineEdit2.setObjectName(u"lastname_lineEdit2")

        self.verticalLayout_14.addWidget(self.lastname_lineEdit2)


        self.verticalLayout.addLayout(self.verticalLayout_14)

        self.layoutWidget3 = QWidget(self)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 280, 531, 69))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.layoutWidget3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_16)

        self.sex_comboBox2 = QComboBox(self.layoutWidget3)
        self.sex_comboBox2.addItem("")
        self.sex_comboBox2.addItem("")
        self.sex_comboBox2.addItem("")
        self.sex_comboBox2.setObjectName(u"sex_comboBox2")

        self.verticalLayout_16.addWidget(self.sex_comboBox2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.layoutWidget3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_17)

        self.position_comboBox = QComboBox(self.layoutWidget3)
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
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


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.layoutWidget3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_20.addWidget(self.label_20)

        self.add_status_offi_set = QComboBox(self.layoutWidget3)
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.addItem("")
        self.add_status_offi_set.setObjectName(u"add_status_offi_set")

        self.verticalLayout_20.addWidget(self.add_status_offi_set)


        self.horizontalLayout_2.addLayout(self.verticalLayout_20)

        self.layoutWidget4 = QWidget(self)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 360, 531, 65))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.termstart_dateEdit = QDateEdit(self.layoutWidget4)
        self.termstart_dateEdit.setObjectName(u"termstart_dateEdit")

        self.verticalLayout_7.addWidget(self.termstart_dateEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_9)

        self.termend_dateEdit = QDateEdit(self.layoutWidget4)
        self.termend_dateEdit.setObjectName(u"termend_dateEdit")

        self.verticalLayout_8.addWidget(self.termend_dateEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.retranslateUi(self)
        self.cancel_officialbutton.toggled.connect(self.close)
        self.save_officialbutton.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, OfficialDialog):
        OfficialDialog.setWindowTitle(QCoreApplication.translate("OfficialDialog", u"Dialog", None))
        self.label_12.setText(QCoreApplication.translate("OfficialDialog", u"Add New Official", None))
        self.cancel_officialbutton.setText(QCoreApplication.translate("OfficialDialog", u"Cancel", None))
        self.save_officialbutton.setText(QCoreApplication.translate("OfficialDialog", u"Add", None))
        self.label_18.setText(QCoreApplication.translate("OfficialDialog", u"MIddle Initial", None))
        self.label_10.setText(QCoreApplication.translate("OfficialDialog", u"Age", None))
        self.label_11.setText(QCoreApplication.translate("OfficialDialog", u"Date of Birth", None))
        self.label_22.setText(QCoreApplication.translate("OfficialDialog", u"Email Address", None))
        self.label_13.setText(QCoreApplication.translate("OfficialDialog", u"First Name", None))
        self.label_14.setText(QCoreApplication.translate("OfficialDialog", u"Last Name", None))
        self.label_16.setText(QCoreApplication.translate("OfficialDialog", u"Sex", None))
        self.sex_comboBox2.setItemText(0, "")
        self.sex_comboBox2.setItemText(1, QCoreApplication.translate("OfficialDialog", u"Male", None))
        self.sex_comboBox2.setItemText(2, QCoreApplication.translate("OfficialDialog", u"Female", None))

        self.label_17.setText(QCoreApplication.translate("OfficialDialog", u"Position", None))
        self.position_comboBox.setItemText(0, "")
        self.position_comboBox.setItemText(1, QCoreApplication.translate("OfficialDialog", u"Captain", None))
        self.position_comboBox.setItemText(2, QCoreApplication.translate("OfficialDialog", u"Secretary", None))
        self.position_comboBox.setItemText(3, QCoreApplication.translate("OfficialDialog", u"Treasurer", None))
        self.position_comboBox.setItemText(4, QCoreApplication.translate("OfficialDialog", u"Councilor", None))
        self.position_comboBox.setItemText(5, QCoreApplication.translate("OfficialDialog", u"Kagawad", None))
        self.position_comboBox.setItemText(6, QCoreApplication.translate("OfficialDialog", u"Sk Kagawad", None))
        self.position_comboBox.setItemText(7, QCoreApplication.translate("OfficialDialog", u"Tanod", None))

        self.label_20.setText(QCoreApplication.translate("OfficialDialog", u"Status", None))
        self.add_status_offi_set.setItemText(0, "")
        self.add_status_offi_set.setItemText(1, QCoreApplication.translate("OfficialDialog", u"Single", None))
        self.add_status_offi_set.setItemText(2, QCoreApplication.translate("OfficialDialog", u"Married", None))
        self.add_status_offi_set.setItemText(3, QCoreApplication.translate("OfficialDialog", u"Divorced", None))
        self.add_status_offi_set.setItemText(4, QCoreApplication.translate("OfficialDialog", u"Separated", None))
        self.add_status_offi_set.setItemText(5, QCoreApplication.translate("OfficialDialog", u"Widowed", None))

        self.label_8.setText(QCoreApplication.translate("OfficialDialog", u"Term Start", None))
        self.label_9.setText(QCoreApplication.translate("OfficialDialog", u"Term End", None))
    # retranslateUi

