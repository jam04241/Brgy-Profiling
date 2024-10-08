# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UPDATEOFFICIAL_FINAL.ui'
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
        Dialog.resize(548, 583)
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
        self.layoutWidget.setGeometry(QRect(10, 280, 531, 69))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_16.setFont(font)

        self.verticalLayout_16.addWidget(self.label_16)

        self.update_sex_official_set = QComboBox(self.layoutWidget)
        self.update_sex_official_set.addItem("")
        self.update_sex_official_set.addItem("")
        self.update_sex_official_set.addItem("")
        self.update_sex_official_set.setObjectName(u"update_sex_official_set")

        self.verticalLayout_16.addWidget(self.update_sex_official_set)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_17.addWidget(self.label_17)

        self.update_pos_official_set = QComboBox(self.layoutWidget)
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.addItem("")
        self.update_pos_official_set.setObjectName(u"update_pos_official_set")
        self.update_pos_official_set.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.update_pos_official_set)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_20.addWidget(self.label_20)

        self.update_status_official_set = QComboBox(self.layoutWidget)
        self.update_status_official_set.addItem("")
        self.update_status_official_set.addItem("")
        self.update_status_official_set.addItem("")
        self.update_status_official_set.addItem("")
        self.update_status_official_set.addItem("")
        self.update_status_official_set.addItem("")
        self.update_status_official_set.setObjectName(u"update_status_official_set")

        self.verticalLayout_20.addWidget(self.update_status_official_set)


        self.horizontalLayout_2.addLayout(self.verticalLayout_20)

        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 210, 531, 67))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_18.addWidget(self.label_18)

        self.update_mid_official = QLineEdit(self.layoutWidget_2)
        self.update_mid_official.setObjectName(u"update_mid_official")

        self.verticalLayout_18.addWidget(self.update_mid_official)


        self.horizontalLayout.addLayout(self.verticalLayout_18)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_9.addWidget(self.label_10)

        self.update_age_official = QLineEdit(self.layoutWidget_2)
        self.update_age_official.setObjectName(u"update_age_official")

        self.verticalLayout_9.addWidget(self.update_age_official)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_10.addWidget(self.label_11)

        self.update_dob_official_set = QDateEdit(self.layoutWidget_2)
        self.update_dob_official_set.setObjectName(u"update_dob_official_set")
        self.update_dob_official_set.setMinimumSize(QSize(100, 0))

        self.verticalLayout_10.addWidget(self.update_dob_official_set)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.layoutWidget_8 = QWidget(Dialog)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(340, 520, 191, 52))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel_update = QPushButton(self.layoutWidget_8)
        self.btn_cancel_update.setObjectName(u"btn_cancel_update")
        self.btn_cancel_update.setMinimumSize(QSize(0, 50))
        self.btn_cancel_update.setBaseSize(QSize(0, 50))
        self.btn_cancel_update.setStyleSheet(u"QPushButton{\n"
" background-color: #585858;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.btn_cancel_update.setCheckable(True)
        self.btn_cancel_update.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.btn_cancel_update)

        self.btn_update_official = QPushButton(self.layoutWidget_8)
        self.btn_update_official.setObjectName(u"btn_update_official")
        self.btn_update_official.setMinimumSize(QSize(0, 50))
        self.btn_update_official.setBaseSize(QSize(0, 50))
        self.btn_update_official.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        self.btn_update_official.setCheckable(True)
        self.btn_update_official.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.btn_update_official)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 261, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_12.setFont(font1)
        self.layoutWidget_3 = QWidget(Dialog)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 440, 531, 63))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_22.addWidget(self.label_22)

        self.update_email_official = QLineEdit(self.layoutWidget_3)
        self.update_email_official.setObjectName(u"update_email_official")

        self.verticalLayout_22.addWidget(self.update_email_official)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-40, 80, 541, 21))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget_4 = QWidget(Dialog)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 360, 531, 65))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_start_official = QDateEdit(self.layoutWidget_4)
        self.update_start_official.setObjectName(u"update_start_official")

        self.verticalLayout_7.addWidget(self.update_start_official)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_8.addWidget(self.label_9)

        self.update_end_official = QDateEdit(self.layoutWidget_4)
        self.update_end_official.setObjectName(u"update_end_official")

        self.verticalLayout_8.addWidget(self.update_end_official)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.layoutWidget_5 = QWidget(Dialog)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 70, 531, 128))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.layoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_13.addWidget(self.label_13)

        self.update_fname_official = QLineEdit(self.layoutWidget_5)
        self.update_fname_official.setObjectName(u"update_fname_official")

        self.verticalLayout_13.addWidget(self.update_fname_official)


        self.verticalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.layoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_14.addWidget(self.label_14)

        self.update_lname_official = QLineEdit(self.layoutWidget_5)
        self.update_lname_official.setObjectName(u"update_lname_official")

        self.verticalLayout_14.addWidget(self.update_lname_official)


        self.verticalLayout.addLayout(self.verticalLayout_14)


        self.retranslateUi(Dialog)
        self.btn_update_official.toggled.connect(Dialog.close)
        self.btn_cancel_update.toggled.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Sex", None))
        self.update_sex_official_set.setItemText(0, "")
        self.update_sex_official_set.setItemText(1, QCoreApplication.translate("Dialog", u"Male", None))
        self.update_sex_official_set.setItemText(2, QCoreApplication.translate("Dialog", u"Female", None))

        self.label_17.setText(QCoreApplication.translate("Dialog", u"Position", None))
        self.update_pos_official_set.setItemText(0, "")
        self.update_pos_official_set.setItemText(1, QCoreApplication.translate("Dialog", u"Captain", None))
        self.update_pos_official_set.setItemText(2, QCoreApplication.translate("Dialog", u"Councilor", None))
        self.update_pos_official_set.setItemText(3, QCoreApplication.translate("Dialog", u"Kagawad", None))
        self.update_pos_official_set.setItemText(4, QCoreApplication.translate("Dialog", u"Sk Kagawad", None))
        self.update_pos_official_set.setItemText(5, QCoreApplication.translate("Dialog", u"Tanod", None))

        self.label_20.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.update_status_official_set.setItemText(0, "")
        self.update_status_official_set.setItemText(1, QCoreApplication.translate("Dialog", u"Single", None))
        self.update_status_official_set.setItemText(2, QCoreApplication.translate("Dialog", u"Married", None))
        self.update_status_official_set.setItemText(3, QCoreApplication.translate("Dialog", u"Divorced", None))
        self.update_status_official_set.setItemText(4, QCoreApplication.translate("Dialog", u"Separated", None))
        self.update_status_official_set.setItemText(5, QCoreApplication.translate("Dialog", u"Widowed", None))

        self.label_18.setText(QCoreApplication.translate("Dialog", u"MIddle Initial", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Age", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Date of Birth", None))
        self.btn_cancel_update.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn_update_official.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Update Official", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Email Address", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Term Start", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Term End", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
    # retranslateUi

