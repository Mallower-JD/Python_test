import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from LoginWindow import Ui_LoginWindow
from Registation import Ui_Registration
from Admin import Ui_Admin

#	бд
db = sqlite3.connect('database_1.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
	name TEXT,
	login TEXT,
    password TEXT
)''')
db.commit()

for i in cursor.execute('SELECT * FROM users'):
    print(i)

#	Хуйня открывающее базовое логина окно!
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
	
	#	новая хуита
	def reg():
		user_name = ui.reg_FIO.text()
		user_login = ui.reg_login.text()
		user_password = ui.reg_password.text()

		if len(user_name) == 0:
			return

		if len(user_login) == 0:
			return

		if len(user_password) == 0:
			return

		cursor.execute(f'SELECT name FROM users WHERE name ="{user_name}"')
		if cursor.fetchone() is None:
			cursor.execute(f'INSERT INTO users VALUES (?,?,?)',(user_name, user_login, user_password) )
			db.commit()
			print("Регистрация пользователя " + str(user_name) + " успешна!")
			LoginWindow.show()
			Registration.close()
			for i in cursor.execute('SELECT * FROM users'):
				print(i)
		else:
			print("Такая запись уже имеется!")
			Registration.close()
			LoginWindow.show()


	# Возвращение к окну "Логин"
	def retrunToLoginWindow():
		Registration.close()
		LoginWindow.show()

	ui.reg_cancel.clicked.connect(retrunToLoginWindow)
	ui.reg_registration.clicked.connect(reg)

#	Функция открытия окна "Администратор" 
def openAdministrator():
	global Admin
	app = QtWidgets.QApplication(sys.argv)
	Admin = QtWidgets.QWidget()
	ui = Ui_Admin()
	ui.setupUi(Admin)
	LoginWindow.close()
	Admin.show()

	def add():
		#	бд
		db = sqlite3.connect('list_kod_0.db')
		cursor = db.cursor()

		cursor.execute('''CREATE TABLE IF NOT EXISTS users(
			kod TEXT
		)''')
		db.commit()
	
	ui.pushButton.clicked.connect(add)

#	Само открыте окна "Регистрации"
ui.log_reg.clicked.connect(openRegistration)
#	Открытие окна "Администратор"(список спец./ список мест)
ui.log_entry.clicked.connect(openAdministrator)



sys.exit(app.exec_())