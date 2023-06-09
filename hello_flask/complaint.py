from PySide6.QtCore import QSize, Qt,QEvent
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QPainter,QFont
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QWidget,QGridLayout
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QMessageBox
import subprocess
import sys

class MyApplication_complaints(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = app
        
        # Set the window title and size
        self.setWindowTitle('Complaints')
        self.setMinimumSize(400, 500)

        # menu bar
        menu_bar = self.menuBar()


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
        self.list_box.addItems(['Complaints'])
        self.list_box.setStyleSheet("background-color: #F3ECB0;")

        self.label2 = QtWidgets.QLabel('Write Complaint:')
        self.label2.setStyleSheet("color: white;")
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setStyleSheet("background-color: white;")

        self.sub_button = QtWidgets.QPushButton("Submit")
        self.sub_button.setStyleSheet("background-color: #ADE792;")
        self.sub_button.clicked.connect(show_notification)
        self.sub_button.clicked.connect(self.clear_data)

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
        main_layout.addWidget(self.label2)
        main_layout.addWidget(self.text_area)
        main_layout.addWidget(self.sub_button)
        # Create a central widget and set the main layout
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.label2.setFont(font)
        self.list_box.setFont(font)
        self.label.setFont(font)
        self.search_bar.setFont(font)
        self.text_area.setFont(font)
        self.sub_button.setFont(font)
        
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

    def clear_data(self):
            # Clear
            self.search_bar.setText('')
            self.text_area.setText('')

def show_notification():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Complaint")
    msg_box.setText("Complaint Filed, Thank you for your feedback. ")
    msg_box.exec_()

if __name__ == '__main__':
    import sys
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and show the main window
    main_window = MyApplication_complaints()
    main_window.show()
    
    # Run the event loop
    sys.exit(app.exec_())
