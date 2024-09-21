# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1330, 890)
        MainWindow.setMinimumSize(QSize(1330, 890))
        MainWindow.setMaximumSize(QSize(1360, 890))
        font = QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 7, 1311, 881))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(95, 0))
        self.icon_only_widget.setMaximumSize(QSize(95, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"\n"
"background-color: rgb(0,0,0);\n"
"\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/images/head1-1.png"))

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/border-all-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(100, 20))
        self.dashboard_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.dashboard_1)

        self.official_1 = QPushButton(self.icon_only_widget)
        self.official_1.setObjectName(u"official_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/users-gear-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.official_1.setIcon(icon1)
        self.official_1.setIconSize(QSize(100, 20))
        self.official_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.official_1)

        self.resident_1 = QPushButton(self.icon_only_widget)
        self.resident_1.setObjectName(u"resident_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/user-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resident_1.setIcon(icon2)
        self.resident_1.setIconSize(QSize(100, 19))
        self.resident_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.resident_1)

        self.certificate_1 = QPushButton(self.icon_only_widget)
        self.certificate_1.setObjectName(u"certificate_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/scroll-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.certificate_1.setIcon(icon3)
        self.certificate_1.setIconSize(QSize(100, 20))
        self.certificate_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.certificate_1)

        self.blotter_1 = QPushButton(self.icon_only_widget)
        self.blotter_1.setObjectName(u"blotter_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/file-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.blotter_1.setIcon(icon4)
        self.blotter_1.setIconSize(QSize(100, 20))
        self.blotter_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.blotter_1)

        self.staff_1 = QPushButton(self.icon_only_widget)
        self.staff_1.setObjectName(u"staff_1")
        self.staff_1.setIcon(icon2)
        self.staff_1.setIconSize(QSize(100, 20))
        self.staff_1.setCheckable(True)

        self.verticalLayout_7.addWidget(self.staff_1)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(17, 385, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setIcon(icon2)
        self.settings_1.setIconSize(QSize(100, 20))

        self.verticalLayout_8.addWidget(self.settings_1)

        self.pushButton_8 = QPushButton(self.icon_only_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon5 = QIcon()
        icon5.addFile(u":/images/right-from-bracket-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(100, 20))

        self.verticalLayout_8.addWidget(self.pushButton_8)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget {\n"
"\n"
"background-color: rgb(0,0,0);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"height:30px;\n"
"border:none;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.icon_text_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/images/head1-1.png"))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 30, 0, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"  padding-right:35\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/images/border-all-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/images/border-all-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon6)
        self.dashboard_2.setIconSize(QSize(100, 20))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.dashboard_2)

        self.officials = QFrame(self.icon_text_widget)
        self.officials.setObjectName(u"officials")
        self.officials.setFrameShape(QFrame.Shape.StyledPanel)
        self.officials.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.officials)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.official_2 = QPushButton(self.officials)
        self.official_2.setObjectName(u"official_2")
        self.official_2.setStyleSheet(u"QPushButton{\n"
"  padding-right:-20\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.official_2.setIcon(icon1)
        self.official_2.setIconSize(QSize(100, 20))
        self.official_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.official_2)

        self.officials_dropdown = QFrame(self.officials)
        self.officials_dropdown.setObjectName(u"officials_dropdown")
        self.officials_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.officials_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.officials_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_official = QPushButton(self.officials_dropdown)
        self.new_official.setObjectName(u"new_official")
        self.new_official.setStyleSheet(u"QPushButton{\n"
"  padding-left:-60;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.new_official.setCheckable(True)
        self.new_official.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.new_official)

        self.list_official = QPushButton(self.officials_dropdown)
        self.list_official.setObjectName(u"list_official")
        self.list_official.setStyleSheet(u"QPushButton{\n"
"  padding-left:-45;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.list_official.setCheckable(True)
        self.list_official.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.list_official)

        self.end_term = QPushButton(self.officials_dropdown)
        self.end_term.setObjectName(u"end_term")
        self.end_term.setStyleSheet(u"QPushButton{\n"
"  padding-left:-35;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.end_term.setCheckable(True)
        self.end_term.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.end_term)


        self.verticalLayout_3.addWidget(self.officials_dropdown)


        self.verticalLayout_5.addWidget(self.officials)

        self.residents = QFrame(self.icon_text_widget)
        self.residents.setObjectName(u"residents")
        self.residents.setFrameShape(QFrame.Shape.StyledPanel)
        self.residents.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.residents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.resident_2 = QPushButton(self.residents)
        self.resident_2.setObjectName(u"resident_2")
        self.resident_2.setStyleSheet(u"QPushButton{\n"
"  padding-right:20\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.resident_2.setIcon(icon2)
        self.resident_2.setIconSize(QSize(100, 20))
        self.resident_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.resident_2)

        self.residents_dropdown = QFrame(self.residents)
        self.residents_dropdown.setObjectName(u"residents_dropdown")
        self.residents_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.residents_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.residents_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.new_resident = QPushButton(self.residents_dropdown)
        self.new_resident.setObjectName(u"new_resident")
        self.new_resident.setStyleSheet(u"QPushButton{\n"
"  padding-left:-40;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.new_resident.setCheckable(True)
        self.new_resident.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.new_resident)

        self.all_resident = QPushButton(self.residents_dropdown)
        self.all_resident.setObjectName(u"all_resident")
        self.all_resident.setStyleSheet(u"QPushButton{\n"
"  padding-left:-43;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.all_resident.setCheckable(True)
        self.all_resident.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.all_resident)

        self.archieve_resident = QPushButton(self.residents_dropdown)
        self.archieve_resident.setObjectName(u"archieve_resident")
        self.archieve_resident.setStyleSheet(u"QPushButton{\n"
"  padding-left:-13;\n"
"}\n"
"\n"
"QPushButtonhover{\n"
"color:#12B298\n"
"}")
        self.archieve_resident.setCheckable(True)
        self.archieve_resident.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.archieve_resident)


        self.verticalLayout_4.addWidget(self.residents_dropdown)


        self.verticalLayout_5.addWidget(self.residents)

        self.certificate_2 = QPushButton(self.icon_text_widget)
        self.certificate_2.setObjectName(u"certificate_2")
        self.certificate_2.setStyleSheet(u"QPushButton{\n"
"  padding-right:-10\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.certificate_2.setIcon(icon3)
        self.certificate_2.setIconSize(QSize(100, 20))
        self.certificate_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.certificate_2)

        self.blotter_2 = QPushButton(self.icon_text_widget)
        self.blotter_2.setObjectName(u"blotter_2")
        self.blotter_2.setStyleSheet(u"QPushButton{\n"
"  padding-right:15\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/file-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/images/file-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.blotter_2.setIcon(icon7)
        self.blotter_2.setIconSize(QSize(100, 20))
        self.blotter_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.blotter_2)

        self.staff_2 = QPushButton(self.icon_text_widget)
        self.staff_2.setObjectName(u"staff_2")
        self.staff_2.setStyleSheet(u"QPushButton{\n"
"  padding-left:-75\n"
";\n"
"}\n"
"\n"
"QPushButtonchecked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/user-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/images/user-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.staff_2.setIcon(icon8)
        self.staff_2.setIconSize(QSize(100, 20))
        self.staff_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.staff_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 145, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setIcon(icon2)
        self.settings_2.setIconSize(QSize(100, 20))

        self.verticalLayout_6.addWidget(self.settings_2)

        self.pushButton_14 = QPushButton(self.icon_text_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon5)
        self.pushButton_14.setIconSize(QSize(100, 20))

        self.verticalLayout_6.addWidget(self.pushButton_14)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        icon9 = QIcon()
        icon9.addFile(u":/images/bars-solid (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon9)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 24, -1, 24)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(False)
        self.label.setFont(font2)

        self.verticalLayout_11.addWidget(self.label)

        self.label_2 = QLabel(self.header_widget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        self.label_2.setFont(font3)

        self.verticalLayout_11.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(384, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/icons8-administrator-48.png"))

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_12.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(920, 741))
        self.main_screen_widget.setMaximumSize(QSize(950, 741))
        self.main_screen_widget.setStyleSheet(u"\n"
"background-color: rgb(244, 244, 244);")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 931, 867))
        self.stackedWidget.setMaximumSize(QSize(950, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 30, 291, 121))
        self.frame.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 100, 291, 21))
        self.label_7.setStyleSheet(u"background-color: rgb(183, 224, 255);")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(220, 20, 61, 51))
        self.label_20.setPixmap(QPixmap(u":/images/users-solid (1).ico"))
        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 10, 51, 31))
        font4 = QFont()
        font4.setFamilies([u"Trebuchet MS"])
        font4.setPointSize(20)
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 50, 91, 21))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setKerning(False)
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 170, 291, 121))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 255, 127);\n"
"background-color: rgb(116, 255, 92);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(210, 10, 71, 71))
        self.label_21.setPixmap(QPixmap(u":/images/user-check-solid (1).ico"))
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 100, 291, 21))
        self.label_25.setStyleSheet(u"background-color: rgb(208, 255, 170);")
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 51, 31))
        font6 = QFont()
        font6.setFamilies([u"Trebuchet MS"])
        font6.setPointSize(21)
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 50, 61, 21))
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 310, 291, 121))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 110, 37);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(210, 10, 71, 71))
        self.label_22.setPixmap(QPixmap(u":/images/user-xmark-solid (1).ico"))
        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 100, 291, 21))
        self.label_26.setStyleSheet(u"background-color: rgb(255, 164, 17);")
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 51, 31))
        self.label_33.setFont(font6)
        self.label_33.setStyleSheet(u"color: rgb(208, 208, 208);\n"
"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 50, 91, 21))
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 450, 291, 121))
        self.frame_4.setStyleSheet(u"background-color: rgb(153, 0, 0);\n"
"background-color: rgb(213, 9, 23);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(210, 10, 71, 71))
        self.label_23.setPixmap(QPixmap(u":/images/person-cane-solid (1).ico"))
        self.label_27 = QLabel(self.frame_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 100, 291, 21))
        self.label_27.setStyleSheet(u"background-color: rgb(255, 33, 74);")
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 10, 51, 31))
        self.label_35.setFont(font6)
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 50, 101, 21))
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(30, 590, 291, 121))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 89);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(210, 10, 71, 71))
        self.label_24.setPixmap(QPixmap(u":/images/wheelchair-solid (1).ico"))
        self.label_28 = QLabel(self.frame_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 100, 291, 21))
        self.label_28.setStyleSheet(u"background-color: rgb(161, 0, 241);")
        self.label_37 = QLabel(self.frame_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 10, 51, 31))
        self.label_37.setFont(font6)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_38 = QLabel(self.frame_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 50, 171, 21))
        self.label_38.setFont(font5)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(350, 30, 561, 341))
        self.frame_6.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_39 = QLabel(self.frame_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(180, 100, 251, 91))
        font7 = QFont()
        font7.setPointSize(23)
        self.label_39.setFont(font7)
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(350, 390, 561, 331))
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 19, 113);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_40 = QLabel(self.frame_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(140, 80, 281, 91))
        self.label_40.setFont(font7)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 250, 311, 141))
        font8 = QFont()
        font8.setPointSize(25)
        self.label_8.setFont(font8)
        self.label_8.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 20, 571, 31))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.layoutWidget1 = QWidget(self.widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 351, 32))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.widget_2 = QWidget(self.page_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 20, 331, 701))
        self.widget_2.setStyleSheet(u"background-color: rgb(153, 153, 153);")
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 60, 281, 31))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 40, 51, 16))
        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 120, 61, 16))
        self.label_42 = QLabel(self.widget_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(180, 120, 49, 16))
        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 240, 281, 31))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_3 = QComboBox(self.widget_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(20, 310, 281, 31))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 151, 101, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 151, 113, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_43 = QLabel(self.widget_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(30, 220, 31, 16))
        self.label_44 = QLabel(self.widget_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(30, 290, 49, 16))
        self.label_45 = QLabel(self.widget_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(30, 440, 81, 16))
        self.label_46 = QLabel(self.widget_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(30, 370, 71, 16))
        self.lineEdit_4 = QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 470, 271, 31))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_4 = QComboBox(self.widget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(20, 390, 281, 31))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget_2 = QStackedWidget(self.page_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(350, 50, 571, 671))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 255, 127);\n"
