from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QDialog, QGridLayout, QPushButton, QLineEdit
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets,QtGui
import subprocess
import sys
from databaseconn import connect_db
from myDictionary import dictionary
from employee_data import

class MyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        # Set the window title and size
        self.setWindowTitle('Forsyth Family Medical Practice Directory')
        self.setMinimumSize(720, 780)

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
        
        # Create the list box
        self.list_box = QtWidgets.QListWidget(self)
        self.populate_listbox()
        self.list_box.doubleClicked.connect(self.on_listbox_select)
        self.list_box.setStyleSheet("background-color: #F3ECB0;")

        # Add a label and search bar
        self.label = QtWidgets.QLabel('Search:')
        self.label.setStyleSheet('color: white;')
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.textChanged.connect(self.search_item)
        self.search_bar.setStyleSheet("background-color: white;")
        # Create the search layout
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.label)
        
        search_layout.addWidget(self.search_bar)
        search_layout.addStretch()
        
        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.list_box)
        
        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)



        font = QtGui.QFont()
        font1 = QtGui.QFont()
        font1.setPointSize(18)
        font.setPointSize(15)
        self.search_bar.setFont(font)
        self.label.setFont(font)
        self.list_box.setFont(font1)
        
    def quit_app(self):
        self.app.quit()

    def goHome(self):
        # Define the path to the program to run
        #program_path4 = "FultonA993/CapstoneProject/hello_flask/frontPage.py"
        # Run the program using subprocess
        #subprocess.Popen([sys.executable, program_path4])
        self.close()

    def search_item(self, text):
        items = [self.list_box.item(i) for i in range(self.list_box.count())]
        matches = [item for item in items if text.lower() in item.text().lower()]
        for item in items:
            if item in matches:
                item.setHidden(False)
            else:
                item.setHidden(True)

    #this code uses myDictionary
    def populate_list(self):
        for key, value in dictionary.items():
            item_text = f"{value['job_title']} {value['first_name']} {value['last_name']}"
            item = QtWidgets.QListWidgetItem(item_text)
            self.list_box.addItem(item)
    

    def clear_data(self):
            # Clear
            self.search_bar.setText('')

    def on_listbox_select(self):
        item = self.list_box.currentItem()
        name = item.text()
        self.fetch_employee_info(name)
        self.open_program4()

    '''def populate_listbox(self):
                names = fetch_employees()
                self.list_box.addItems(names)'''

    '''def fetch_employee_info(self, name):
        # Call the connect_to_db function to establish a connection to the database
        cursor = connect_db()
        query = f"SELECT * FROM Employee WHERE FirstName='{name.split()[0]}' AND LastName='{name.split()[1]}'"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return {'Name': f"{row[1]} {row[2]}", 'Position': row[3], 'Email': row[4]}
        else:
            return {'Name': 'Not found', 'Position': 'Not found', 'Email': 'Not found'}'''

    def open_program4(self):
            # Define the path to the program to run
            program_path4 = "/Capstone/hello_flask/hello_flask/infoPage.py"

            # Run the program using subprocess
            subprocess.Popen([sys.executable, program_path4])

'''def fetch_employees(): 
        # Call the connect_to_db function to establish a connection to the database
        cursor = connect_db()
        query = "SELECT EmployeeID, Title, FirstName, LastName FROM Employee"
        cursor.execute(query)
        result = cursor.fetchall()
        name_list = [f"{name[1]} {name[2]} {name[3]} ({name[0]})" for name in result]
        return name_list'''

if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication([])
    
    # Create and show the main window
    main_window = MyApplication()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())
