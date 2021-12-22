import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel

from LoginWindow import Ui_LoginWindow
from Admin_new import Ui_Admin
from Admissions import Ui_Admission_Officer
from User import Ui_User
#------------------------------------------------------------------
#	бд пользователей и абитуриентов
db = sqlite3.connect('list_login.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
	role TEXT,
    login TEXT,
	password TEXT
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS abiturient(
	FIO TEXT,
	ball TEXT,
    login TEXT,
    password TEXT,
	role TEXT DEFAULT user
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS postup(
    FIO      TEXT,
    kod      TEXT,
    attestat TEXT,
    passport TEXT,
    propiska TEXT,
    faktich  TEXT,
    SNILS    TEXT,
    phone    TEXT,
    email    TEXT,
    ball     TEXT,
	role 	 TEXT DEFAULT user
)''')
db.commit()
for i in cursor.execute('SELECT * FROM users'):
	print(i)
#------------------------------------------------------------------

#------------------------------------------------------------------
#	бд списка специальностей
db1 = sqlite3.connect('list_kod.db')
cursor1 = db1.cursor()

cursor1.execute('''CREATE TABLE IF NOT EXISTS spec(
	kod TEXT,
    name1 TEXT
)''')
db1.commit()
#------------------------------------------------------------------

#	Функция открывающее базовое логина окно!
app = QtWidgets.QApplication(sys.argv)

LoginWindow = QtWidgets.QMainWindow()
ui = Ui_LoginWindow()
ui.setupUi(LoginWindow)
LoginWindow.show()

def log():
	user_login = ui.log_login.text()
	user_password = ui.log_password.text()
	user_role = ui.log_role.text()

	if len(user_login) == 0:
		return

	if len(user_password) == 0:
		return

	if len(user_role) == 0:
		return

	cursor.execute(f'SELECT password FROM users WHERE password="{user_password}"')
	check_pass = cursor.fetchall()

	cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
	check_login = cursor.fetchall()

	if user_role == "admin":
		if check_login[0][0] == user_login and check_pass[0][0] == user_password:	
			print('Успешная авторизация!')
			LoginWindow.close()
			return openAdministrator()
	elif user_role == "officer":
		if check_login[0][0] == user_login and check_pass[0][0] == user_password:
			print('Успешная авторизация!')
			LoginWindow.close()
			return openAdmissions()
	elif user_role == "user":
		if check_login[0][0] == user_login and check_pass[0][0] == user_password:
			print('Успешная авторизация!')
			LoginWindow.close()
			return openUser()


# logic...

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
	
	# where cursor1 is the cursor
	cursor.execute(f'SELECT * FROM users ')
	rows_1 = cursor.fetchall()

	for row_1 in rows_1:
		inx = rows_1.index(row_1)
		ui.tableWidget_2.insertRow(inx)
		# add more if there is more columns in the database.
		ui.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row_1[0]))
		ui.tableWidget_2.setItem(inx, 1, QTableWidgetItem(row_1[1]))
		ui.tableWidget_2.setItem(inx, 2, QTableWidgetItem(row_1[2]))

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

	def add_2():
		user_role = ui.lineEdit_4.text()
		user_login = ui.lineEdit_5.text()
		user_password = ui.lineEdit_6.text()

		if len(user_role) == 0:
			return

		if len(user_login) == 0:
			return

		if len(user_password) == 0:
			return


		cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
		if cursor.fetchone() is None:
			cursor.execute(f'INSERT INTO users VALUES (?,?,?)',(user_role, user_login, user_password) )
			db.commit()
			print("Добавление " + str(user_login) + " успешно!")
			for i in cursor.execute('SELECT * FROM users'):
				print(i)
		else:
			print("Такая запись уже имеется!")

	def delete2():
		user_role = ui.lineEdit_4.text()
		user_login = ui.lineEdit_5.text()
		user_password = ui.lineEdit_6.text()

		if len(user_role) == 0:
			return

		if len(user_login) == 0:
			return

		if len(user_password) == 0:
			return

		cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
		if cursor.fetchone() is None:
			print(user_login + " - такой записи нет!")
		else:
			cursor.execute(f'DELETE FROM users WHERE login = "{user_login}"')
			db.commit()
			print(user_login + " успешно удалено!")
			for i in cursor.execute('SELECT * FROM users'):
				print(i)
	def returnToLoginWindow():
		Admin.close()
		LoginWindow.show()

	ui.pushButton_3.clicked.connect(returnToLoginWindow)
	ui.pushButton.clicked.connect(add)
	ui.pushButton_2.clicked.connect(delete)
	ui.reg.clicked.connect(add_2)
	ui.delete_2.clicked.connect(delete2)

# Функция открытия окна "Служащего приемной комиссии"
def openAdmissions():
	global Admission_Officer
	Admission_Officer = QtWidgets.QWidget()
	ui = Ui_Admission_Officer()
	ui.setupUi(Admission_Officer)
	Admission_Officer.show()
	LoginWindow.close()

	# where cursor1 is the cursor
	cursor.execute(f'SELECT ball, FIO FROM abiturient ')
	rows = cursor.fetchall()

	for row in rows:
		inx = rows.index(row)
		ui.tableWidget.insertRow(inx)
		# add more if there is more columns in the database.
		ui.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		ui.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))

	def reg_abiturient():
		abit_FIO = ui.abit_FIO.text()
		abit_ball = ui.abit_ball.text()
		abit_login = ui.abit_login.text()
		abit_password = ui.abit_password.text()
		abit_role = "user"

		if len(abit_FIO) == 0:
			return
		
		if len(abit_ball) == 0:
			return

		if len(abit_login) == 0:
			return

		if len(abit_password) == 0:
			return

		cursor.execute(f'SELECT FIO FROM abiturient WHERE FIO ="{abit_FIO}"')
		if cursor.fetchone() is None:
			cursor.execute(f'INSERT INTO abiturient VALUES (?,?,?,?,?)',(abit_FIO, abit_ball ,abit_login, abit_password, abit_role) )
			db.commit()
			print("Регистрация абитуриента " + str(abit_FIO) + " успешна!")
			for a in cursor.execute('SELECT * FROM abiturient'):
				print(a)
		else:
			print("Такая запись уже имеется!")

	def delete():
		abit_FIO = ui.abit_FIO.text()
		abit_ball = ui.abit_ball.text()
		abit_login = ui.abit_login.text()
		abit_password = ui.abit_password.text()

		if len(abit_FIO) == 0:
			return
		
		if len(abit_ball) == 0:
			return

		if len(abit_login) == 0:
			return

		if len(abit_password) == 0:
			return

		cursor.execute(f'SELECT FIO FROM abiturient WHERE FIO="{abit_FIO}"')
		if cursor.fetchone() is None:
			print(abit_FIO + " - такой записи нет!")
		else:
			cursor.execute(f'DELETE FROM abiturient WHERE FIO = "{abit_FIO}"')
			db.commit()
			print(abit_FIO + " успешно удалено!")
			for a in cursor.execute('SELECT * FROM abiturient'):
				print(a)

	def retrunToLoginWindow():
		Admission_Officer.close()
		LoginWindow.show()
	
	ui.abit_entry.clicked.connect(reg_abiturient)
	ui.abit_del.clicked.connect(delete)
	ui.abit_cancel.clicked.connect(retrunToLoginWindow)

# Функция открытия окна "Абитуриент"
def openUser():
	global User
	User = QtWidgets.QWidget()
	ui = Ui_User()
	ui.setupUi(User)
	User.show()
	
	# where cursor1 is the cursor
	cursor.execute(f'SELECT ball, FIO FROM abiturient ')
	rows = cursor.fetchall()

	for row in rows:
		inx = rows.index(row)
		ui.tableWidget.insertRow(inx)
		# add more if there is more columns in the database.
		ui.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		ui.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))

	def add_3():
		ab_FIO = ui.lineEdit.text()
		ab_kod = ui.lineEdit_2.text()
		ab_attestat = ui.lineEdit_3.text()
		ab_passport = ui.lineEdit_4.text()
		ab_propiska = ui.lineEdit_5.text()
		ab_faktich = ui.lineEdit_6.text()
		ab_SNILS = ui.lineEdit_7.text()
		ab_phone = ui.lineEdit_8.text()
		ab_email = ui.lineEdit_9.text()
		ab_ball = ui.lineEdit_10.text()
		ab_role = "user"

		if len(ab_FIO) == 0:
			return

		if len(ab_kod) == 0:
			return

		if len(ab_attestat) == 0:
			return

		if len(ab_passport) == 0:
			return

		if len(ab_propiska) == 0:
			return

		if len(ab_faktich) == 0:
			return

		if len(ab_SNILS) == 0:
			return

		if len(ab_phone) == 0:
			return

		if len(ab_email) == 0:
			return

		if len(ab_ball) == 0:
			return
		
		cursor.execute(f'SELECT FIO FROM postup WHERE FIO ="{ab_FIO}"')
		if cursor.fetchone() is None:
			cursor.execute(f'INSERT INTO postup VALUES (?,?,?,?,?,?,?,?,?,?,?)',(ab_FIO, ab_kod, ab_attestat, ab_passport, ab_propiska, ab_faktich, ab_SNILS, ab_phone, ab_email, ab_ball, ab_role) )
			db.commit()
			print("Регистрация абитуриента " + str(ab_FIO) + " успешна!")
			for a in cursor.execute('SELECT * FROM postup'):
				print(a)
		else:
			print("Такая запись уже имеется!")
			

	def delete3():
		ab_FIO = ui.lineEdit.text()
		ab_kod = ui.lineEdit_2.text()
		ab_attestat = ui.lineEdit_3.text()
		ab_passport = ui.lineEdit_4.text()
		ab_propiska = ui.lineEdit_5.text()
		ab_faktich = ui.lineEdit_6.text()
		ab_SNILS = ui.lineEdit_7.text()
		ab_phone = ui.lineEdit_8.text()
		ab_email = ui.lineEdit_9.text()
		ab_ball = ui.lineEdit_10.text()

		if len(ab_FIO) == 0:
			return

		if len(ab_kod) == 0:
			return

		if len(ab_attestat) == 0:
			return

		if len(ab_passport) == 0:
			return

		if len(ab_propiska) == 0:
			return

		if len(ab_faktich) == 0:
			return

		if len(ab_SNILS) == 0:
			return

		if len(ab_phone) == 0:
			return

		if len(ab_email) == 0:
			return

		if len(ab_ball) == 0:
			return
		
		cursor.execute(f'SELECT FIO FROM postup WHERE FIO ="{ab_FIO}"')
		if cursor.fetchone() is None:
			print(ab_FIO + " - такой записи нет!")
		else:
			cursor.execute(f'DELETE FROM postup WHERE FIO = "{ab_FIO}"')
			db.commit()
			print(ab_FIO + " успешно удалено!")
			for a in cursor.execute('SELECT * FROM postup'):
				print(a)

	def returnToLoginWindow():
		User.close()
		LoginWindow.show()

	ui.pushButton_3.clicked.connect(returnToLoginWindow)
	ui.pushButton.clicked.connect(add_3)
	ui.pushButton_2.clicked.connect(delete3)


#	Открытие окна 
ui.log_entry.clicked.connect(log)

sys.exit(app.exec_())