"background-color: rgb(149, 149, 149);")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.label_47 = QLabel(self.page_14)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(210, 20, 151, 21))
        self.label_47.setFont(font)
        self.label_48 = QLabel(self.page_14)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(30, 80, 61, 16))
        self.lineEdit_5 = QLineEdit(self.page_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(30, 100, 471, 31))
        self.lineEdit_5.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.page_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 170, 471, 31))
        self.lineEdit_6.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_49 = QLabel(self.page_14)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 150, 81, 16))
        self.lineEdit_7 = QLineEdit(self.page_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(30, 240, 471, 31))
        self.lineEdit_7.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_50 = QLabel(self.page_14)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(30, 220, 81, 16))
        self.lineEdit_8 = QLineEdit(self.page_14)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(30, 360, 231, 31))
        self.lineEdit_8.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_51 = QLabel(self.page_14)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(40, 340, 49, 16))
        self.lineEdit_9 = QLineEdit(self.page_14)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(280, 360, 231, 31))
        self.lineEdit_9.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_52 = QLabel(self.page_14)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(280, 340, 49, 16))
        self.comboBox_5 = QComboBox(self.page_14)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(30, 440, 231, 31))
        self.comboBox_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_53 = QLabel(self.page_14)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(40, 420, 61, 16))
        self.lineEdit_10 = QLineEdit(self.page_14)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(280, 440, 231, 31))
        self.lineEdit_10.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_54 = QLabel(self.page_14)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(280, 420, 49, 16))
        self.lineEdit_11 = QLineEdit(self.page_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(30, 520, 231, 31))
        self.lineEdit_11.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.label_55 = QLabel(self.page_14)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(30, 500, 61, 16))
        self.stackedWidget_2.addWidget(self.page_14)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.page_16.setStyleSheet(u"background-color: rgb(158, 255, 223);")
        self.stackedWidget_2.addWidget(self.page_16)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.page_15.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.stackedWidget_2.addWidget(self.page_15)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 250, 311, 141))
        self.label_10.setFont(font8)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(290, 280, 311, 141))
        self.label_11.setFont(font8)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(310, 210, 311, 141))
        self.label_12.setFont(font8)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 230, 391, 141))
        self.label_13.setFont(font8)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 220, 311, 141))
        self.label_14.setFont(font8)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(270, 240, 311, 141))
        self.label_15.setFont(font8)
        self.stackedWidget.addWidget(self.page_9)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(290, 250, 311, 141))
        self.label_17.setFont(font8)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_11)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 220, 311, 141))
        font9 = QFont()
        font9.setPointSize(24)
        self.label_16.setFont(font9)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_10)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(280, 210, 311, 141))
        self.label_18.setFont(font8)
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.label_19 = QLabel(self.page_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(290, 250, 131, 141))
        self.label_19.setFont(font8)
        self.stackedWidget.addWidget(self.page_13)

        self.verticalLayout_12.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.official_2.toggled.connect(self.officials_dropdown.hide)
        self.resident_2.toggled.connect(self.residents_dropdown.setHidden)
        self.official_2.toggled.connect(self.officials_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.official_2.toggled.connect(self.official_1.setChecked)
        self.resident_2.toggled.connect(self.resident_1.setChecked)
        self.certificate_2.toggled.connect(self.certificate_1.setChecked)
        self.blotter_2.toggled.connect(self.blotter_1.setChecked)
        self.staff_2.toggled.connect(self.staff_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.pushButton_14.toggled.connect(MainWindow.close)
        self.pushButton_8.toggled.connect(MainWindow.close)
        self.pushButton_14.toggled.connect(self.pushButton_8.setChecked)
        self.pushButton_3.toggled.connect(self.stackedWidget_2.setVisible)
        self.pushButton_2.toggled.connect(self.stackedWidget_2.setVisible)
        self.pushButton_4.toggled.connect(self.stackedWidget_2.setVisible)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.official_1.setText("")
        self.resident_1.setText("")
        self.certificate_1.setText("")
        self.blotter_1.setText("")
        self.staff_1.setText("")
        self.settings_1.setText("")
        self.pushButton_8.setText("")
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Barangay", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.official_2.setText(QCoreApplication.translate("MainWindow", u"Barangay Official    \u25bc", None))
        self.new_official.setText(QCoreApplication.translate("MainWindow", u"New Official", None))
        self.list_official.setText(QCoreApplication.translate("MainWindow", u"List of Officials", None))
        self.end_term.setText(QCoreApplication.translate("MainWindow", u"Official End Term", None))
        self.resident_2.setText(QCoreApplication.translate("MainWindow", u"Residents      \u25bc", None))
        self.new_resident.setText(QCoreApplication.translate("MainWindow", u"New Resident", None))
        self.all_resident.setText(QCoreApplication.translate("MainWindow", u"All Residents", None))
        self.archieve_resident.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        self.certificate_2.setText(QCoreApplication.translate("MainWindow", u"Barangay Certificate", None))
        self.blotter_2.setText(QCoreApplication.translate("MainWindow", u"Blotter Records", None))
        self.staff_2.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.settings_2.setText("")
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Barangay", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Profiling", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here...", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"                                  Total Population", None))
        self.label_20.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"POPULATION", None))
        self.label_21.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"                                  Total Voters", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"VOTERS", None))
        self.label_22.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"                                  Total Non-Voters", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"NON-VOTERS", None))
        self.label_23.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"                                  Total Senior Citizen", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"SENIOR CITIZEN", None))
        self.label_24.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"                                  Total PWD's", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"PERSON WITH DISABILITIES", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"BLOTTER GRAPH", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"MALE AND FEMALE  GRAPH", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Barangay Official", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Term From", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Voter", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"PWD", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Place of Birth", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Personal Details", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Suffix", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Religion", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"List of Officials", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Official ENd term", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Residents", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"New Resident", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"All Residents", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Blotter Records", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Barangay Certificates", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

