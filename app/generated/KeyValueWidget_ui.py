# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/KeyValueWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyValueWidget(object):
    def setupUi(self, KeyValueWidget):
        KeyValueWidget.setObjectName("KeyValueWidget")
        KeyValueWidget.resize(473, 36)
        KeyValueWidget.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(KeyValueWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chk_item_enabled = QtWidgets.QCheckBox(KeyValueWidget)
        self.chk_item_enabled.setText("")
        self.chk_item_enabled.setChecked(True)
        self.chk_item_enabled.setObjectName("chk_item_enabled")
        self.horizontalLayout.addWidget(self.chk_item_enabled)
        self.txt_item_name = QtWidgets.QLineEdit(KeyValueWidget)
        self.txt_item_name.setStyleSheet("")
        self.txt_item_name.setObjectName("txt_item_name")
        self.horizontalLayout.addWidget(self.txt_item_name)
        self.txt_item_value = QtWidgets.QLineEdit(KeyValueWidget)
        self.txt_item_value.setObjectName("txt_item_value")
        self.horizontalLayout.addWidget(self.txt_item_value)
        self.btn_remove_item = QtWidgets.QToolButton(KeyValueWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/delete-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove_item.setIcon(icon)
        self.btn_remove_item.setObjectName("btn_remove_item")
        self.horizontalLayout.addWidget(self.btn_remove_item)

        self.retranslateUi(KeyValueWidget)
        QtCore.QMetaObject.connectSlotsByName(KeyValueWidget)

    def retranslateUi(self, KeyValueWidget):
        _translate = QtCore.QCoreApplication.translate
        KeyValueWidget.setWindowTitle(_translate("KeyValueWidget", "Form"))
        self.btn_remove_item.setText(_translate("KeyValueWidget", "-"))
