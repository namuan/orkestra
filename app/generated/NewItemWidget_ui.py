# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/NewItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewItemWidget(object):
    def setupUi(self, NewItemWidget):
        NewItemWidget.setObjectName("NewItemWidget")
        NewItemWidget.resize(417, 44)
        font = QtGui.QFont()
        font.setPointSize(10)
        NewItemWidget.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(NewItemWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_new_item = QtWidgets.QPushButton(NewItemWidget)
        self.btn_new_item.setObjectName("btn_new_item")
        self.horizontalLayout.addWidget(self.btn_new_item)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(NewItemWidget)
        QtCore.QMetaObject.connectSlotsByName(NewItemWidget)

    def retranslateUi(self, NewItemWidget):
        _translate = QtCore.QCoreApplication.translate
        NewItemWidget.setWindowTitle(_translate("NewItemWidget", "Form"))
        self.btn_new_item.setText(_translate("NewItemWidget", "Add New"))
