# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SorterWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def __init__(self):
        self.lb = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 390)
        MainWindow.setMinimumSize(QSize(700, 390))
        MainWindow.setMaximumSize(QSize(700, 390))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 702, 365))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(700, 0))
        self.label.setMaximumSize(QSize(700, 59))
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_src_dir = QPushButton(self.verticalLayoutWidget)
        self.pb_src_dir.setObjectName(u"pb_src_dir")
        self.pb_src_dir.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.pb_src_dir)

        self.lb_src_dir = QLabel(self.verticalLayoutWidget)
        self.lb_src_dir.setObjectName(u"lb_src_dir")
        self.lb_src_dir.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.lb_src_dir)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_dst_dir = QPushButton(self.verticalLayoutWidget)
        self.pb_dst_dir.setObjectName(u"pb_dst_dir")
        self.pb_dst_dir.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.pb_dst_dir)

        self.lb_dst_dir = QLabel(self.verticalLayoutWidget)
        self.lb_dst_dir.setObjectName(u"lb_dst_dir")
        self.lb_dst_dir.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.lb_dst_dir)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pb_go = QPushButton(self.verticalLayoutWidget)
        self.pb_go.setObjectName(u"pb_go")

        self.verticalLayout_2.addWidget(self.pb_go)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_current_number = QLabel(self.verticalLayoutWidget)
        self.lb_current_number.setObjectName(u"lb_current_number")
        self.lb_current_number.setMinimumSize(QSize(0, 10))
        self.lb_current_number.setMaximumSize(QSize(150, 30))
        self.lb_current_number.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_current_number)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(10, 30))

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lb_total_number = QLabel(self.verticalLayoutWidget)
        self.lb_total_number.setObjectName(u"lb_total_number")
        self.lb_total_number.setMaximumSize(QSize(150, 30))

        self.horizontalLayout_5.addWidget(self.lb_total_number)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_src_dir.clicked.connect(MainWindow.src_dir_slot)
        self.pb_dst_dir.clicked.connect(MainWindow.dst_dir_slot)
        self.progressBar.valueChanged.connect(MainWindow.progress_changed_slot)
        self.pb_go.clicked.connect(MainWindow.go_slot)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ORDENADOR DE FOTOS", None))
        self.pb_src_dir.setText(QCoreApplication.translate("MainWindow", u"Select Source Directory", None))
        self.lb_src_dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pb_dst_dir.setText(QCoreApplication.translate("MainWindow", u"Select Destination Directory", None))
        self.lb_dst_dir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pb_go.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.lb_current_number.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.lb_total_number.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi