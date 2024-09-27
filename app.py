from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
import sys


class Paint(QMainWindow):
    '''simple paint app'''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("simple paint app")
        self.setGeometry(100, 100, 800, 600)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Paint()
    window.show()
    sys.exit(app.exec_())
