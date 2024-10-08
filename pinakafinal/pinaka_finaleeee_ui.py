# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinaka_finaleeee.ui'
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
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1546, 860))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
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

        self.icon_text_widget = QWidget(self.layoutWidget)
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
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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

        self.horizontalSpacer_3 = QSpacerItem(484, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/images/icons8-administrator-48.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_12.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setMaximumSize(QSize(920, 741))
        self.main_screen_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 901, 731))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 330, 401, 101))
        self.frame.setStyleSheet(u"background-color: rgb(0, 94, 141);\n"
"color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 80, 401, 21))
        self.widget.setStyleSheet(u"background-color: rgb(57, 57, 86);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(150, 0, 91, 16))
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 10, 61, 61))
        self.label_7.setPixmap(QPixmap(u":/images/users-solid (1).ico"))
        self.population_label = QLabel(self.frame)
        self.population_label.setObjectName(u"population_label")
        self.population_label.setGeometry(QRect(10, 10, 31, 31))
        font3 = QFont()
        font3.setFamilies([u"Impact"])
        font3.setPointSize(24)
        self.population_label.setFont(font3)
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 50, 71, 21))
        self.label_17.setFont(font2)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 460, 401, 101))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 182);\n"
"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_5 = QWidget(self.frame_5)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 80, 401, 21))
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.label_32 = QLabel(self.widget_5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(150, 0, 91, 16))
        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(330, 10, 61, 61))
        self.label_33.setPixmap(QPixmap(u":/images/wheelchair-solid (1).ico"))
        self.pwd_label = QLabel(self.frame_5)
        self.pwd_label.setObjectName(u"pwd_label")
        self.pwd_label.setGeometry(QRect(10, 10, 31, 31))
        self.pwd_label.setFont(font3)
        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 50, 61, 21))
        self.label_35.setFont(font2)
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(480, 330, 401, 101))
        self.frame_6.setStyleSheet(u"background-color: rgb(0, 94, 141);\n"
"color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_6 = QWidget(self.frame_6)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(0, 80, 401, 21))
        self.widget_6.setStyleSheet(u"background-color: rgb(57, 57, 86);")
        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(160, 0, 91, 16))
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(330, 10, 61, 61))
        self.label_15.setPixmap(QPixmap(u":/images/users-solid (1).ico"))
        self.official_label = QLabel(self.frame_6)
        self.official_label.setObjectName(u"official_label")
        self.official_label.setGeometry(QRect(10, 10, 31, 31))
        self.official_label.setFont(font3)
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 50, 61, 21))
        self.label_18.setFont(font2)
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(480, 460, 401, 101))
        self.frame_7.setStyleSheet(u"background-color: rgb(0, 94, 141);\n"
"background-color: rgb(0, 108, 162);\n"
"color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_7 = QWidget(self.frame_7)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 80, 401, 21))
        self.widget_7.setStyleSheet(u"background-color: rgb(57, 57, 86);")
        self.label_19 = QLabel(self.widget_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(160, 0, 91, 16))
        self.male_label = QLabel(self.frame_7)
        self.male_label.setObjectName(u"male_label")
        self.male_label.setGeometry(QRect(10, 10, 31, 31))
        self.male_label.setFont(font3)
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 50, 61, 21))
        self.label_26.setFont(font2)
        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(310, 10, 91, 71))
        self.label_21.setPixmap(QPixmap(u":/images/icons8-boy-96 (2).png"))
        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(480, 590, 401, 101))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 88, 163);\n"
