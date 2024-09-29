# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1241, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1231, 860))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(90, 0))
        self.icon_only_widget.setMaximumSize(QSize(90, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/images/head1-1.png"))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 35, -1, 9)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/border-all-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/images/border-all-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(100, 20))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_1)

        self.offy_1 = QPushButton(self.icon_only_widget)
        self.offy_1.setObjectName(u"offy_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/users-gear-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/images/users-gear-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.offy_1.setIcon(icon1)
        self.offy_1.setIconSize(QSize(100, 20))
        self.offy_1.setCheckable(True)
        self.offy_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.offy_1)

        self.residents_1 = QPushButton(self.icon_only_widget)
        self.residents_1.setObjectName(u"residents_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/user-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/images/user-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.residents_1.setIcon(icon2)
        self.residents_1.setIconSize(QSize(100, 20))
        self.residents_1.setCheckable(True)
        self.residents_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.residents_1)

        self.blotter_1 = QPushButton(self.icon_only_widget)
        self.blotter_1.setObjectName(u"blotter_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/file-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/images/file-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.blotter_1.setIcon(icon3)
        self.blotter_1.setIconSize(QSize(100, 20))
        self.blotter_1.setCheckable(True)
        self.blotter_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.blotter_1)

        self.staff_1 = QPushButton(self.icon_only_widget)
        self.staff_1.setObjectName(u"staff_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/users-solid (1).ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/images/users-solid (1).ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.staff_1.setIcon(icon4)
        self.staff_1.setIconSize(QSize(100, 20))
        self.staff_1.setCheckable(True)
        self.staff_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.staff_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 408, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/images/gear-solid.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/images/gear-solid.ico", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        icon6 = QIcon()
        icon6.addFile(u":/images/right-from-bracket-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/images/right-from-bracket-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon6)
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.signout_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"   height:30px;\n"
"   border:none;\n"
"}\n"
"\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/head1-1.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
" padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setIconSize(QSize(100, 20))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.dashboard_2)

        self.officials = QFrame(self.icon_text_widget)
        self.officials.setObjectName(u"officials")
        self.officials.setFrameShape(QFrame.Shape.StyledPanel)
        self.officials.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.officials)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.offy_2 = QPushButton(self.officials)
        self.offy_2.setObjectName(u"offy_2")
        self.offy_2.setStyleSheet(u"QPushButton{\n"
" padding-left:-50px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.offy_2.setIcon(icon1)
        self.offy_2.setIconSize(QSize(100, 20))
        self.offy_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.offy_2)

        self.officials_dropdown = QFrame(self.officials)
        self.officials_dropdown.setObjectName(u"officials_dropdown")
        self.officials_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.officials_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.officials_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_official = QPushButton(self.officials_dropdown)
        self.add_official.setObjectName(u"add_official")
        self.add_official.setStyleSheet(u"QPushButton{\n"
" padding-left:-30px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.add_official.setCheckable(True)

        self.verticalLayout.addWidget(self.add_official)

        self.list_official = QPushButton(self.officials_dropdown)
        self.list_official.setObjectName(u"list_official")
        self.list_official.setStyleSheet(u"QPushButton{\n"
" padding-left:-20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.list_official.setCheckable(True)

        self.verticalLayout.addWidget(self.list_official)

        self.official_end = QPushButton(self.officials_dropdown)
        self.official_end.setObjectName(u"official_end")
        self.official_end.setStyleSheet(u"QPushButton{\n"
" padding-left:-5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.official_end.setCheckable(True)

        self.verticalLayout.addWidget(self.official_end)


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
        self.residents_2 = QPushButton(self.residents)
        self.residents_2.setObjectName(u"residents_2")
        self.residents_2.setStyleSheet(u"QPushButton{\n"
" padding-left:-40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.residents_2.setIcon(icon2)
        self.residents_2.setIconSize(QSize(100, 20))
        self.residents_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.residents_2)

        self.residents_dropdown = QFrame(self.residents)
        self.residents_dropdown.setObjectName(u"residents_dropdown")
        self.residents_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.residents_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.residents_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_residents = QPushButton(self.residents_dropdown)
        self.add_residents.setObjectName(u"add_residents")
        self.add_residents.setStyleSheet(u"QPushButton{\n"
" padding-left:-10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.add_residents.setCheckable(True)

        self.verticalLayout_2.addWidget(self.add_residents)

        self.list_residents = QPushButton(self.residents_dropdown)
        self.list_residents.setObjectName(u"list_residents")
        self.list_residents.setStyleSheet(u"QPushButton{\n"
" padding-left:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.list_residents.setCheckable(True)

        self.verticalLayout_2.addWidget(self.list_residents)

        self.archieve_residents = QPushButton(self.residents_dropdown)
        self.archieve_residents.setObjectName(u"archieve_residents")
        self.archieve_residents.setStyleSheet(u"QPushButton{\n"
" padding-left:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.archieve_residents.setCheckable(True)

        self.verticalLayout_2.addWidget(self.archieve_residents)


        self.verticalLayout_4.addWidget(self.residents_dropdown)


        self.verticalLayout_5.addWidget(self.residents)

        self.blotter_3 = QPushButton(self.icon_text_widget)
        self.blotter_3.setObjectName(u"blotter_3")
        self.blotter_3.setStyleSheet(u"QPushButton{\n"
" padding-left:-60px;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.blotter_3.setIcon(icon3)
        self.blotter_3.setIconSize(QSize(100, 20))
        self.blotter_3.setCheckable(True)

        self.verticalLayout_5.addWidget(self.blotter_3)

        self.staff_2 = QPushButton(self.icon_text_widget)
        self.staff_2.setObjectName(u"staff_2")
        self.staff_2.setStyleSheet(u"QPushButton{\n"
" padding-left:-70px;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"background-color:white;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.staff_2.setIcon(icon4)
        self.staff_2.setIconSize(QSize(100, 20))
        self.staff_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.staff_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 158, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.settings_2.setIcon(icon5)
        self.settings_2.setIconSize(QSize(100, 20))
        self.settings_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton:hover{\n"
"  color:#12B298\n"
"\n"
"}")
        self.signout_2.setIcon(icon6)
        self.signout_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.signout_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"background-color: rgb(255, 57, 159);")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 12, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/bars-solid (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_11.addWidget(self.label)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_6.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(326, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color: rgb(176, 176, 176);")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/images/icons8-administrator-48.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_12.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.widget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setMaximumSize(QSize(920, 741))
        self.main_screen_widget.setStyleSheet(u"background-color: rgb(235, 155, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(147, 147, 147);")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 881, 731))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 210, 49, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(310, 200, 241, 151))
        font2 = QFont()
        font2.setPointSize(28)
        self.label_8.setFont(font2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(340, 250, 241, 151))
        self.label_9.setFont(font2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(310, 230, 281, 151))
        self.label_10.setFont(font2)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.add_button = QPushButton(self.page_5)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 100, 131, 41))
        self.add_button.setStyleSheet(u"QPushButton{\n"
" background-color: #34D481;\n"
" color:white;\n"
"border:none;\n"
"border-radius:8px;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/user-check-solid (1).ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_button.setIcon(icon8)
        self.tableWidget = QTableWidget(self.page_5)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 200, 881, 511))
        self.tableWidget.setStyleSheet(u"QTableWidget{background-color: rgb(235, 235, 235);}\n"
"\n"
"QHeaderView::section{\n"
"\n"
" font-weight:bold;\n"
" background-color:black;\n"
" color:white;\n"
"\n"
"}\n"
"\n"
"")
        self.widget1 = QWidget(self.page_5)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 20, 271, 67))
        self.verticalLayout_13 = QVBoxLayout(self.widget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setPointSize(20)
        self.label_11.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_11)

        self.label_17 = QLabel(self.widget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_13.addWidget(self.label_17)

        self.widget2 = QWidget(self.page_5)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 150, 391, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gender_comboBox = QComboBox(self.widget2)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setMinimumSize(QSize(150, 0))
        self.gender_comboBox.setStyleSheet(u"QComboBox{ \n"
"border: 2px solid white;\n"
"border-radius:6px;\n"
"padding-left: 1px 18px 1px 3px;\n"
"height: 35px;\n"
"background-color:black;\n"
"color:white;\n"
"padding-left:15px;\n"
"selection-background-color: #298089;\n"
"}")

        self.horizontalLayout_6.addWidget(self.gender_comboBox)

        self.PWD_comboBox = QComboBox(self.widget2)
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.addItem("")
        self.PWD_comboBox.setObjectName(u"PWD_comboBox")
        self.PWD_comboBox.setStyleSheet(u"QComboBox{ \n"
"border: 2px solid white;\n"
"border-radius:6px;\n"
"padding-left: 1px 18px 1px 3px;\n"
"height: 35px;\n"
"background-color:black;\n"
"color:white;\n"
"padding-left:15px;\n"
"selection-background-color: #298089;\n"
"}")

        self.horizontalLayout_6.addWidget(self.PWD_comboBox)

        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 31))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(260, 230, 241, 151))
        self.label_12.setFont(font2)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(280, 210, 331, 151))
        self.label_13.setFont(font2)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(320, 230, 241, 151))
        self.label_14.setFont(font2)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 230, 241, 151))
        self.label_15.setFont(font2)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 230, 241, 151))
        self.label_16.setFont(font2)
        self.stackedWidget.addWidget(self.page_10)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_12.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.offy_2.toggled.connect(self.officials_dropdown.setHidden)
        self.residents_2.toggled.connect(self.residents_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.offy_1.toggled.connect(self.offy_2.setChecked)
        self.offy_2.toggled.connect(self.offy_1.setChecked)
        self.residents_1.toggled.connect(self.residents_2.setChecked)
        self.residents_2.toggled.connect(self.residents_1.setChecked)
        self.blotter_1.toggled.connect(self.blotter_3.setChecked)
        self.blotter_3.toggled.connect(self.blotter_1.setChecked)
        self.staff_1.toggled.connect(self.staff_2.setChecked)
        self.staff_2.toggled.connect(self.staff_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.offy_1.setText("")
        self.residents_1.setText("")
        self.blotter_1.setText("")
        self.staff_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Barangay Profiling", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.offy_2.setText(QCoreApplication.translate("MainWindow", u"Officials   \u25bc", None))
        self.add_official.setText(QCoreApplication.translate("MainWindow", u"Add Official", None))
        self.list_official.setText(QCoreApplication.translate("MainWindow", u"List of Official", None))
        self.official_end.setText(QCoreApplication.translate("MainWindow", u"Official End Term", None))
        self.residents_2.setText(QCoreApplication.translate("MainWindow", u"Residents  \u25bc", None))
        self.add_residents.setText(QCoreApplication.translate("MainWindow", u"Add Residents", None))
        self.list_residents.setText(QCoreApplication.translate("MainWindow", u"List of Residents", None))
        self.archieve_residents.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        self.blotter_3.setText(QCoreApplication.translate("MainWindow", u"Blotter", None))
        self.staff_2.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello!,", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to Barangay Profiling", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search here...", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add official", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"List official", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"OFficial end term", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add Residents", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FirstName", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LastName", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PWD", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Birthplace", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Resident Information", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Welcome to Resident's Information", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.PWD_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Voter", None))
        self.PWD_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.PWD_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"No", None))

        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search here...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"List of Residents", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Blotter", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

