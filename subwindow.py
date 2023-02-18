from PyQt5 import QtCore, QtGui, QtWidgets
# from main import window

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
        self.info_title.setObjectName("info_title")

        # Button
        self.submit = QtWidgets.QPushButton(self)
        self.submit.setText("確認")
        self.submit.setStyleSheet("font-size:20px")

        # Detail
        self.level_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.level_edit.setGeometry(QtCore.QRect(260, 120, 280, 40))
        self.level_edit.setObjectName("level_edit")
        
        self.duration_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.duration_edit.setGeometry(QtCore.QRect(260, 180, 280, 40))
        self.duration_edit.setObjectName("duration_edit")
        
        self.timeout_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.timeout_edit.setGeometry(QtCore.QRect(260, 240, 280, 40))
        self.timeout_edit.setObjectName("timeout_edit")
        
        self.delay_edit = QtWidgets.QTextEdit(self.centralwidget)
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

        editbox_table = {
            "level" : [self.level_edit, "255"],
            "duration" : [self.duration_edit, "50"],
            "timeout" : [self.timeout_edit, "1000"],
            "delay" : [self.delay_edit, "0"]
        } 

        for i in range(len(config)):
            
            # Text
            label = QtWidgets.QLabel(self.centralwidget)
            label.setFont(font)
            label.setText(config[i])
            label.setGeometry(QtCore.QRect(120, 120 + i*60, 140, 40))

            # Edit
            edit = editbox_table[config[i]][0]
            edit.setPlaceholderText(editbox_table[config[i]][1])
            edit.setVisible(True)

    def closeEvent(self, event):
        # do stuff
        window.temp_pair_table = [0, 0]
        for i in window.device_buttom.keys():
            window.device_buttom[i].setEnabled(True)
        for i in window.target_buttom.keys():
            window.target_buttom[i].setEnabled(True)
        event.accept()