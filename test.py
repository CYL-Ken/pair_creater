from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonPreview(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 創建按鈕和預覽區域
        self.button = QtWidgets.QPushButton('Preview Button', self)
        self.preview_area = QtWidgets.QLabel(self)

        # 設置預覽區域的大小和樣式
        self.preview_area.setFixedSize(200, 100)
        self.preview_area.setAlignment(QtCore.Qt.AlignCenter)
        self.preview_area.setStyleSheet('background-color: white; border: 1px solid black;')

        # 設置按鈕的屬性
        self.button.setToolTip('Click \nto \npreview the button')
        self.button.clicked.connect(self.preview_button)

        # 創建水平布局，將按鈕和預覽區域添加到布局中
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.preview_area)
        self.setLayout(layout)

    def preview_button(self):
        # 創建一個臨時的按鈕，複製原來按鈕的外觀和行為
        temp_button = QtWidgets.QPushButton(self.button.text(), self)
        temp_button.setFlat(self.button.isFlat())
        temp_button.setAutoDefault(self.button.autoDefault())
        temp_button.setDefault(self.button.isDefault())
        temp_button.setEnabled(self.button.isEnabled())
        temp_button.setCheckable(self.button.isCheckable())
        temp_button.setChecked(self.button.isChecked())
        temp_button.setToolTip(self.button.toolTip())
        temp_button.setShortcut(self.button.shortcut())

        # 設置臨時按鈕的大小和位置
        temp_button.setGeometry(0, 0, self.preview_area.width(), self.preview_area.height())

        # 將臨時按鈕渲染到預覽區域中
        pixmap = QtGui.QPixmap(self.preview_area.size())
        temp_button.render(pixmap)
        self.preview_area.setPixmap(pixmap)

        # 刪除臨時按鈕
        temp_button.deleteLater()

import sys
app = QtWidgets.QApplication(sys.argv)
window = ButtonPreview()
window.show()
sys.exit(app.exec_())