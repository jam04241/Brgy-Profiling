# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UPDATERESIDENT_FINAL.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(531, 762)
        Dialog.setStyleSheet(u"QDialog{\n"
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
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(299, 686, 211, 52))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_update_cancel_resi = QPushButton(self.layoutWidget)
        self.btn_update_cancel_resi.setObjectName(u"btn_update_cancel_resi")
        self.btn_update_cancel_resi.setMinimumSize(QSize(0, 50))
        self.btn_update_cancel_resi.setStyleSheet(u"QPushButton{\n"
" background-color: #585858;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.btn_update_cancel_resi.setCheckable(True)
        self.btn_update_cancel_resi.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_update_cancel_resi)

        self.btn_update_resi = QPushButton(self.layoutWidget)
        self.btn_update_resi.setObjectName(u"btn_update_resi")
        self.btn_update_resi.setMinimumSize(QSize(0, 50))
        self.btn_update_resi.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.btn_update_resi.setCheckable(True)
        self.btn_update_resi.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.btn_update_resi)

        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(13, 98, 511, 124))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_15.setFont(font)

        self.verticalLayout_18.addWidget(self.label_15)

        self.update_fname = QLineEdit(self.layoutWidget_2)
        self.update_fname.setObjectName(u"update_fname")
        self.update_fname.setMinimumSize(QSize(0, 35))

        self.verticalLayout_18.addWidget(self.update_fname)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_19.addWidget(self.label_17)

        self.update_lname = QLineEdit(self.layoutWidget_2)
        self.update_lname.setObjectName(u"update_lname")
        self.update_lname.setMinimumSize(QSize(0, 35))

        self.verticalLayout_19.addWidget(self.update_lname)


        self.verticalLayout_17.addLayout(self.verticalLayout_19)

        self.layoutWidget_3 = QWidget(Dialog)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(11, 300, 511, 272))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_18 = QLabel(self.layoutWidget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_21.addWidget(self.label_18)

        self.update_birthplace = QLineEdit(self.layoutWidget_3)
        self.update_birthplace.setObjectName(u"update_birthplace")
        self.update_birthplace.setMinimumSize(QSize(0, 35))

        self.verticalLayout_21.addWidget(self.update_birthplace)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_19 = QLabel(self.layoutWidget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.verticalLayout_22.addWidget(self.label_19)

        self.update_contact = QLineEdit(self.layoutWidget_3)
        self.update_contact.setObjectName(u"update_contact")
        self.update_contact.setMinimumSize(QSize(0, 35))

        self.verticalLayout_22.addWidget(self.update_contact)


        self.verticalLayout_20.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_23.addWidget(self.label_20)

        self.update_email = QLineEdit(self.layoutWidget_3)
        self.update_email.setObjectName(u"update_email")
        self.update_email.setMinimumSize(QSize(0, 35))

        self.verticalLayout_23.addWidget(self.update_email)


        self.verticalLayout_20.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_21 = QLabel(self.layoutWidget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.verticalLayout_24.addWidget(self.label_21)

        self.update_address = QLineEdit(self.layoutWidget_3)
        self.update_address.setObjectName(u"update_address")
        self.update_address.setMinimumSize(QSize(0, 35))

        self.verticalLayout_24.addWidget(self.update_address)


        self.verticalLayout_20.addLayout(self.verticalLayout_24)

        self.layoutWidget_4 = QWidget(Dialog)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(13, 590, 511, 67))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_22 = QLabel(self.layoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_25.addWidget(self.label_22)

        self.update_blood = QLineEdit(self.layoutWidget_4)
        self.update_blood.setObjectName(u"update_blood")
        self.update_blood.setMinimumSize(QSize(0, 35))

        self.verticalLayout_25.addWidget(self.update_blood)


        self.horizontalLayout_5.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_23 = QLabel(self.layoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.verticalLayout_26.addWidget(self.label_23)

        self.update_pwd_set = QComboBox(self.layoutWidget_4)
        self.update_pwd_set.addItem("")
        self.update_pwd_set.addItem("")
        self.update_pwd_set.addItem("")
        self.update_pwd_set.setObjectName(u"update_pwd_set")
        self.update_pwd_set.setMinimumSize(QSize(150, 35))
        self.update_pwd_set.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.update_pwd_set)


        self.horizontalLayout_5.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_24 = QLabel(self.layoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.verticalLayout_27.addWidget(self.label_24)

        self.update_status_set = QComboBox(self.layoutWidget_4)
        self.update_status_set.addItem("")
        self.update_status_set.addItem("")
        self.update_status_set.addItem("")
        self.update_status_set.addItem("")
        self.update_status_set.addItem("")
        self.update_status_set.addItem("")
        self.update_status_set.setObjectName(u"update_status_set")
        self.update_status_set.setMinimumSize(QSize(200, 35))
        self.update_status_set.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.update_status_set)


        self.horizontalLayout_5.addLayout(self.verticalLayout_27)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 20, 261, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-1, 60, 541, 21))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_5 = QWidget(Dialog)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 230, 511, 67))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_25 = QLabel(self.layoutWidget_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.verticalLayout_28.addWidget(self.label_25)

        self.update_mid = QLineEdit(self.layoutWidget_5)
        self.update_mid.setObjectName(u"update_mid")
        self.update_mid.setMinimumSize(QSize(0, 35))

        self.verticalLayout_28.addWidget(self.update_mid)


        self.horizontalLayout_6.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_26 = QLabel(self.layoutWidget_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.verticalLayout_29.addWidget(self.label_26)

        self.update_age = QLineEdit(self.layoutWidget_5)
        self.update_age.setObjectName(u"update_age")
        self.update_age.setMinimumSize(QSize(0, 35))

        self.verticalLayout_29.addWidget(self.update_age)


        self.horizontalLayout_6.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_27 = QLabel(self.layoutWidget_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.verticalLayout_30.addWidget(self.label_27)

        self.update_sex_set = QComboBox(self.layoutWidget_5)
        self.update_sex_set.addItem("")
        self.update_sex_set.addItem("")
        self.update_sex_set.addItem("")
        self.update_sex_set.setObjectName(u"update_sex_set")
        self.update_sex_set.setMinimumSize(QSize(150, 35))

        self.verticalLayout_30.addWidget(self.update_sex_set)


        self.horizontalLayout_6.addLayout(self.verticalLayout_30)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_28 = QLabel(self.layoutWidget_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.verticalLayout_31.addWidget(self.label_28)

        self.update_dob_dateEdit_res = QDateEdit(self.layoutWidget_5)
        self.update_dob_dateEdit_res.setObjectName(u"update_dob_dateEdit_res")
        self.update_dob_dateEdit_res.setMinimumSize(QSize(100, 35))

        self.verticalLayout_31.addWidget(self.update_dob_dateEdit_res)


        self.horizontalLayout_6.addLayout(self.verticalLayout_31)


        self.retranslateUi(Dialog)
        self.btn_update_resi.toggled.connect(Dialog.close)
        self.btn_update_cancel_resi.toggled.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_update_cancel_resi.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_update_resi.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Birth Place", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Contact", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Email Address", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Blood Type", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"PWD", None))
        self.update_pwd_set.setItemText(0, "")
        self.update_pwd_set.setItemText(1, QCoreApplication.translate("Dialog", u"Yes", None))
        self.update_pwd_set.setItemText(2, QCoreApplication.translate("Dialog", u"No", None))

        self.label_24.setText(QCoreApplication.translate("Dialog", u"Civil Status", None))
        self.update_status_set.setItemText(0, "")
        self.update_status_set.setItemText(1, QCoreApplication.translate("Dialog", u"Single", None))
        self.update_status_set.setItemText(2, QCoreApplication.translate("Dialog", u"Married", None))
        self.update_status_set.setItemText(3, QCoreApplication.translate("Dialog", u"Divorced", None))
        self.update_status_set.setItemText(4, QCoreApplication.translate("Dialog", u"Separated", None))
        self.update_status_set.setItemText(5, QCoreApplication.translate("Dialog", u"Widowed", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Update Resident", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"MIddle Initial", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Age", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Sex", None))
        self.update_sex_set.setItemText(0, "")
        self.update_sex_set.setItemText(1, QCoreApplication.translate("Dialog", u"Male", None))
        self.update_sex_set.setItemText(2, QCoreApplication.translate("Dialog", u"Female", None))

        self.label_28.setText(QCoreApplication.translate("Dialog", u"Date of Birth", None))
    # retranslateUi

