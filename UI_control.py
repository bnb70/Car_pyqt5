from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_Dialog
#from drive import car

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.state = self.time_state = False
        self.time01 = self.time02 = self.time03 = self.time04 = self.time05 = 0
        self.speed = 10
#        self.drive = car()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_control()
    def setup_control(self):
        self.ui.Star_Button.clicked.connect(self.clicked_start_button)
        self.ui.Stop_Button.clicked.connect(self.clicked_stop_button)
        self.ui.Confirm_Button.clicked.connect(self.clicked_confirm_button)
        self.ui.Time_check.clicked.connect(self.clicked_Time_check)
    def main_run(self):
        if self.state == True:
            print("Car_Start")
            if self.time_state == True:
                print("Use_Timer")
            else:
                print("Not_Timer")
#                self.drive.start()
#                self.drive.move(speed=self.speed)
        else:
            print("Car_Stop")
#            self.drive.stop()
    def clicked_Time_check(self):
        if self.time_state != True:
            self.time_state = True
            self.ui.label_7.setText("計時器:開啟")
        else:
            self.time_state = False
            self.ui.label_7.setText("計時器:關閉")
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
        self.speed = self.ui.speed_input.value()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())