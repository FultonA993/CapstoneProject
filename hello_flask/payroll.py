from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets, QtCore,QtGui


import subprocess
import sys
from myDictionary import dictionary
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit
from databaseconn import connect_db

class MyApplication2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Forsyth Family Medical Practice Payroll')
        self.setMinimumSize(400, 500)

        # menu bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet('color: #6ECCAF;')
        file_menu = menu_bar.addMenu("&File")
        home_action = file_menu.addAction("Home")
        home_action.triggered.connect(self.goHome)   
        clear_action = file_menu.addAction("Clear")
        clear_action.triggered.connect(self.clear_data)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_action = edit_menu.addAction("Edit Entry")
        edit_action.triggered.connect(self.edit_data)

        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Set the background color
        self.setStyleSheet('background-color: #344D67')
        self.labelDate = QtWidgets.QLabel('Choose Start Date of Pay Period:')
        self.labelDate.setStyleSheet('color: white;')
        self.date_edit = QDateEdit()
        self.date_edit.setMaximumWidth(250)
        self.date_edit.setMaximumHeight(50)
        self.label1 = QtWidgets.QLabel('Employee ID:')
        self.label1.setStyleSheet('color: white;')
        self.textbox1 = QtWidgets.QLineEdit()
        self.textbox1.setMaximumWidth(250)
        self.textbox1.setMaximumHeight(50)
        self.textbox1.setReadOnly(True)
        self.label2 = QtWidgets.QLabel('First Name:')
        self.label2.setStyleSheet('color: white;')
        self.textbox2 = QtWidgets.QLineEdit()
        self.textbox2.setMaximumWidth(250)
        self.textbox2.setMaximumHeight(50)
        self.textbox2.setReadOnly(True)
        self.label3 = QtWidgets.QLabel('Last Name:')
        self.label3.setStyleSheet('color: white;')
        self.textbox3 = QtWidgets.QLineEdit()
        self.textbox3.setMaximumWidth(250)
        self.textbox3.setMaximumHeight(50)
        self.textbox3.setReadOnly(True)
        self.label4 = QtWidgets.QLabel('Salary:')
        self.label4.setStyleSheet('color: white;')
        self.textbox4 = QtWidgets.QLineEdit()
        self.textbox4.setMaximumWidth(250)
        self.textbox4.setMaximumHeight(50)
        self.textbox4.setReadOnly(True)
        self.label5 = QtWidgets.QLabel('Hours Worked:')
        self.label5.setStyleSheet('color: white;')
        self.textbox5 = QtWidgets.QLineEdit()
        self.textbox5.setMaximumWidth(250)
        self.textbox5.setMaximumHeight(50)

        self.textbox5.setReadOnly(True)
        self.button1 = QtWidgets.QPushButton("Request PTO", self)
        self.button1.setMaximumWidth(250)
        self.button1.setMaximumHeight(50)
        
        
        # Set the background color of the button to blue
        self.button1.setStyleSheet("background-color: #ADE792;")   
        self.button1.clicked.connect(self.open_program1)
        self.date_edit.setStyleSheet("background-color: #F3ECB0;")
        self.textbox1.setStyleSheet("background-color: #F3ECB0;")
        self.textbox2.setStyleSheet("background-color: #F3ECB0;")
        self.textbox3.setStyleSheet("background-color: #F3ECB0;")
        self.textbox4.setStyleSheet("background-color: #F3ECB0;")
        self.textbox5.setStyleSheet("background-color: #F3ECB0;")
              
        # Add a label and search bar
        self.label = QtWidgets.QLabel('Search:')
        self.label.setStyleSheet('color: white;')
        self.search_bar = QtWidgets.QLineEdit()
        
        self.search_bar.setStyleSheet("background-color: white;")
        self.search_bar.textChanged.connect(self.search_item)
        self.search_bar.textChanged.connect(self.display_record)
        
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.label)
        search_layout.addWidget(self.search_bar)
        self.search_bar.setFixedSize(200, 30)
        search_layout.addStretch()
        search_layout.setAlignment(QtCore.Qt.AlignHCenter)


# Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.labelDate)
        main_layout.addWidget(self.date_edit)
        self.date_edit.setFixedSize(300, 30)
        main_layout.addWidget(self.label1)
        main_layout.addWidget(self.textbox1)
        self.textbox1.setFixedSize(300, 30)
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.textbox2)
        self.textbox2.setFixedSize(300, 30)
        main_layout.addWidget(self.label3)
        main_layout.addWidget(self.textbox3)
        self.textbox3.setFixedSize(300, 30)
        main_layout.addWidget(self.label4)
        main_layout.addWidget(self.textbox4)
        self.textbox4.setFixedSize(300, 30)
        main_layout.addWidget(self.label5)
        main_layout.addWidget(self.textbox5)
        self.textbox5.setFixedSize(300, 30)
        main_layout.addWidget(self.button1)
        self.button1.setFixedSize(200, 50)

        

# Align the main layout center
        main_layout.setAlignment(QtCore.Qt.AlignCenter)

# Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        


        font = QtGui.QFont()
        font.setPointSize(15)
        self.search_bar.setFont(font)
        self.label.setFont(font)
        self.labelDate.setFont(font)
        self.date_edit.setFont(font)
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
        self.button1.setFont(font)

    def quit_app(self):
        self.app.quit()

    def goHome(self):
        # Define the path to the program to run
        #program_path4 = "/Capstone/hello_flask/hello_flask/frontPage.py"
        # Run the program using subprocess
        #subprocess.Popen([sys.executable, program_path4])
        self.close()

    #adjust this method 
    def search_item(self, search_string):
        # search the dictionary for the corresponding record
        record = None
        for key, value in dictionary.items():
            if search_string.lower() == value['key'].lower():
                record = value
                break
        # update the text boxes
        if record is not None:
            self.textbox4.setText(record['salary'])
            self.textbox5.setText(record['hours_worked'])
        else:
            self.textbox4.setText('')
            self.textbox5.setText('')

    def open_program1(self):
        # Define the path to the program to run
        program_path = "FultonA993/CapstoneProject/hello_flask/rPTO.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path])
        self.close()

    def clear_data(self):
            self.search_bar.setText('')
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
    def edit_data(self, dictionary):
        program_path = "FultonA993/CapstoneProject/hello_flask/editInfo.py"
        subprocess.Popen([sys.executable, program_path])

        key_entry = self.textbox3
        key = key_entry.text()
        key = key_entry.text()
        new_value = key.text()

        # update the dictionary with the new value
        dictionary[key] = new_value

    def display_record(self, key):
        key = self.search_bar.text()

        # Fetch the employee record from the database
        employee = fetch_employee_by_id(key)

        # Update the text boxes with the employee's information
        if employee is not None:
            self.textbox1.setText(str(employee.get('employee_id')))
            self.textbox2.setText(employee.get('first_name'))
            self.textbox3.setText(employee.get('last_name'))
        else:
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')

def fetch_employee_by_id(emp_id):
            cursor = connect_db()
            query = "SELECT * FROM Employee WHERE EmployeeID = ?"
            cursor.execute(query, emp_id)
            row = cursor.fetchone()
            cursor.close()
            if row is None:
                return None
            else:
                employee = {
                    'employee_id': row[1],
                    'first_name': row[3],
                    'last_name': row[2],
                }
                return employee

if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and show the main window
    main_window = MyApplication2()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())

