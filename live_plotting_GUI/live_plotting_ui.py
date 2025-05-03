# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'live_plotting_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 6, 0, 1, 1)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        self.start_button.setFont(font)

        self.gridLayout_2.addWidget(self.start_button, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.tare_button = QPushButton(self.centralwidget)
        self.tare_button.setObjectName(u"tare_button")
        sizePolicy.setHeightForWidth(self.tare_button.sizePolicy().hasHeightForWidth())
        self.tare_button.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.tare_button, 3, 1, 1, 1)

        self.countdownLabel = QLabel(self.centralwidget)
        self.countdownLabel.setObjectName(u"countdownLabel")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.countdownLabel.setFont(font1)
        self.countdownLabel.setStyleSheet(u" color: red")

        self.gridLayout_2.addWidget(self.countdownLabel, 8, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_2.addLayout(self.verticalLayout_2, 7, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.absline_button = QPushButton(self.centralwidget)
        self.absline_button.setObjectName(u"absline_button")
        sizePolicy.setHeightForWidth(self.absline_button.sizePolicy().hasHeightForWidth())
        self.absline_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.absline_button, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.absbar_button = QPushButton(self.centralwidget)
        self.absbar_button.setObjectName(u"absbar_button")
        sizePolicy.setHeightForWidth(self.absbar_button.sizePolicy().hasHeightForWidth())
        self.absbar_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.absbar_button, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(220, 133))
        self.label_4.setPixmap(QPixmap(u"../../Screen Shot 2024-11-08 at 4.19.17 PM.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QSize(220, 133))
        self.label_5.setPixmap(QPixmap(u"../../Screen Shot 2024-11-04 at 1.37.53 PM.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.diffbar_button = QPushButton(self.centralwidget)
        self.diffbar_button.setObjectName(u"diffbar_button")
        sizePolicy.setHeightForWidth(self.diffbar_button.sizePolicy().hasHeightForWidth())
        self.diffbar_button.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SoftwareUpdateAvailable))
        self.diffbar_button.setIcon(icon)

        self.gridLayout.addWidget(self.diffbar_button, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.diffline_button = QPushButton(self.centralwidget)
        self.diffline_button.setObjectName(u"diffline_button")
        sizePolicy.setHeightForWidth(self.diffline_button.sizePolicy().hasHeightForWidth())
        self.diffline_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.diffline_button, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(220, 133))
        self.label_6.setPixmap(QPixmap(u"../../Screen Shot 2024-11-08 at 3.00.54 PM.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(220, 133))
        self.label_3.setMaximumSize(QSize(220, 133))
        self.label_3.setPixmap(QPixmap(u"../../Screen Shot 2024-11-04 at 1.38.21 PM.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start!", None))
        self.tare_button.setText(QCoreApplication.translate("MainWindow", u"Tare", None))
        self.countdownLabel.setText(QCoreApplication.translate("MainWindow", u"Start rowing in: 5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"3.    Start! ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Force Sensor for Rowing Biomechanics", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1.    Choose Graph Format ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2.    Tare Sensors", None))
        self.absline_button.setText(QCoreApplication.translate("MainWindow", u"Absolute Force Line Graph", None))
        self.absbar_button.setText(QCoreApplication.translate("MainWindow", u"Absolute Force Bar Graph", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.diffbar_button.setText(QCoreApplication.translate("MainWindow", u"Force Difference Bar Graph", None))
        self.diffline_button.setText(QCoreApplication.translate("MainWindow", u"Force Difference Line Graph", None))
        self.label_6.setText("")
        self.label_3.setText("")
    # retranslateUi

