from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
import subprocess
import sys
from myDictionary import dictionary
from databaseconn import connect_db

class MyApplication5(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Forsyth Family Medical Practice Blacklist')
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
        #edit_action.triggered.connect(self.edit_data)
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Set the background color
        self.setStyleSheet('background-color: #344D67')

        self.label1 = QtWidgets.QLabel('Title:')
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
        self.label4 = QtWidgets.QLabel('Blacklist Details:')
        self.label4.setStyleSheet('color: white;')

        # Create the list box
        self.textbox1.setStyleSheet("background-color: #F3ECB0;")
        self.textbox2.setStyleSheet("background-color: #F3ECB0;")
        self.textbox3.setStyleSheet("background-color: #F3ECB0;")

        self.list_box = QtWidgets.QLineEdit()
        self.list_box.setStyleSheet("padding: 5px; border: 1px solid gray; background-color: #F3ECB0; selection-background-color: blue;")
        self.list_box.setMinimumHeight(250)
        #self.populate_list()
        #self.list_box.setStyleSheet("background-color: #F3ECB0;")

        # Add a label and search bar
        self.label = QtWidgets.QLabel('Search by ID:')
        self.label.setStyleSheet('color: white;')
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.textChanged.connect(self.search_item)
        #self.search_bar.textChanged.connect(self.populate_list)
        self.search_bar.textChanged.connect(self.display_record)
        self.search_bar.setStyleSheet("background-color: white;")
        # Create the search layout
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.label)
        search_layout.addWidget(self.search_bar)
        search_layout.addStretch()

        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.label1)
        main_layout.addWidget(self.textbox1)
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.textbox2)
        main_layout.addWidget(self.label3)
        main_layout.addWidget(self.textbox3)
        main_layout.addWidget(self.label4)
        main_layout.addWidget(self.list_box)

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
        self.list_box.setFont(font)
        self.label.setFont(font)
        self.search_bar.setFont(font)

    def quit_app(self):
        self.app.quit()

    def goHome(self):
        # Define the path to the program to run
        #program_path4 = "/Capstone/hello_flask/hello_flask/frontPage.py"
        # Run the program using subprocess
        #subprocess.Popen([sys.executable, program_path4])
        self.close()

    def search_item(self, search_string):
        # search the dictionary for the corresponding record
        record = None
        for key, value in dictionary.items():
            if search_string.lower() == value['key'].lower():
                record = value
                break
        # update the text boxes
        if record is not None:
            self.list_box.setText(record['blacklist'])
        else:
            self.list_box.setText('')

    def clear_data(self):
            # Clear
            self.search_bar.setText('')

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
    main_window = MyApplication5()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())
