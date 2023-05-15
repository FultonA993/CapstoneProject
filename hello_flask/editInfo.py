from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit
import subprocess
import sys
from myDictionary import dictionary
import re
import json
from PySide6.QtWidgets import QMessageBox

class MyApplication_edit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Forsyth Family Medical Practice Employee Information')
        self.setMinimumSize(400, 200)
        # menu bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet('color: #6ECCAF;')
        file_menu = menu_bar.addMenu("&File")
        home_action = file_menu.addAction("Back")
        home_action.triggered.connect(self.goHome)   
        clear_action = file_menu.addAction("Clear")
        clear_action.triggered.connect(self.clear_data)
        save_action = file_menu.addAction("Save")
        save_action.triggered.connect(self.save_data)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_action = edit_menu.addAction("Edit Entry")
        #edit_action.triggered.connect(self.edit_data)

        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Set the background color
        self.setStyleSheet('background-color: #344D67')

        #self.label = QLabel("Select item to edit:")
        
        self.comboBox = QComboBox(self)
        self.comboBox.setStyleSheet('color: white;')
        self.comboBox.addItem("Email")
        self.comboBox.addItem("Phone Number")
        self.comboBox.addItem("Title")
        self.comboBox.addItem("Department")
        self.comboBox.addItem("Blacklist Status")
        self.comboBox.addItem("Credential Status")
        self.comboBox.addItem("Salary")
        self.comboBox.addItem("Hours Worked")
        self.comboBox.addItem("Age")
        #self.comboBox.currentIndexChanged.connect(self.update_textbox)

        #self.textbox = QLineEdit(self)
        self.editBox = QLineEdit(self)
        self.label1 = QtWidgets.QLabel('Employee ID:')
        self.label1.setStyleSheet('color: white;')
        self.textbox1 = QtWidgets.QLineEdit()
        self.label2 = QtWidgets.QLabel('First Name:')
        self.label2.setStyleSheet('color: white;')
        self.textbox2 = QtWidgets.QLineEdit()
        self.label3 = QtWidgets.QLabel('Last Name:')
        self.label3.setStyleSheet('color: white;')
        self.textbox3 = QtWidgets.QLineEdit()
        self.label4 = QtWidgets.QLabel('Email:')
        self.label4.setStyleSheet('color: white;')
        self.textbox4 = QtWidgets.QLineEdit()
        self.label5 = QtWidgets.QLabel('Phone Number:')
        self.label5.setStyleSheet('color: white;')
        self.textbox5 = QtWidgets.QLineEdit()
        self.label6 = QtWidgets.QLabel('Title:')
        self.label6.setStyleSheet('color: white;')
        self.textbox6 = QtWidgets.QLineEdit()
        self.label7 = QtWidgets.QLabel('Department:')
        self.label7.setStyleSheet('color: white;')
        self.textbox7 = QtWidgets.QLineEdit()
        self.label8 = QtWidgets.QLabel('Blacklist Status:')
        self.label8.setStyleSheet('color: white;')
        self.textbox8 = QtWidgets.QLineEdit()
        self.label9 = QtWidgets.QLabel('Credential Status:')
        self.label9.setStyleSheet('color: white;')
        self.textbox9 = QtWidgets.QLineEdit()
        self.label10 = QtWidgets.QLabel('Salary:')
        self.label10.setStyleSheet('color: white;')
        self.textbox10 = QtWidgets.QLineEdit()
        self.label11 = QtWidgets.QLabel('Hours Worked:')
        self.label11.setStyleSheet('color: white;')
        self.textbox11 = QtWidgets.QLineEdit()
        self.label12 = QtWidgets.QLabel('Age:')
        self.label12.setStyleSheet('color: white;')
        self.textbox12 = QtWidgets.QLineEdit()
        self.label13 = QtWidgets.QLabel('Sex:')
        self.label13.setStyleSheet('color: white;')
        self.textbox13 = QtWidgets.QLineEdit()


        self.textbox1.setStyleSheet("background-color: #F3ECB0;")
        self.textbox2.setStyleSheet("background-color: #F3ECB0;")
        self.textbox3.setStyleSheet("background-color: #F3ECB0;")
        self.textbox4.setStyleSheet("background-color: #F3ECB0;")
        self.textbox5.setStyleSheet("background-color: #F3ECB0;")
        self.textbox6.setStyleSheet("background-color: #F3ECB0;")
        self.textbox7.setStyleSheet("background-color: #F3ECB0;")
        self.textbox8.setStyleSheet("background-color: #F3ECB0;")
        self.textbox9.setStyleSheet("background-color: #F3ECB0;")
        self.textbox10.setStyleSheet("background-color: #F3ECB0;")
        self.textbox11.setStyleSheet("background-color: #F3ECB0;")
        self.textbox12.setStyleSheet("background-color: #F3ECB0;")
        self.textbox13.setStyleSheet("background-color: #F3ECB0;")
        self.editBox.setStyleSheet("background-color: #F3ECB0;")
        self.editBox.setMinimumHeight(50)

        # Connect the textboxes to their respective functions
        self.textbox1.textChanged.connect(lambda: self.update_data('Employee ID', self.textbox1.text()))
        self.textbox2.textChanged.connect(lambda: self.update_data('First Name', self.textbox2.text()))
        self.textbox3.textChanged.connect(lambda: self.update_data('Last Name', self.textbox3.text()))
        self.textbox4.textChanged.connect(lambda: self.update_data('Email', self.textbox4.text()))
        self.textbox5.textChanged.connect(lambda: self.update_data('Phone Number', self.textbox5.text()))
        self.textbox6.textChanged.connect(lambda: self.update_data('Title', self.textbox6.text()))
        self.textbox7.textChanged.connect(lambda: self.update_data('Department', self.textbox7.text()))
        self.textbox8.textChanged.connect(lambda: self.update_data('Blacklist Status', self.textbox8.text()))
        self.textbox9.textChanged.connect(lambda: self.update_data('Credential Status', self.textbox9.text()))
        self.textbox10.textChanged.connect(lambda: self.update_data('Salary', self.textbox10.text()))
        self.textbox11.textChanged.connect(lambda: self.update_data('Hours Worked', self.textbox11.text()))
        self.textbox12.textChanged.connect(lambda: self.update_data('Age', self.textbox10.text()))
        self.textbox13.textChanged.connect(lambda: self.update_data('Sex', self.textbox11.text()))

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        #main_layout.addLayout(search_layout)  
        main_layout.addWidget(self.label1)
        main_layout.addWidget(self.textbox1)
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.textbox2)
        main_layout.addWidget(self.label3)
        main_layout.addWidget(self.textbox3)
        main_layout.addWidget(self.comboBox)
        #main_layout.addWidget(self.textbox)
        main_layout.addWidget(self.editBox)    

        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label1.setFont(font)
        self.textbox1.setFont(font)
        self.label2.setFont(font)
        self.textbox2.setFont(font)
        self.label3.setFont(font)
        self.textbox3.setFont(font)
        self.label4.setFont(font)
        self.textbox4.setFont(font)
        self.label5.setFont(font)
        self.textbox5.setFont(font)
        self.label6.setFont(font)
        self.textbox6.setFont(font)
        self.label7.setFont(font)
        self.textbox7.setFont(font)
        self.label8.setFont(font)
        self.textbox8.setFont(font)
        self.label9.setFont(font)
        self.textbox9.setFont(font)
        self.label10.setFont(font)
        self.textbox10.setFont(font)
        self.label11.setFont(font)
        self.textbox11.setFont(font)
        self.label12.setFont(font)
        self.textbox12.setFont(font)
        self.label13.setFont(font)
        self.textbox13.setFont(font)
        self.editBox.setFont(font)
        self.comboBox.setFont(font)
        
    def quit_app(self):
        self.app.quit()

    def search_item(self, search_string):
        # search the dictionary for the corresponding record
        record = None
        for key, value in dictionary.items():
            if search_string.lower() in value['first_name'].lower() or search_string.lower() in value['last_name'].lower():
                record = value
                break
    
        # update the text boxes
        if record is not None:
            self.textbox1.setText(str(key))
            self.textbox2.setText(record['first_name'])
            self.textbox3.setText(record['last_name'])
            self.textbox6.setText(record['job_title'])
            self.textbox4.setText(record['email'])
            self.textbox5.setText(record['phone'])
            self.textbox7.setText(record['department'])
            self.textbox8.setText(record['blacklist'])
            self.textbox9.setText(record['credentials'])
            self.textbox10.setText(record['salary'])
            self.textbox11.setText(record['hours_worked'])
            self.textbox12.setText(record['age'])
            self.textbox13.setText(record['sex'])
        else:
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox6.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
            self.textbox7.setText('')
            self.textbox8.setText('')
            self.textbox9.setText('')
            self.textbox10.setText('')
            self.textbox11.setText('')
            self.textbox12.setText('')
            self.textbox13.setText('')

    def clear_data(self):
            #self.search_bar.setText('')
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox6.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
            self.textbox7.setText('')
            self.textbox8.setText('')
            self.textbox9.setText('')
            self.textbox10.setText('')
            self.textbox11.setText('')
            self.textbox12.setText('')
            self.textbox13.setText('')
            self.editBox.setText('')
            
    def update_data(self, key, new_value):
        if key == 'Employee ID':
            dictionary['Employee ID'] = new_value
        elif key == 'First Name':
            dictionary['First Name'] = new_value
        elif key == 'Last Name':
            dictionary['Last Name'] = new_value
        elif key == 'Email':
            dictionary['Email'] = new_value
        elif key == 'Phone Number':
            dictionary['Phone Number'] = new_value
        elif key == 'Title':
            dictionary['Title'] = new_value
        elif key == 'Department':
            dictionary['Department'] = new_value
        elif key == 'Blacklist Status':
            dictionary['Blacklist Status'] = new_value
        elif key == 'Credential Status':
            dictionary['Credential Status'] = new_value
        elif key == 'Salary':
            dictionary['Salary'] = new_value
        elif key == 'Hours Worked':
            dictionary['Hours Worked'] = new_value
        elif key == 'Age':
            dictionary['age'] = new_value
        elif key == 'Sex':
            dictionary['sex'] = new_value
    def save_data(self):
        self.close()

    def goHome(self):
        self.close()

if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the main window
    main_window = MyApplication_edit()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())