from PyQt5 import QtWidgets, QtCore
from UI import Ui_Dialog
from drive import car

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.state = self.time_state = False
        self.speed = 10
        self.count_first_ = self.count_turn_ = 0
        self.drive = car()
        self.timer_first = QtCore.QTimer()
        self.timer_first.timeout.connect(self.count_first)
        self.timer_turn = QtCore.QTimer()
        self.timer_turn.timeout.connect(self.count_turn)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_control()
    def setup_control(self):
        self.ui.Star_Button.clicked.connect(self.clicked_start_button)
        self.ui.Stop_Button.clicked.connect(self.clicked_stop_button)
        self.ui.Time_check.clicked.connect(self.clicked_Time_check)
    def main_run(self):
        if self.state == True:
            print("Car_Start")
            self.drive.start()
            self.drive.move(speed=self.ui.speed_input.value())
            if self.time_state == True:
                print("Use_Timer")
                self.timer_first.start(100)
            else:
                print("Not_Timer")
        else:
            print("Car_Stop")
            self.timer_first.stop()
            self.timer_turn.stop()
            self.count_first_ = self.count_turn_ = 0
            self.ui.label_8.setText(f'直行秒數:0秒')
            self.drive.stop()
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
    def count_first(self):
        self.count_first_ = self.count_first_ + 1
        self.ui.label_8.setText(f'直行秒數:{self.count_first_ / 10}秒')
        if self.count_first_ >= self.ui.time_input01.value()*10:
            self.drive.move_RL(speed=self.ui.speed_input.value())
            self.timer_turn.start(100)
            self.timer_first.stop()
            self.count_first_ = 0
    def count_turn(self):
        self.count_turn_ = self.count_turn_ + 1
        self.ui.label_8.setText(f'轉彎秒數:{self.count_turn_ / 10}秒')
        if self.count_turn_ >= self.ui.time_input02.value()*10:
            self.drive.move(speed=self.ui.speed_input.value())
            self.timer_turn.stop()
            self.count_turn_ = 0

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())