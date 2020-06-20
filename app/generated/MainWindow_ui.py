# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 805)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.stepsFrame = QtWidgets.QFrame(self.splitter)
        self.stepsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stepsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stepsFrame.setObjectName("stepsFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stepsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cmb_folders = QtWidgets.QComboBox(self.stepsFrame)
        self.cmb_folders.setObjectName("cmb_folders")
        self.verticalLayout_2.addWidget(self.cmb_folders)
        self.txt_search_steps = QtWidgets.QLineEdit(self.stepsFrame)
        self.txt_search_steps.setObjectName("txt_search_steps")
        self.verticalLayout_2.addWidget(self.txt_search_steps)
        self.lst_steps = QtWidgets.QListView(self.stepsFrame)
        self.lst_steps.setObjectName("lst_steps")
        self.verticalLayout_2.addWidget(self.lst_steps)
        self.detailsFrame = QtWidgets.QFrame(self.splitter)
        self.detailsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailsFrame.setObjectName("detailsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.detailsFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.detailsFrame)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btn_new_http_request = QtWidgets.QPushButton(self.page)
        self.btn_new_http_request.setObjectName("btn_new_http_request")
        self.verticalLayout_3.addWidget(self.btn_new_http_request)
        self.btn_new_sql_request = QtWidgets.QPushButton(self.page)
        self.btn_new_sql_request.setObjectName("btn_new_sql_request")
        self.verticalLayout_3.addWidget(self.btn_new_sql_request)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.notesFrame = QtWidgets.QFrame(self.splitter_2)
        self.notesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notesFrame.setObjectName("notesFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.notesFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.notesFrame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txt_scratch_pad = QtWidgets.QTextEdit(self.notesFrame)
        self.txt_scratch_pad.setObjectName("txt_scratch_pad")
        self.verticalLayout.addWidget(self.txt_scratch_pad)
        self.horizontalLayout_2.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orkestra"))
        self.btn_new_http_request.setText(_translate("MainWindow", "New HTTP Request"))
        self.btn_new_sql_request.setText(_translate("MainWindow", "New SQL Request"))
        self.label_2.setText(_translate("MainWindow", "Notes"))