"color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_9 = QWidget(self.frame_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 80, 401, 21))
        self.widget_9.setStyleSheet(u"background-color: rgb(176, 27, 8);\n"
"background-color: rgb(255, 103, 209);")
        self.label_30 = QLabel(self.widget_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(160, 0, 91, 16))
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.frame_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(310, 10, 81, 71))
        self.label_34.setPixmap(QPixmap(u":/images/icons8-girl-96 (2).png"))
        self.female_label = QLabel(self.frame_8)
        self.female_label.setObjectName(u"female_label")
        self.female_label.setGeometry(QRect(10, 10, 31, 31))
        self.female_label.setFont(font3)
        self.label_42 = QLabel(self.frame_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 50, 51, 21))
        self.label_42.setFont(font2)
        self.frame_17 = QFrame(self.page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, 590, 401, 101))
        self.frame_17.setStyleSheet(u"background-color: rgb(0, 80, 0);\n"
"color: rgb(255, 255, 255);")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_19 = QWidget(self.frame_17)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(0, 80, 401, 21))
        self.widget_19.setStyleSheet(u"background-color: rgb(57, 57, 86);\n"
"background-color: rgb(0, 140, 0);")
        self.label_79 = QLabel(self.widget_19)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(140, 0, 91, 16))
        self.label_80 = QLabel(self.frame_17)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(330, 10, 61, 61))
        self.label_80.setPixmap(QPixmap(u":/images/icons8-file-96.png"))
        self.blotter_label = QLabel(self.frame_17)
        self.blotter_label.setObjectName(u"blotter_label")
        self.blotter_label.setGeometry(QRect(10, 10, 31, 31))
        self.blotter_label.setFont(font3)
        self.label_81 = QLabel(self.frame_17)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(10, 50, 91, 21))
        self.label_81.setFont(font2)
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 881, 311))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 10, 861, 301))
        self.label_20.setPixmap(QPixmap(u":/images/background (1).jpg"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 181, 41))
        font4 = QFont()
        font4.setPointSize(28)
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.official_table = QTableWidget(self.page_2)
        if (self.official_table.columnCount() < 13):
            self.official_table.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.official_table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.official_table.setObjectName(u"official_table")
        self.official_table.setGeometry(QRect(0, 110, 901, 611))
        self.official_table.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"	background-color: rgb(244, 249, 250);\n"
