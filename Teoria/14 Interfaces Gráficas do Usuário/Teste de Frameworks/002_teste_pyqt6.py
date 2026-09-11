import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt6.QtCore import QSize, Qt


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(280, 120))
        self.setWindowTitle('Olá, mundo! Exemplo PyQt6')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout()
        centralWidget.setLayout(gridLayout)

        title = QLabel('Olá mundo para PyQt')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        gridLayout.addWidget(title, 0, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec())
