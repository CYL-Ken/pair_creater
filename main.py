from PyQt5 import QtWidgets, QtGui, QtCore
from main_ui import Ui_MainWindow
import json
# from subwindow import SubWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        
        self.sub_window = SubWindow()
        
        self.channels = 96

        self.device_buttom = dict()
        self.target_buttom = dict()

        self.temp_pair_table = [0, 0]

        self.ui.setupUi(self)
        print(self.sub_window.info_title.text())
        self.setup_control()

        self.get_device_and_info()

        self.ui.comboBox.currentTextChanged.connect(self.update_device)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_target)

        

    def setup_control(self):
        # TODO
        pass
        self.create_port_button(object="device")
        self.create_port_button(object="target")

    
    def update_device(self):
        self.device_mac = self.ui.comboBox.currentText()
        self.device_channel = self.data[self.device_mac]["channels"]
        self.device_commands = self.data[self.device_mac]["cmd"]
        pass

    def update_target(self):
        self.target_mac = self.ui.comboBox_2.currentText()
        pass
        


    def get_device_and_info(self):

        self.device_list = []
        with open("virtual.json") as f:
            self.data = json.load(f)
            self.device_list = self.data.keys()

        self.ui.comboBox.addItems(self.device_list)
        self.ui.comboBox_2.addItems(self.device_list)

        
        

    def create_port_button(self, object="device"):
        if object == "device":
            # Input
            Vbox_input = QtWidgets.QVBoxLayout()
            groupBox_input = QtWidgets.QGroupBox("Input Channels")
            font = QtGui.QFont()
            font.setPointSize(8)
            groupBox_input.setFont(font)
            groupBox_input.setAlignment(QtCore.Qt.AlignCenter)

            # Output
            Vbox_output = QtWidgets.QVBoxLayout()
            groupBox_output = QtWidgets.QGroupBox("Output Channels")
            groupBox_output.setFont(font)
            groupBox_output.setAlignment(QtCore.Qt.AlignCenter)

            for i in range(self.channels):
                self.device_buttom[i] = QtWidgets.QPushButton()
                self.device_buttom[i].setObjectName(f"device_endpoint_{i+1}")
                font = QtGui.QFont()
                font.setFamily("Consolas")
                font.setPointSize(8)
                self.device_buttom[i].setFont(font)
                self.device_buttom[i].setText(f"{i+1}")
                self.device_buttom[i].clicked.connect(self.click_device)
                if i%2==0:
                    Vbox_output.addWidget(self.device_buttom[i])
                else:
                    Vbox_input.addWidget(self.device_buttom[i])

            groupBox_input.setLayout(Vbox_input)
            self.ui.scroll_input.setWidget(groupBox_input)
            
            groupBox_output.setLayout(Vbox_output)
            self.ui.scroll_output.setWidget(groupBox_output)
            self.ui.v_input.addWidget(self.ui.scroll_input)
            self.ui.v_output.addWidget(self.ui.scroll_output)

        elif object == "target":
            # Input
            Vbox_input = QtWidgets.QVBoxLayout()
            groupBox_input = QtWidgets.QGroupBox("Input Channels")
            font = QtGui.QFont()
            font.setPointSize(8)
            groupBox_input.setFont(font)
            groupBox_input.setAlignment(QtCore.Qt.AlignCenter)

            # Output
            Vbox_output = QtWidgets.QVBoxLayout()
            groupBox_output = QtWidgets.QGroupBox("Output Channels")
            groupBox_output.setFont(font)
            groupBox_output.setAlignment(QtCore.Qt.AlignCenter)

            for i in range(self.channels):
                self.target_buttom[i] = QtWidgets.QPushButton()
                self.target_buttom[i].setObjectName(f"device_endpoint_{i+1}")
                font = QtGui.QFont()
                font.setFamily("Consolas")
                font.setPointSize(8)
                self.target_buttom[i].setFont(font)
                self.target_buttom[i].setText(f"{i+1}")
                self.target_buttom[i].clicked.connect(self.click_target)
                if i%2==0:
                    Vbox_output.addWidget(self.target_buttom[i])
                else:
                    Vbox_input.addWidget(self.target_buttom[i])

            groupBox_input.setLayout(Vbox_input)
            self.ui.scroll_input_target.setWidget(groupBox_input)
            
            groupBox_output.setLayout(Vbox_output)
            self.ui.scroll_output_target.setWidget(groupBox_output)
            self.ui.v_input_target.addWidget(self.ui.scroll_input_target)
            self.ui.v_output_target.addWidget(self.ui.scroll_output_target)


    def click_device(self):
        sender = self.sender()
        print(sender.text())
        self.temp_pair_table[0] = sender.text()
        for i in self.device_buttom.keys():
            if self.device_buttom[i].text() != sender.text():
                self.device_buttom[i].setEnabled(False)

    def click_target(self):
        sender = self.sender()
        print(sender.text())
        self.temp_pair_table[1] = sender.text()
        for i in self.target_buttom.keys():
            if self.target_buttom[i].text() != sender.text():
                self.target_buttom[i].setEnabled(False)
        self.show_sub_window(self.temp_pair_table)

    
    def show_sub_window(self, temp_pair_table):
        
        self.sub_window.info_title.setText(f"配對裝置: endpoint {temp_pair_table[0]}, 配對目標: endpoint {temp_pair_table[1]}")
        self.sub_window.create_config_item(config=["duration", "timeout", "delay"])
        self.sub_window.show()


    def start_pair(self, device, target):
        pass


class SubWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.resize(640, 480)

        # Title
        self.info_title = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.info_title.setFont(font)
        self.info_title.setGeometry(QtCore.QRect(20, 50, 620, 40))
        self.info_title.setAlignment(QtCore.Qt.AlignCenter)
        self.info_title.setObjectName("info_title")

        # Button
        self.submit = QtWidgets.QPushButton(self)
        self.submit.setText("確認")
        self.submit.setStyleSheet("font-size:20px")
        self.submit.setGeometry(QtCore.QRect(240, 380, 140, 40))
        self.submit.clicked.connect(self.submit_setting)

        # Detail
        self.level_edit = QtWidgets.QTextEdit(self)
        self.level_edit.setGeometry(QtCore.QRect(260, 120, 280, 40))
        self.level_edit.setObjectName("level_edit")
        
        self.duration_edit = QtWidgets.QTextEdit(self)
        self.duration_edit.setGeometry(QtCore.QRect(260, 180, 280, 40))
        self.duration_edit.setObjectName("duration_edit")
        
        self.timeout_edit = QtWidgets.QTextEdit(self)
        self.timeout_edit.setGeometry(QtCore.QRect(260, 240, 280, 40))
        self.timeout_edit.setObjectName("timeout_edit")
        
        self.delay_edit = QtWidgets.QTextEdit(self)
        self.delay_edit.setGeometry(QtCore.QRect(260, 300, 280, 40))
        self.delay_edit.setObjectName("delay_edit")
        
        self.level_edit.setVisible(False)
        self.duration_edit.setVisible(False)
        self.timeout_edit.setVisible(False)
        self.delay_edit.setVisible(False)

    def create_config_item(self, config=["timeout", "delay"]):
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)

        config_table = {
            "level": ["level", self.level_edit, "255"],
            "duration": ["duration", self.duration_edit, "50"],
            "timeout": ["timeout (ms)", self.timeout_edit, "1000"],
            "delay": ["delay (ms)", self.delay_edit, "0"]
        } 

        for i in range(len(config)):
            
            # Text
            label = QtWidgets.QLabel(self)
            label.setFont(font)
            label.setText(config_table[config[i]][0])
            label.setGeometry(QtCore.QRect(120, 120 + i*60, 140, 40))

            # Edit
            edit = config_table[config[i]][1]
            edit.setPlaceholderText(config_table[config[i]][2])
            edit.setGeometry(QtCore.QRect(260, 125 + i*60, 280, 35))
            edit.setFont(font)
            edit.setVisible(True)

    def submit_setting(self):

        self.close()

    def closeEvent(self, event):
        # do stuff
        window.temp_pair_table = [0, 0]
        for i in window.device_buttom.keys():
            window.device_buttom[i].setEnabled(True)
        for i in window.target_buttom.keys():
            window.target_buttom[i].setEnabled(True)
        event.accept()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