"}\n"
"")
        self.official_table.setAlternatingRowColors(True)
        self.layoutWidget_4 = QWidget(self.page_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 60, 401, 51))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.select_officialposition = QComboBox(self.layoutWidget_4)
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.addItem("")
        self.select_officialposition.setObjectName(u"select_officialposition")
        self.select_officialposition.setMinimumSize(QSize(150, 0))
        self.select_officialposition.setStyleSheet(u"QComboBox{ \n"
"border: 2px solid white;\n"
"border-radius:6px;\n"
"padding-left: 1px 18px 1px 3px;\n"
"height: 35px;\n"
"background-color:black;\n"
"color:white;\n"
"padding-left:15px;\n"
"selection-background-color: #298089;\n"
"}")

        self.horizontalLayout_9.addWidget(self.select_officialposition)

        self.search_official = QLineEdit(self.layoutWidget_4)
        self.search_official.setObjectName(u"search_official")
        self.search_official.setMinimumSize(QSize(0, 31))
        self.search_official.setMaximumSize(QSize(16777215, 31))
        self.search_official.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(65, 65, 65);")

        self.horizontalLayout_9.addWidget(self.search_official)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 291, 31))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.archieveofficial_table = QTableWidget(self.page_3)
        if (self.archieveofficial_table.columnCount() < 13):
            self.archieveofficial_table.setColumnCount(13)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(10, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(11, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.archieveofficial_table.setHorizontalHeaderItem(12, __qtablewidgetitem25)
        self.archieveofficial_table.setObjectName(u"archieveofficial_table")
        self.archieveofficial_table.setGeometry(QRect(0, 50, 901, 681))
        self.archieveofficial_table.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"	background-color: rgb(244, 249, 250);\n"
"}\n"
"")
        self.archieveofficial_table.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 271, 51))
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.residents_table = QTableWidget(self.page_4)
        if (self.residents_table.columnCount() < 15):
            self.residents_table.setColumnCount(15)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(10, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(11, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(12, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(13, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.residents_table.setHorizontalHeaderItem(14, __qtablewidgetitem40)
        self.residents_table.setObjectName(u"residents_table")
        self.residents_table.setGeometry(QRect(0, 120, 911, 611))
        self.residents_table.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"	background-color: rgb(244, 249, 250);\n"
"}\n"
"")
        self.residents_table.setAlternatingRowColors(True)
        self.select_residentgender = QComboBox(self.page_4)
        self.select_residentgender.addItem("")
        self.select_residentgender.addItem("")
        self.select_residentgender.addItem("")
        self.select_residentgender.setObjectName(u"select_residentgender")
        self.select_residentgender.setGeometry(QRect(11, 71, 150, 39))
        self.select_residentgender.setMinimumSize(QSize(150, 0))
        self.select_residentgender.setStyleSheet(u"QComboBox{ \n"
"border: 2px solid white;\n"
"border-radius:6px;\n"
"padding-left: 1px 18px 1px 3px;\n"
"height: 35px;\n"
"background-color:black;\n"
"color:white;\n"
"padding-left:15px;\n"
"selection-background-color: #298089;\n"
"}")
        self.search_resident = QLineEdit(self.page_4)
        self.search_resident.setObjectName(u"search_resident")
        self.search_resident.setGeometry(QRect(167, 75, 132, 31))
        self.search_resident.setMinimumSize(QSize(0, 31))
        self.search_resident.setMaximumSize(QSize(16777215, 31))
        self.search_resident.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 311, 31))
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.archieveresident_table = QTableWidget(self.page_5)
        if (self.archieveresident_table.columnCount() < 15):
            self.archieveresident_table.setColumnCount(15)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(7, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(8, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(9, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(10, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(11, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(12, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(13, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.archieveresident_table.setHorizontalHeaderItem(14, __qtablewidgetitem55)
        self.archieveresident_table.setObjectName(u"archieveresident_table")
        self.archieveresident_table.setGeometry(QRect(0, 50, 911, 681))
        self.archieveresident_table.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"	background-color: rgb(244, 249, 250);\n"
"}\n"
"")
        self.archieveresident_table.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_14 = QLabel(self.page_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 251, 41))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.blotter_table = QTableWidget(self.page_6)
        if (self.blotter_table.columnCount() < 7):
            self.blotter_table.setColumnCount(7)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.blotter_table.setHorizontalHeaderItem(6, __qtablewidgetitem62)
        self.blotter_table.setObjectName(u"blotter_table")
        self.blotter_table.setGeometry(QRect(0, 110, 901, 611))
        self.blotter_table.setStyleSheet(u"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QTableWidget {\n"
"   \n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"	background-color: rgb(244, 249, 250);\n"
"}\n"
"")
        self.blotter_table.setAlternatingRowColors(True)
        self.widget1 = QWidget(self.page_6)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 60, 281, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.search_blotter = QLineEdit(self.widget1)
        self.search_blotter.setObjectName(u"search_blotter")
        self.search_blotter.setMinimumSize(QSize(0, 31))
        self.search_blotter.setMaximumSize(QSize(16777215, 31))
        self.search_blotter.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(48, 48, 48);")

        self.horizontalLayout_6.addWidget(self.search_blotter)

        self.add_case = QPushButton(self.widget1)
        self.add_case.setObjectName(u"add_case")
        self.add_case.setMinimumSize(QSize(100, 35))
        self.add_case.setStyleSheet(u"background-color: rgb(143, 255, 112);\n"
"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_6.addWidget(self.add_case)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_16 = QLabel(self.page_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 131, 51))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_36 = QLabel(self.page_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(330, 30, 101, 91))
        self.label_36.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"}")
        self.label_36.setPixmap(QPixmap(u":/images/head1-2.png"))
        self.layoutWidget_7 = QWidget(self.page_7)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(30, 340, 341, 56))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.layoutWidget_7)
        self.label_38.setObjectName(u"label_38")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_38.setFont(font5)
        self.label_38.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_15.addWidget(self.label_38)

        self.lineEdit_7 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font5)
        self.lineEdit_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_15.addWidget(self.lineEdit_7)

        self.layoutWidget_8 = QWidget(self.page_7)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(30, 440, 341, 56))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.layoutWidget_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)
        self.label_39.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_16.addWidget(self.label_39)

        self.lineEdit_8 = QLineEdit(self.layoutWidget_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font5)
        self.lineEdit_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_16.addWidget(self.lineEdit_8)

        self.layoutWidget_9 = QWidget(self.page_7)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(30, 540, 341, 56))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.layoutWidget_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_17.addWidget(self.label_40)

        self.lineEdit_9 = QLineEdit(self.layoutWidget_9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font5)
        self.lineEdit_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_17.addWidget(self.lineEdit_9)

        self.widget_8 = QWidget(self.page_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(400, 210, 461, 431))
        self.widget_8.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(248, 248, 248);\n"
"\n"
"QWIdget{\n"
"border:none;	\n"
"border-radius:10px;\n"
"}")
        self.label_41 = QLabel(self.widget_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(140, 10, 181, 22))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_41.setFont(font6)
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit = QTextEdit(self.widget_8)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 40, 421, 351))
        font7 = QFont()
        font7.setBold(False)
        self.textEdit.setFont(font7)
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit.setReadOnly(False)
        self.layoutWidget1 = QWidget(self.page_7)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 240, 341, 56))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget1)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)
        self.label_37.setStyleSheet(u"background-color: rgb(3, 3, 3);")

        self.verticalLayout_13.addWidget(self.label_37)

        self.lineEdit_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_13.addWidget(self.lineEdit_2)

        self.stackedWidget.addWidget(self.page_7)

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
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(5)


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
        self.official_end.setText(QCoreApplication.translate("MainWindow", u"Archieve Official", None))
        self.residents_2.setText(QCoreApplication.translate("MainWindow", u"Residents  \u25bc", None))
        self.add_residents.setText(QCoreApplication.translate("MainWindow", u"Add Residents", None))
        self.list_residents.setText(QCoreApplication.translate("MainWindow", u"List of Residents", None))
        self.archieve_residents.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        self.blotter_3.setText(QCoreApplication.translate("MainWindow", u"Blotter", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.signout_2.setText(QCoreApplication.translate("MainWindow", u"Signout", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello!,", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to Barangay Profiling", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Population", None))
        self.label_7.setText("")
        self.population_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Total PWD's", None))
        self.label_33.setText("")
        self.pwd_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"PWD'S", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Officials", None))
        self.label_15.setText("")
        self.official_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Officials", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Total Male", None))
        self.male_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_21.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Total Female", None))
        self.label_34.setText("")
        self.female_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Total Cases", None))
        self.label_80.setText("")
        self.blotter_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Blotter Cases", None))
        self.label_20.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"List Official", None))
        ___qtablewidgetitem = self.official_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.official_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FirstName", None));
        ___qtablewidgetitem2 = self.official_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LastName", None));
        ___qtablewidgetitem3 = self.official_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"MI", None));
        ___qtablewidgetitem4 = self.official_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem5 = self.official_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem6 = self.official_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None));
        ___qtablewidgetitem7 = self.official_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem8 = self.official_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None));
        ___qtablewidgetitem9 = self.official_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Term Start", None));
        ___qtablewidgetitem10 = self.official_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Term End", None));
        ___qtablewidgetitem11 = self.official_table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem12 = self.official_table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.select_officialposition.setItemText(0, QCoreApplication.translate("MainWindow", u"Position", None))
        self.select_officialposition.setItemText(1, QCoreApplication.translate("MainWindow", u"Captain", None))
        self.select_officialposition.setItemText(2, QCoreApplication.translate("MainWindow", u"Secretary", None))
        self.select_officialposition.setItemText(3, QCoreApplication.translate("MainWindow", u"Treasurer", None))
        self.select_officialposition.setItemText(4, QCoreApplication.translate("MainWindow", u"Councilor", None))
        self.select_officialposition.setItemText(5, QCoreApplication.translate("MainWindow", u"Kagawad", None))
        self.select_officialposition.setItemText(6, QCoreApplication.translate("MainWindow", u"SK Kagawad", None))
        self.select_officialposition.setItemText(7, QCoreApplication.translate("MainWindow", u"Tanod", None))

        self.search_official.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search here...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Archieve Official", None))
        ___qtablewidgetitem13 = self.archieveofficial_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem14 = self.archieveofficial_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"FirstName", None));
        ___qtablewidgetitem15 = self.archieveofficial_table.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"LastName", None));
        ___qtablewidgetitem16 = self.archieveofficial_table.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"MI", None));
        ___qtablewidgetitem17 = self.archieveofficial_table.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem18 = self.archieveofficial_table.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem19 = self.archieveofficial_table.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None));
        ___qtablewidgetitem20 = self.archieveofficial_table.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem21 = self.archieveofficial_table.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None));
        ___qtablewidgetitem22 = self.archieveofficial_table.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Term Start", None));
        ___qtablewidgetitem23 = self.archieveofficial_table.horizontalHeaderItem(10)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Term End", None));
        ___qtablewidgetitem24 = self.archieveofficial_table.horizontalHeaderItem(11)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem25 = self.archieveofficial_table.horizontalHeaderItem(12)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"List of Residents", None))
        ___qtablewidgetitem26 = self.residents_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem27 = self.residents_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"FirstName", None));
        ___qtablewidgetitem28 = self.residents_table.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"LastName", None));
        ___qtablewidgetitem29 = self.residents_table.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"MI", None));
        ___qtablewidgetitem30 = self.residents_table.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem31 = self.residents_table.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Blood Type", None));
        ___qtablewidgetitem32 = self.residents_table.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem33 = self.residents_table.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"PWD", None));
        ___qtablewidgetitem34 = self.residents_table.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None));
        ___qtablewidgetitem35 = self.residents_table.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None));
        ___qtablewidgetitem36 = self.residents_table.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Birthplace", None));
        ___qtablewidgetitem37 = self.residents_table.horizontalHeaderItem(11)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem38 = self.residents_table.horizontalHeaderItem(12)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem39 = self.residents_table.horizontalHeaderItem(13)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem40 = self.residents_table.horizontalHeaderItem(14)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.select_residentgender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_residentgender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_residentgender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.search_resident.setText("")
        self.search_resident.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search here...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Archieve Residents", None))
        ___qtablewidgetitem41 = self.archieveresident_table.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem42 = self.archieveresident_table.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"FirstName", None));
        ___qtablewidgetitem43 = self.archieveresident_table.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"LastName", None));
        ___qtablewidgetitem44 = self.archieveresident_table.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"MI", None));
        ___qtablewidgetitem45 = self.archieveresident_table.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem46 = self.archieveresident_table.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Blood Type", None));
        ___qtablewidgetitem47 = self.archieveresident_table.horizontalHeaderItem(6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem48 = self.archieveresident_table.horizontalHeaderItem(7)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"PWD", None));
        ___qtablewidgetitem49 = self.archieveresident_table.horizontalHeaderItem(8)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None));
        ___qtablewidgetitem50 = self.archieveresident_table.horizontalHeaderItem(9)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None));
        ___qtablewidgetitem51 = self.archieveresident_table.horizontalHeaderItem(10)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Birthplace", None));
        ___qtablewidgetitem52 = self.archieveresident_table.horizontalHeaderItem(11)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem53 = self.archieveresident_table.horizontalHeaderItem(12)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem54 = self.archieveresident_table.horizontalHeaderItem(13)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem55 = self.archieveresident_table.horizontalHeaderItem(14)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Blotter Records", None))
        ___qtablewidgetitem56 = self.blotter_table.horizontalHeaderItem(0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Case No.", None));
        ___qtablewidgetitem57 = self.blotter_table.horizontalHeaderItem(1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Incident", None));
        ___qtablewidgetitem58 = self.blotter_table.horizontalHeaderItem(2)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Location of Incident", None));
        ___qtablewidgetitem59 = self.blotter_table.horizontalHeaderItem(3)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Date Incident", None));
        ___qtablewidgetitem60 = self.blotter_table.horizontalHeaderItem(4)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Date Reported", None));
        ___qtablewidgetitem61 = self.blotter_table.horizontalHeaderItem(5)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Person In-charge", None));
        ___qtablewidgetitem62 = self.blotter_table.horizontalHeaderItem(6)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.search_blotter.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search here...", None))
        self.add_case.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_36.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Zip Code", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"8000", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"District", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Tugbok District, Davao City", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"Barangay Mintal, Davao City", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"About Barangay Mintal:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">The objective of Barangay Mintal is to promote sustainable development, improve the quality of life for its residents, and preserve its rich cultural heritage. It aims to support local economic growth through livelihood programs, particularly in agriculture and trade, while fostering youth development and providing accessible education and healthcare services. Ensuring"
                        " peace and order, the barangay works closely with local law enforcement to maintain a secure environment. It also prioritizes environmental sustainability through waste management and conservation efforts, while preserving its Japanese legacy by maintaining historical landmarks and promoting cultural awareness. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Barangay Mintal emphasizes disaster preparedness and community resilience through effective risk management programs and response systems</span></p></body></html>", None))
        self.textEdit.setPlaceholderText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Barangay", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Barangay Mintal, Davao City", None))
    # retranslateUi

