import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel

from Login import Ui_LoginWindow
from Registation import Ui_Registration
from Admin import Ui_Admin
from Admissions import Ui_Admission_Officer
#------------------------------------------------------------------
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
#------------------------------------------------------------------

#------------------------------------------------------------------
#	бд для списка специальностей
db1 = sqlite3.connect('list_kod_1.db')
cursor1 = db1.cursor()

cursor1.execute('''CREATE TABLE IF NOT EXISTS spec(
	kod TEXT,
    name1 TEXT
)''')
db1.commit()
for j in cursor1.execute('SELECT * FROM spec'):
	print(j)
#------------------------------------------------------------------

#------------------------------------------------------------------
#	бд для списка специальностей
db2 = sqlite3.connect('reg_abiturient.db')
cursor2 = db2.cursor()

cursor2.execute('''CREATE TABLE IF NOT EXISTS abiturient(
	name2 TEXT,
    ball TEXT,
	login TEXT,
	password TEXT
)''')
db1.commit()
for a in cursor2.execute('SELECT * FROM abiturient'):
	print(a)
#------------------------------------------------------------------

#	Хуйня открывающее базовое логина окно!
app = QtWidgets.QApplication(sys.argv)

LoginWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow()
ui.setupUi(LoginWindow)
LoginWindow.show()

def log():
	user_login = ui.log_login.text()
	user_password = ui.log_password.text()

	if len(user_login) == 0:
		return

	if len(user_password) == 0:
		return

	cursor.execute(f'SELECT password FROM users WHERE password="{user_password}"')
	check_pass = cursor.fetchall()

	cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
	check_login = cursor.fetchall()

	if check_pass[0][0] == user_password and check_login[0][0] == user_login:
		print('Успешная авторизация!')
		LoginWindow.close()
		return openAdmissions()
		
	else:
		print('Ошибка авторизации!')


# logic...

#	Функция открытия и возвращения окна "Регистрации" (через "Отмена" и "Зарегистрироваться")
def openRegistration():
	global Registration
	Registration = QtWidgets.QWidget()
	ui = Ui_Registration()
	ui.setupUi(Registration)
	LoginWindow.close()
	Registration.show()
	
	#	регистрация
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

	# where cursor1 is the cursor
	cursor1.execute(f'SELECT * FROM spec ')
	rows = cursor1.fetchall()

	for row in rows:
		inx = rows.index(row)
		ui.tableWidget.insertRow(inx)
		# add more if there is more columns in the database.
		ui.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		ui.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))

	def add():		
		spec_kod = ui.lineEdit.text()
		spec_name1 = ui.lineEdit_2.text()

		if len(spec_kod) == 0:
			return

		if len(spec_name1) == 0:
			return


		cursor1.execute(f'SELECT kod FROM spec WHERE kod="{spec_kod}"')
		if cursor1.fetchone() is None:
			cursor1.execute(f'INSERT INTO spec VALUES (?,?)',(spec_kod, spec_name1) )
			db1.commit()
			print("Добавление " + str(spec_kod) + " успешно!")
			for j in cursor1.execute('SELECT * FROM spec'):
				print(j)
		else:
			print("Такая запись уже имеется!")

	def delete():
		spec_kod = ui.lineEdit.text()
		spec_name1 = ui.lineEdit_2.text()

		if len(spec_kod) == 0:
			return

		if len(spec_name1) == 0:
			return


		cursor1.execute(f'SELECT kod FROM spec WHERE kod="{spec_kod}"')
		if cursor1.fetchone() is None:
			print(spec_kod + " - такой записи нет!")
		else:
			cursor1.execute(f'DELETE FROM spec WHERE kod = "{spec_kod}"')
			db1.commit()
			print(spec_kod + " успешно удалено!")
			for j in cursor1.execute('SELECT * FROM spec'):
				print(j)


	ui.pushButton.clicked.connect(add)
	ui.pushButton_2.clicked.connect(delete)

def openAdmissions():
	global Admission_Officer
	Admission_Officer = QtWidgets.QWidget()
	ui = Ui_Admission_Officer()
	ui.setupUi(Admission_Officer)
	Admission_Officer.show()
	LoginWindow.close()

	def reg_abiturient():
		abit_name = ui.abit_FIO.text()
		abit_ball = ui.abit_ball.text()
		abit_login = ui.abit_login.text()
		abit_password = ui.abit_password.text()

		if len(abit_name) == 0:
			return
		
		if len(abit_ball) == 0:
			return

		if len(abit_login) == 0:
			return

		if len(abit_password) == 0:
			return

		cursor2.execute(f'SELECT name2 FROM abiturient WHERE name2 ="{abit_name}"')
		if cursor2.fetchone() is None:
			cursor2.execute(f'INSERT INTO abiturient VALUES (?,?,?,?)',(abit_name, abit_ball ,abit_login, abit_password) )
			db2.commit()
			print("Регистрация абитуриента " + str(abit_name) + " успешна!")
			for a in cursor2.execute('SELECT * FROM abiturient'):
				print(a)
		else:
			print("Такая запись уже имеется!")

	def delete():
		abit_name = ui.abit_FIO.text()
		abit_ball = ui.abit_ball.text()
		abit_login = ui.abit_login.text()
		abit_password = ui.abit_password.text()

		if len(abit_name) == 0:
			return
		
		if len(abit_ball) == 0:
			return

		if len(abit_login) == 0:
			return

		if len(abit_password) == 0:
			return

		cursor2.execute(f'SELECT name2 FROM abiturient WHERE name2="{abit_name}"')
		if cursor2.fetchone() is None:
			print(abit_name + " - такой записи нет!")
		else:
			cursor2.execute(f'DELETE FROM abiturient WHERE name2 = "{abit_name}"')
			db2.commit()
			print(abit_name + " успешно удалено!")
			for a in cursor2.execute('SELECT * FROM abiturient'):
				print(a)

	def retrunToLoginWindow():
		Admission_Officer.close()
		LoginWindow.show()
	


	ui.abit_entry.clicked.connect(reg_abiturient)
	ui.abit_del.clicked.connect(delete)
	ui.abit_cancel.clicked.connect(retrunToLoginWindow)

	

#	Само открыте окна "Регистрации"
ui.log_reg.clicked.connect(openRegistration)
#	Открытие окна 
ui.log_entry.clicked.connect(log)



sys.exit(app.exec_())