# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/HttpStepWidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_HttpStepWidget(object):
    def setupUi(self, HttpStepWidget):
        HttpStepWidget.setObjectName("HttpStepWidget")
        HttpStepWidget.resize(875, 755)
        self.verticalLayout = QtWidgets.QVBoxLayout(HttpStepWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.http_path = QtWidgets.QFrame(HttpStepWidget)
        self.http_path.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.http_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.http_path.setObjectName("http_path")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.http_path)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_http_method = QtWidgets.QComboBox(self.http_path)
        self.cmb_http_method.setObjectName("cmb_http_method")
        self.horizontalLayout.addWidget(self.cmb_http_method)
        self.txt_http_url = QtWidgets.QLineEdit(self.http_path)
        self.txt_http_url.setObjectName("txt_http_url")
        self.horizontalLayout.addWidget(self.txt_http_url)
        self.btn_send_request = QtWidgets.QPushButton(self.http_path)
        self.btn_send_request.setObjectName("btn_send_request")
        self.horizontalLayout.addWidget(self.btn_send_request)
        self.verticalLayout.addWidget(self.http_path)
        self.http_request = QtWidgets.QFrame(HttpStepWidget)
        self.http_request.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.http_request.setFrameShadow(QtWidgets.QFrame.Raised)
        self.http_request.setObjectName("http_request")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.http_request)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab_request_elements = QtWidgets.QTabWidget(self.http_request)
        self.tab_request_elements.setObjectName("tab_request_elements")
        self.description = QtWidgets.QWidget()
        self.description.setObjectName("description")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.description)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txt_http_step_description = QtWidgets.QPlainTextEdit(self.description)
        self.txt_http_step_description.setObjectName("txt_http_step_description")
        self.horizontalLayout_4.addWidget(self.txt_http_step_description)
        self.tab_request_elements.addTab(self.description, "")
        self.header_params = QtWidgets.QWidget()
        self.header_params.setObjectName("header_params")
        self.tab_request_elements.addTab(self.header_params, "")
        self.query_params = QtWidgets.QWidget()
        self.query_params.setObjectName("query_params")
        self.tab_request_elements.addTab(self.query_params, "")
        self.form_params = QtWidgets.QWidget()
        self.form_params.setObjectName("form_params")
        self.tab_request_elements.addTab(self.form_params, "")
        self.request_body = QtWidgets.QWidget()
        self.request_body.setObjectName("request_body")
        self.tab_request_elements.addTab(self.request_body, "")
        self.horizontalLayout_2.addWidget(self.tab_request_elements)
        self.verticalLayout.addWidget(self.http_request)
        self.http_response = QtWidgets.QFrame(HttpStepWidget)
        self.http_response.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.http_response.setFrameShadow(QtWidgets.QFrame.Raised)
        self.http_response.setObjectName("http_response")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.http_response)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tab_response_elements = QtWidgets.QTabWidget(self.http_response)
        self.tab_response_elements.setObjectName("tab_response_elements")
        self.raw_request = QtWidgets.QWidget()
        self.raw_request.setObjectName("raw_request")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.raw_request)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txt_raw_request = QtWidgets.QPlainTextEdit(self.raw_request)
        self.txt_raw_request.setObjectName("txt_raw_request")
        self.horizontalLayout_5.addWidget(self.txt_raw_request)
        self.tab_response_elements.addTab(self.raw_request, "")
        self.raw_response = QtWidgets.QWidget()
        self.raw_response.setObjectName("raw_response")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.raw_response)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_raw_response = QtWidgets.QPlainTextEdit(self.raw_response)
        self.txt_raw_response.setObjectName("txt_raw_response")
        self.horizontalLayout_6.addWidget(self.txt_raw_response)
        self.tab_response_elements.addTab(self.raw_response, "")
        self.formatted_response = QtWidgets.QWidget()
        self.formatted_response.setObjectName("formatted_response")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.formatted_response)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txt_formatted_response = QtWidgets.QPlainTextEdit(self.formatted_response)
        self.txt_formatted_response.setObjectName("txt_formatted_response")
        self.horizontalLayout_7.addWidget(self.txt_formatted_response)
        self.tab_response_elements.addTab(self.formatted_response, "")
        self.horizontalLayout_3.addWidget(self.tab_response_elements)
        self.verticalLayout.addWidget(self.http_response)

        self.retranslateUi(HttpStepWidget)
        self.tab_request_elements.setCurrentIndex(0)
        self.tab_response_elements.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HttpStepWidget)

    def retranslateUi(self, HttpStepWidget):
        _translate = QtCore.QCoreApplication.translate
        HttpStepWidget.setWindowTitle(_translate("HttpStepWidget", "Form"))
        self.btn_send_request.setText(_translate("HttpStepWidget", "Send"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.description),
                                             _translate("HttpStepWidget", "Description"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.header_params),
                                             _translate("HttpStepWidget", "Headers"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.query_params),
                                             _translate("HttpStepWidget", "Query Params"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.form_params),
                                             _translate("HttpStepWidget", "Form Params"))
        self.tab_request_elements.setTabText(self.tab_request_elements.indexOf(self.request_body),
                                             _translate("HttpStepWidget", "Request Body"))
        self.tab_response_elements.setTabText(self.tab_response_elements.indexOf(self.raw_request),
                                              _translate("HttpStepWidget", "Raw Request"))
        self.tab_response_elements.setTabText(self.tab_response_elements.indexOf(self.raw_response),
                                              _translate("HttpStepWidget", "Raw Response"))
        self.tab_response_elements.setTabText(self.tab_response_elements.indexOf(self.formatted_response),
                                              _translate("HttpStepWidget", "Formatted Response"))
