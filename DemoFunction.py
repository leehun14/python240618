#DemoFunction.py

#1)함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:", x)


#2) 호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출

#스코핑룰
x = 5
def func2(a):
    return a+x

print(func2(1))