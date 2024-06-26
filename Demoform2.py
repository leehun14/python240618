#DemoForm.ui(화면) + DemoForm.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인 파일 로딩
form_class = uic.loadUiType("Demoform.ui")[0]

#폼클래스 정의
class DemoForm(QMainWindow, form_class):
    #초기화 메소드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메소드
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def firstClick(self):
        self.label.setText("두번째 버튼")
    def firstClick(self):
        self.label.setText("세번째 버튼")    

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
