#DemoLoop.py

fruits = {"apple":100, "kiwi":200}
for item in fruits.items():
    print(item)

print("---range함수----")
print(list(range(10)))
print(list(range(2000,2025)))
print(list(range(1,32)))

print("---리스트 컴프리핸션---")
lst = list(range(1,11))
print([i**2 for i in lst if 1> 5])
tp = ("apple","kiwi","banana")
print(([len(i) for i in tp]))


print("---필터링---")
lst = [10,25,30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

#함수
def getBiggerThan20(i):
    return i > 20

print("---필터링 함수 사용")
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("----람다 함수 사용----")
itemL = filter(lambda x:x>20,lst)
for item in itemL:
    print(item)