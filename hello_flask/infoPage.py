from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets, QtCore,QtGui
import subprocess
import sys
from myDictionary import dictionary
from databaseconn import connect_db
class MyApplication3(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Forsyth Family Medical Practice Employee Information')
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
        edit_menu.addAction("paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_action = edit_menu.addAction("Edit Entry")
        edit_action.triggered.connect(self.edit_data)

        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Set the background color
        self.setStyleSheet('background-color: #344D67')
                
        self.label1 = QtWidgets.QLabel('Employee ID:')
        self.label1.setStyleSheet('color: white;')
        self.textbox1 = QtWidgets.QLineEdit()
        self.textbox1.setReadOnly(True)
        self.label2 = QtWidgets.QLabel('First Name:')
        self.label2.setStyleSheet('color: white;')
        self.textbox2 = QtWidgets.QLineEdit()
        self.textbox2.setReadOnly(True)
        self.label3 = QtWidgets.QLabel('Last Name:')
        self.label3.setStyleSheet('color: white;')
        self.textbox3 = QtWidgets.QLineEdit()
        self.textbox3.setReadOnly(True)
        self.label4 = QtWidgets.QLabel('Email:')
        self.label4.setStyleSheet('color: white;')
        self.textbox4 = QtWidgets.QLineEdit()
        self.textbox4.setReadOnly(True)
        self.label5 = QtWidgets.QLabel('Phone Number:')
        self.label5.setStyleSheet('color: white;')
        self.textbox5 = QtWidgets.QLineEdit()
        self.textbox5.setReadOnly(True)
        self.label6 = QtWidgets.QLabel('Title:')
        self.label6.setStyleSheet('color: white;')
        self.textbox6 = QtWidgets.QLineEdit()
        self.textbox6.setReadOnly(True)
        self.label7 = QtWidgets.QLabel('Department:')
        self.label7.setStyleSheet('color: white;')
        self.textbox7 = QtWidgets.QLineEdit()
        self.textbox7.setReadOnly(True)        
        self.label8 = QtWidgets.QLabel('Age:')
        self.label8.setStyleSheet('color: white;')
        self.textbox8 = QtWidgets.QLineEdit()
        self.textbox8.setReadOnly(True)
        self.label9 = QtWidgets.QLabel('Sex:')
        self.label9.setStyleSheet('color: white;')
        self.textbox9 = QtWidgets.QLineEdit()
        self.textbox9.setReadOnly(True)

        self.textbox1.setStyleSheet("background-color: #F3ECB0;")
        self.textbox2.setStyleSheet("background-color: #F3ECB0;")
        self.textbox3.setStyleSheet("background-color: #F3ECB0;")
        self.textbox4.setStyleSheet("background-color: #F3ECB0;")
        self.textbox5.setStyleSheet("background-color: #F3ECB0;")
        self.textbox6.setStyleSheet("background-color: #F3ECB0;")
        self.textbox7.setStyleSheet("background-color: #F3ECB0;")
        self.textbox8.setStyleSheet("background-color: #F3ECB0;")
        self.textbox9.setStyleSheet("background-color: #F3ECB0;")
              
        # Add a label and search bar
        self.label = QtWidgets.QLabel('Search by ID:')
        self.label.setStyleSheet('color: white;')
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setStyleSheet("background-color: white;")
        self.search_bar.textChanged.connect(self.display_record)
        
        # Create the search layout
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.label)
        search_layout.addWidget(self.search_bar)
        self.search_bar.setFixedSize(300, 30)
        search_layout.addStretch()
        
        
        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.label1)
        main_layout.addWidget(self.textbox1)
        self.textbox1.setFixedSize(300, 30)
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.textbox2)
        self.textbox2.setFixedSize(300, 30)
        main_layout.addWidget(self.label3)
        main_layout.addWidget(self.textbox3)
        self.textbox3.setFixedSize(300, 30)

        main_layout.addWidget(self.label8)
        main_layout.addWidget(self.textbox8)
        self.textbox8.setFixedSize(300, 30)
        main_layout.addWidget(self.label9)
        main_layout.addWidget(self.textbox9)
        self.textbox9.setFixedSize(300, 30)
        
        main_layout.addWidget(self.label4)
        main_layout.addWidget(self.textbox4)
        self.textbox4.setFixedSize(300, 30)
        main_layout.addWidget(self.label5)
        main_layout.addWidget(self.textbox5)
        self.textbox5.setFixedSize(300, 30)
        main_layout.addWidget(self.label6)
        main_layout.addWidget(self.textbox6)
        self.textbox6.setFixedSize(300, 30)
        main_layout.addWidget(self.label7)
        main_layout.addWidget(self.textbox7)
        self.textbox7.setFixedSize(300, 30)

        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.search_bar.setFont(font)
        self.label.setFont(font)
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


    def quit_app(self):
        self.app.quit()

    def goHome(self):
        # Define the path to the program to run
        #program_path4 = "/Capstone/hello_flask/hello_flask/frontPage.py"
        # Run the program using subprocess
        #subprocess.Popen([sys.executable, program_path4])
        self.close()

    def display_record(self, key):
        key = self.search_bar.text()

        # Fetch the employee record from the database
        employee = fetch_employee_by_id(key)

        # Update the text boxes with the employee's information
        if employee is not None:
            self.textbox1.setText(str(employee.get('employee_id')))
            self.textbox2.setText(employee.get('first_name'))
            self.textbox3.setText(employee.get('last_name'))
            self.textbox4.setText(employee.get('email'))
            self.textbox5.setText(employee.get('phone'))
            self.textbox6.setText(employee.get('job_title'))
            self.textbox7.setText(str(employee.get('department')))
            self.textbox8.setText(str(employee.get('age')))
            self.textbox9.setText(employee.get('sex'))
        else:
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
            self.textbox6.setText('')
            self.textbox7.setText('')
            self.textbox8.setText('')
            self.textbox9.setText('')
            
    '''def search_item(self, search_string):
        # search the dictionary for the corresponding record
        employee_dict = fetch_employees()
        employee = employee_dict.get(1234)

        self.textbox1.setText(str(employee.get('employee_id')))
        self.textbox2.setText(employee.get('first_name'))
        self.textbox3.setText(employee.get('last_name'))
        self.textbox4.setText(employee.get('email'))
        self.textbox5.setText(employee.get('phone_number'))
        self.textbox6.setText(employee.get('title'))
        self.textbox7.setText(employee.get('department'))
        self.textbox8.setText(str(employee.get('age')))
        self.textbox9.setText(employee.get('sex'))

        # update the text boxes
        if record is not None:
            self.textbox1.setText(str(key))
            self.textbox2.setText(record['first_name'])
            self.textbox3.setText(record['last_name'])
            self.textbox6.setText(record['job_title'])
            self.textbox4.setText(record['email'])
            self.textbox5.setText(record['phone'])
            self.textbox7.setText(record['department'])
            self.textbox8.setText(record['age'])
            self.textbox9.setText(record['sex'])

        else:
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox6.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
            self.textbox7.setText('')'''
    
    def clear_data(self):
            self.search_bar.setText('')
            self.textbox1.setText('')
            self.textbox2.setText('')
            self.textbox3.setText('')
            self.textbox6.setText('')
            self.textbox4.setText('')
            self.textbox5.setText('')
            self.textbox7.setText('')

    def edit_data(self):
        program_path = "/Capstone/hello_flask/hello_flask/editInfo.py"
        subprocess.Popen([sys.executable, program_path])


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
                    'employee_id': row[0],
                    'title': row[1],
                    'first_name': row[2],
                    'last_name': row[3],
                    'address': row[4] + row[5] + row[6] + row[7], 
                    'phone': row[8],
                    'sex': row[9],
                    'age': row[10],
                    'job_title': row[11],
                    'department': row[12],
                    'email': row[13]
                }
                return employee
            
def fetch_employees(): 
    # Call the connect_db function to establish a connection to the database
    cursor = connect_db()
    query = "SELECT * FROM Employee"
    cursor.execute(query)
    result = cursor.fetchall()
    employees = []
    for row in result:
        employee = {'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3], 'phone': row[4], 'job_title': row[5], 'department': row[6], 'age': row[7], 'sex': row[8]}
        employees.append(employee)
    return employees
if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and show the main window
    main_window = MyApplication3()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())
