# -*- coding: utf-8 -*-

# Admin implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(800, 550)
        self.tab_0 = QtWidgets.QTabWidget(Admin)
        self.tab_0.setGeometry(QtCore.QRect(0, 0, 800, 550))
        self.tab_0.setObjectName("tab_0")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setEnabled(True)
        self.tab_1.setObjectName("tab_1")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 230, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 230, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(40, 230, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 300, 150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(290, 20, 491, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tab_0.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 70, 230, 30))
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 70, 230, 30))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 170, 150, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tab_0.addTab(self.tab_2, "")

        self.retranslateUi(Admin)
        self.tab_0.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin"))
        self.lineEdit.setPlaceholderText(_translate("Admin", "Код"))
        self.lineEdit_2.setPlaceholderText(_translate("Admin", "Название"))
        self.pushButton.setText(_translate("Admin", "Добавить"))
        self.pushButton_2.setText(_translate("Admin", "Удалить"))
        self.tab_0.setTabText(self.tab_0.indexOf(self.tab_1), _translate("Admin", "Список специальностей"))
        self.lineEdit_3.setPlaceholderText(_translate("Admin", "Новое количество мест"))
        self.lineEdit_4.setText(_translate("Admin", "150"))
        self.pushButton_3.setText(_translate("Admin", "Изменить"))
        self.tab_0.setTabText(self.tab_0.indexOf(self.tab_2), _translate("Admin", "Количество мест"))