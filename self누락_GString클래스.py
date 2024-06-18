#전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(str)

#인스턴스 생성
d = DemoString()
d.set("First Message")
d.print()
