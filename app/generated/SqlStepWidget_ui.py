# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/SqlStepWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_SqlStepWidget(object):
    def setupUi(self, SqlStepWidget):
        SqlStepWidget.setObjectName("SqlStepWidget")
        SqlStepWidget.resize(875, 755)
        self.verticalLayout = QtWidgets.QVBoxLayout(SqlStepWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.db_connection = QtWidgets.QFrame(SqlStepWidget)
        self.db_connection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.db_connection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.db_connection.setObjectName("db_connection")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.db_connection)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_connections = QtWidgets.QComboBox(self.db_connection)
        self.cmb_connections.setObjectName("cmb_connections")
        self.horizontalLayout.addWidget(self.cmb_connections)
        self.txt_connection_string = QtWidgets.QLineEdit(self.db_connection)
        self.txt_connection_string.setObjectName("txt_connection_string")
        self.horizontalLayout.addWidget(self.txt_connection_string)
        self.btn_db_connect = QtWidgets.QPushButton(self.db_connection)
        self.btn_db_connect.setObjectName("btn_db_connect")
        self.horizontalLayout.addWidget(self.btn_db_connect)
        self.verticalLayout.addWidget(self.db_connection)
        self.splitter = QtWidgets.QSplitter(SqlStepWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.sql_request = QtWidgets.QFrame(self.splitter)
        self.sql_request.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_request.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_request.setObjectName("sql_request")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sql_request)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab_request_elements = QtWidgets.QTabWidget(self.sql_request)
        self.tab_request_elements.setObjectName("tab_request_elements")
        self.description = QtWidgets.QWidget()
        self.description.setObjectName("description")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.description)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txt_sql_step_description = QtWidgets.QPlainTextEdit(self.description)
        self.txt_sql_step_description.setObjectName("txt_sql_step_description")
        self.horizontalLayout_4.addWidget(self.txt_sql_step_description)
        self.tab_request_elements.addTab(self.description, "")
        self.sql_query = QtWidgets.QWidget()
        self.sql_query.setObjectName("sql_query")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.sql_query)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_sql_query = QtWidgets.QPlainTextEdit(self.sql_query)
        self.txt_sql_query.setObjectName("txt_sql_query")
        self.horizontalLayout_6.addWidget(self.txt_sql_query)
        self.tab_request_elements.addTab(self.sql_query, "")
        self.horizontalLayout_2.addWidget(self.tab_request_elements)
        self.sql_response = QtWidgets.QFrame(self.splitter)
        self.sql_response.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sql_response.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sql_response.setObjectName("sql_response")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sql_response)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tab_response_elements = QtWidgets.QTabWidget(self.sql_response)
        self.tab_response_elements.setObjectName("tab_response_elements")
        self.raw_request = QtWidgets.QWidget()
        self.raw_request.setObjectName("raw_request")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.raw_request)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_results = QtWidgets.QTableWidget(self.raw_request)
        self.tbl_results.setObjectName("tbl_results")
        self.tbl_results.setColumnCount(0)
        self.tbl_results.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_results)
        self.frame = QtWidgets.QFrame(self.raw_request)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.num_page = QtWidgets.QSpinBox(self.frame)
        self.num_page.setObjectName("num_page")
        self.horizontalLayout_5.addWidget(self.num_page)
        self.lbl_total_pages = QtWidgets.QLabel(self.frame)
        self.lbl_total_pages.setObjectName("lbl_total_pages")
        self.horizontalLayout_5.addWidget(self.lbl_total_pages)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame)
        self.tab_response_elements.addTab(self.raw_request, "")
        self.horizontalLayout_3.addWidget(self.tab_response_elements)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(SqlStepWidget)
        self.tab_request_elements.setCurrentIndex(0)
        self.tab_response_elements.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SqlStepWidget)

    def retranslateUi(self, SqlStepWidget):
        _translate = QtCore.QCoreApplication.translate
        SqlStepWidget.setWindowTitle(_translate("SqlStepWidget", "Form"))
        self.btn_db_connect.setText(_translate("SqlStepWidget", "Connect"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.description), _translate("SqlStepWidget", "Description"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.sql_query), _translate("SqlStepWidget", "Query"))
        self.label.setText(_translate("SqlStepWidget", "Jump to page"))
        self.lbl_total_pages.setText(_translate("SqlStepWidget", "of 20"))
        self.tab_response_elements.setTabText(self.tab_response_elements.indexOf(self.raw_request), _translate("SqlStepWidget", "Results"))
