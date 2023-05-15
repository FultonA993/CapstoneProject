import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QPoint

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Forsyth Family Medical Practice")
        # Load the pixmap
        pixmap = QPixmap('\Capstone\hello_flask\CapstoneLogoPNG.png')
        self.pixmap = pixmap
        
        # Set the size of the main window to match the pixmap size
        self.setFixedSize(pixmap.size())

        # Override the paintEvent method to draw the pixmap onto the main window
        self.paintEvent = self.draw_pixmap

        # Set the stylesheet of the main window to use the pixmap as the background
        self.setStyleSheet("background-image: url(\Capstone\hello_flask\CapstoneLogoPNG.png);")

    def draw_pixmap(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(0, 0), self.pixmap)

    def mousePressEvent(self, event):
        if event.button() == 1 and event.pos().x() < self.pixmap.width() and event.pos().y() < self.pixmap.height():
            # Launch the new Python file
            os.system("python main.py")

if __name__ == '__main__':
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec_()
