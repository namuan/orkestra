# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/KeyValueListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_KeyValueListWidget(object):
    def setupUi(self, KeyValueListWidget):
        KeyValueListWidget.setObjectName("KeyValueListWidget")
        KeyValueListWidget.resize(458, 208)
        KeyValueListWidget.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(KeyValueListWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.key_value_item_list = QtWidgets.QListWidget(KeyValueListWidget)
        self.key_value_item_list.setObjectName("key_value_item_list")
        self.horizontalLayout.addWidget(self.key_value_item_list)

        self.retranslateUi(KeyValueListWidget)
        QtCore.QMetaObject.connectSlotsByName(KeyValueListWidget)

    def retranslateUi(self, KeyValueListWidget):
        _translate = QtCore.QCoreApplication.translate
        KeyValueListWidget.setWindowTitle(_translate("KeyValueListWidget", "Form"))
