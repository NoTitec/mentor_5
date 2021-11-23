import sys
from PyQt5.QtWidgets import *

class mywindow(QWidget):
    price={'coffee':3000,'latte':4000,'smoothie':5000,'tea':6000}
    sumprice=0
    def __init__(self):
        super().__init__()
        self.lbal1=QLabel('금액:0원')
        self.lbal2=QLabel('수량:0개')
        self.text=QTextEdit()
        self.vi()

    def vi(self):
        btn1=QPushButton('coffee',self)
        btn2=QPushButton('latte',self)
        btn3=QPushButton('smoothie',self)
        btn4=QPushButton('tea',self)
        btn1.clicked.connect(lambda :self.add(btn1.text()))#버튼 text가져옴, 익명함수 필수
        btn2.clicked.connect(lambda :self.add(btn2.text()))
        btn3.clicked.connect(lambda :self.add(btn3.text()))
        btn4.clicked.connect(lambda :self.add(btn4.text()))
        self.text.textChanged.connect(self.count)#매개변수없는 메소드는 ()제거
        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(self.lbal1)
        vbox.addWidget(self.text)
        vbox.addWidget(self.lbal2)
        self.setLayout(vbox)
        self.setWindowTitle('음료수프로그램')
        self.setGeometry(500,200,500,600)
    def add(self,item):
        c_price=mywindow.price.get(item)
        mywindow.sumprice+=c_price
        self.text.append(item)
        self.lbal1.setText('금액'+str(mywindow.sumprice)+'원')

    def count(self):
        text=self.text.toPlainText()
        self.lbal2.setText('수량'+str(len(text.split()))+'개')


#유용한 단축키 alt+shift+화살표
#블록선택후 ctrl+/
app=QApplication(sys.argv)

window=mywindow()
window.show()
sys.exit(app.exec_())
