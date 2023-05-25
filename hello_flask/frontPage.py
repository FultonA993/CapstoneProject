from PyQt5 import QtWidgets
from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PySide6 import QtWidgets, QtCore, QtGui
import subprocess
import sys

class MyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Welcome to Forsyth Family Medical Practice')
        self.showFullScreen()

        # menu bar
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet('color: #6ECCAF;')
        file_menu = menu_bar.addMenu("&File") 
        home_action = file_menu.addAction("Home")
        #home_action.triggered.connect(self.goHome)   
        clear_action = file_menu.addAction("Clear")
        #clear_action.triggered.connect(self.clear_data)
        quit_action = file_menu.addAction("Log Out")
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

        button1 = QtWidgets.QPushButton("Open Directory", self)
        # Set the background color of the button to blue
        button1.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button1.setMinimumHeight(80)
        button1.setMaximumWidth(500)
        button1.clicked.connect(self.open_program1)
        #change the click action
        button7 = QtWidgets.QPushButton("View/File Complaints", self)
        button7.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button7.setMinimumHeight(80)
        button7.setMaximumWidth(500)
        button7.clicked.connect(self.open_program7)
        #change the click action
        button2 = QtWidgets.QPushButton("View Payroll", self)
        button2.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button2.setMinimumHeight(80)
        button2.setMaximumWidth(500)
        button2.clicked.connect(self.open_program2)
        #change the click action
        button3 = QtWidgets.QPushButton("Information", self)
        button3.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button3.setMinimumHeight(80)
        button3.setMaximumWidth(500)
        button3.clicked.connect(self.open_program3)
        #change the click action
        button4 = QtWidgets.QPushButton("More...", self)
        button4.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button4.setMinimumHeight(80)
        button4.setMaximumWidth(500)
        button4.clicked.connect(self.open_program4)

        button5 = QtWidgets.QPushButton("Blacklist", self)
        button5.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button5.setMinimumHeight(80)
        button5.setMaximumWidth(500)
        button5.clicked.connect(self.open_program5)
        
        button6 = QtWidgets.QPushButton("Licenses", self)
        button6.setStyleSheet("font-size: 36px; background-color: #ADE792;")
        button6.setMinimumHeight(80)
        button6.setMaximumWidth(500)
        button6.clicked.connect(self.open_program6)

        # Add the buttons to the layout
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button4)
        layout.setAlignment(Qt.AlignCenter)

        # Set the layout as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Set the background color
        self.setStyleSheet('background-color: #344D67')
        
    def open_program1(self):
        # Define the path to the program to run
        program_path = "FultonA993/CapstoneProject/hello_flask/directory.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path])

        
    def open_program2(self):
        # Define the path to the program to run
        program_path2 = "FultonA993/CapstoneProject/hello_flask/payroll.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path2])
        

    def open_program3(self):
        # Define the path to the program to run
        program_path3 = "FultonA993/CapstoneProject/hello_flask/infoPage.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path3])
        

    def open_program4(self):
        # Define the path to the program to run
        program_path4 = "FultonA993/CapstoneProject/hello_flask/morePage.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path4])
        

    def open_program5(self):
        # Define the path to the program to run
        program_path5 = "FultonA993/CapstoneProject/hello_flask/testBlacklist.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path5])
        

    def open_program6(self):
        # Define the path to the program to run
        program_path6 = "FultonA993/CapstoneProject/hello_flask/testLicenses.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path6])
        

    def open_program7(self):
        # Define the path to the program to run
        program_path7 = "FultonA993/CapstoneProject/hello_flask/complaint.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path7])
        

    def quit_app(self):
        # Define the path to the program to run
        program_path7 = "FultonA993/CapstoneProject/hello_flask/main.py"
        # Run the program using subprocess
        subprocess.Popen([sys.executable, program_path7])
        self.app.quit()

    def search_item(self, text):
        items = [self.list_box.item(i) for i in range(self.list_box.count())]
        matches = [item for item in items if text.lower() in item.text().lower()]
        if matches:
            self.list_box.setCurrentItem(matches[0])
        else:
            self.list_box.setCurrentItem(None)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApplication()
    window.show()
    app.exec()
