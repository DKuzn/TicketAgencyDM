import sys
from PyQt5 import QtWidgets, uic


class SolveApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SolveApp, self).__init__()
        uic.loadUi('../resources/mainwindow.ui', self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SolveApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
