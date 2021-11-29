import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from LoginWindow import Ui_LoginWindow
from Registation import Ui_Registration

#	Хуйня открывающее базовое окно!
app = QtWidgets.QApplication(sys.argv)

LoginWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow()
ui.setupUi(LoginWindow)
LoginWindow.show()

# logic...

#	Функция открытия и возвращения окна "Регистрации" (через "Отмена" и "Зарегистрироваться")
def openRegistration():
	global Registration
	Registration = QtWidgets.QWidget()
	ui = Ui_Registration()
	ui.setupUi(Registration)
	LoginWindow.close()
	Registration.show()
	
	# Возвращение к окну "Логин"
	def retrunToLoginWindow():
		Registration.close()
		LoginWindow.show()

	ui.reg_cancel.clicked.connect(retrunToLoginWindow)
	ui.reg_registration.clicked.connect(retrunToLoginWindow)

#	Само открыте окна()
ui.log_reg.clicked.connect(openRegistration)


sys.exit(app.exec_())