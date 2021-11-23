import sys
from PyQt5.QtWidgets import *

class mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.lbal1=QLabel('금액:0원')
        self.lbal2=QLabel('수량:0원')
        self.text=QTextEdit()
        self.vi()

    def vi(self):
        vbox=QVBoxLayout()
        vbox.addWidget(self.lbal1)
        vbox.addWidget(self.lbal2)
        vbox.addWidget(self.text)
        self.setLayout(vbox)

app=QApplication(sys.argv)

window=mywindow()
window.show()
sys.exit(app.exec_())
