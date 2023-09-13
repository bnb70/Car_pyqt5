from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.state = False
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_control()
    def setup_control(self):
        self.ui.Star_Button.clicked.connect(self.clicked_start_button)
        self.ui.Stop_Button.clicked.connect(self.clicked_stop_button)
        self.ui.Confirm_Button.clicked.connect(self.clicked_confirm_button)
    def main_run(self):
        if self.state == True:
            print("True")
        else:
            print("False")
    def clicked_start_button(self):
        self.state = True
        self.main_run()
    def clicked_stop_button(self):
        self.state = False
        self.main_run()
    def clicked_confirm_button(self):
        self.time01 = self.ui.time_input01.value()
        self.time02 = self.ui.time_input02.value()
        self.time03 = self.ui.time_input03.value()
        self.time04 = self.ui.time_input04.value()
        self.time05 = self.ui.time_input05.value()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())