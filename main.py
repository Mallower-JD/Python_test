import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from LoginWindow import Ui_LoginWindow
from Registation import Ui_Registration
from Admin import Ui_Admin

#	бд для регистриции
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

#	бд для списка специальностей
db1 = sqlite3.connect('list_kod_0.db')
cursor1 = db1.cursor()

cursor1.execute('''CREATE TABLE IF NOT EXISTS spec(
	kod TEXT,
    name1 TEXT
)''')
db1.commit()



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
	Admin = QtWidgets.QWidget()
	ui = Ui_Admin()
	ui.setupUi(Admin)
	LoginWindow.close()
	Admin.show()

	def add():		
		spec_kod = ui.lineEdit.text()
		spec_name1 = ui.lineEdit_2.text()

		if len(spec_kod) == 0:
			return

		if len(spec_name1) == 0:
			return


		cursor1.execute(f'SELECT * FROM spec')
		if cursor1.fetchone() is None:
			cursor1.execute(f'INSERT INTO spec VALUES (?,?)',(spec_kod, spec_name1) )
			db1.commit()
			print("Успешно!")
		for j in cursor1.execute('SELECT * FROM spec'):
			print(j)

		else:
			print("Такая запись уже имеется!")
		
		

	def change():
		change_value = ui.lineEdit_3.text()


 

	ui.pushButton.clicked.connect(add)
	ui.pushButton_3.clicked.connect(change)

#	Само открыте окна "Регистрации"
ui.log_reg.clicked.connect(openRegistration)
#	Открытие окна "Администратор"(список спец./ список мест)
ui.log_entry.clicked.connect(openAdministrator)



sys.exit(app.exec_())