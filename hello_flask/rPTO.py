from PySide6.QtCore import QEvent, QSize, Qt, QDate, QLocale
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter, QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget, QGridLayout, QTextEdit, QComboBox, QDateEdit, QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QDateEdit
import subprocess
import sys

class MyApplicationPTO(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Request Time Off')
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
        self.title_label = QtWidgets.QLabel("Time Off Request:")
        self.title_label.setStyleSheet('color: white;')
        self.label3 = QtWidgets.QLabel('Dates:')
        self.label3.setStyleSheet('color: white;')
        self.date_edit = QDateEdit()
        self.date_edit2 = QDateEdit()

        '''current_date = QDate.currentDate()
        self.date_edit.setDate(current_date)
        self.date_edit2.setDate(current_date)'''

        self.label4 = QtWidgets.QLabel('Type:')
        self.label4.setStyleSheet('color: white;')
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem("Vacation")
        self.combobox.addItem("Sick")
        self.combobox.addItem("Personal")
        self.label5 = QtWidgets.QLabel('Reason:')
        self.label5.setStyleSheet('color: white;')
        self.textbox5 = QtWidgets.QTextEdit()
        self.subButton = QtWidgets.QPushButton("Submit")
        self.subButton.clicked.connect(show_notification)
        self.subButton.clicked.connect(self.save_data)
        # Create the stylesheet
        self.date_edit.setStyleSheet("background-color: #F3ECB0;")   
        self.date_edit2.setStyleSheet("background-color: #F3ECB0;")   
        self.combobox.setStyleSheet("background-color: #F3ECB0;")   
        self.textbox5.setStyleSheet("background-color: white;")     
        self.subButton.setStyleSheet("background-color: #ADE792;")   
        
        # Create the main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.label3)
        main_layout.addWidget(self.date_edit)
        main_layout.addWidget(self.date_edit2)
        main_layout.addWidget(self.label4)
        main_layout.addWidget(self.combobox)
        main_layout.addWidget(self.label5)
        main_layout.addWidget(self.textbox5)
        main_layout.addWidget(self.subButton)
        
        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.title_label.setFont(font)
        self.date_edit.setFont(font)
        self.date_edit2.setFont(font)
        self.combobox.setFont(font)
        self.label5.setFont(font)
        self.textbox5.setFont(font)
        self.label3.setFont(font)
        self.label4.setFont(font)
        self.subButton.setFont(font)

    def quit_app(self):
        self.app.quit()

    def save_data(self):     
        # Run the program using subprocess
        program_path4 = "/Capstone/hello_flask/hello_flask/payroll.py"
        subprocess.Popen([sys.executable, program_path4])
        # Close the application window
        self.close()

    def goHome(self):
        # Define the path to the program to run
        program_path4 = "/Capstone/hello_flask/hello_flask/frontPage.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path4])
        self.close()

    def clear_data(self):
            # Clear
            self.search_bar.setText('')

def show_notification():
        msg_box = QMessageBox()
        msg_box.setWindowTitle("PTO")
        msg_box.setText("PTO Request Sent. ")
        msg_box.exec_()

if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication([])
    #locale = QLocale(QLocale.English, QLocale.UnitedStates) # Set the locale to English (US)
    #QLocale.setDefault(locale) # Set the default locale
    #Create and show the main window
    main_window = MyApplicationPTO()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())