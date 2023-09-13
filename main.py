import sys
from PyQt5 import QtWidgets
from UI_control import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("控制")
    window.show()
    sys.exit(app.exec_())