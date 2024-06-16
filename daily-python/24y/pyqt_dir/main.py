# -*- coding: utf-8 -*-

import sys
from ui.demo import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QDir, QThread, pyqtSignal, QTimer
from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.init_connections()
        self.log_thread = None
        self.timer = None

    def init_connections(self):
        # try:
        # except:
        #
        self.pushButton_analyze_files.clicked.connect(self.open_file_dialog)
        self.pushButton_test_start.clicked.connect(self.start_test_thread)
        self.pushButton_test_stop.clicked.connect(self.stop_test_thread)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(QDir.homePath())  # 设置默认打开的文件夹
        file_dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件选择模式为任意文件
        file_dialog.setNameFilters(["Text files (*.txt)", "All files (*.*)"])  # 设置文件过滤器，只显示文本文件
        file_dialog.setOptions(QFileDialog.ReadOnly)  # 设置只读选项，防止用户修改文件内容
        if file_dialog.exec_() == QFileDialog.Accepted:  # 如果用户点击了"打开"按钮
            selected_file = file_dialog.selectedFiles()[0]  # 获取选中的文件路径
            self.add_text(f"{selected_file}")  # 将文件路径显示在文本浏览器中
            self.lineEdit_file.setText(selected_file)

    def start_test_thread(self):
        if self.log_thread is None or not self.log_thread.isRunning():
            self.log_thread = test_thread()
            self.log_thread.sinout.connect(self.add_text)
            self.log_thread.start()
        else:
            self.add_text("已开启测试")

    def start_test_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.add_text)
        self.timer.start(1000)

    def stop_test_thread(self):
        if self.log_thread is not None and self.log_thread.isRunning():
            self.add_text("结束")
            self.log_thread.terminate()
        else:
            self.add_text("未开启测试")

    def stop_test_timer(self):
        self.timer.stop()

    def add_text(self, text):
        cur_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        self.textBrowser.append(f"{cur_time}    {text}")


class test_thread(QThread):
    sinout = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.sinout.emit("开始测试")
            QThread.sleep(1)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    # sys.exit(app.exec_())
