#DemoListTuple.py
lst = ["red", "blue", "green"]
print(len(lst))
#슬라이싱
print(lst[0])
print(lst[1])
lst.append("white")
print(lst)
lst.remove("blue")
print(lst)

#슬라이싱
strA = "python is very powerful"
print(strA[0:6])
print(strA[:6])
print(strA[-3:])
print(strA[-8:])

#Set
a ={1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple
tp = ("아이폰", "아이패드", "갤럭시")
print(len(tp))
print(tp[0])
print(tp.index("아이패드"))

#함수정의
def times(a,b):
    return a+b, a*b
#호출
print(times(3,4))

print("id : %s, name : %s" % ("kim", "김유신"))

#형식변환
a = list((1,2,3))
print(a)
b = set(a)
print(b)

#딕셔너리
color = {"apple":"red", "banana": "yellow"}
print(len(color))
color["cherry"] = "red"
print(color)
del color["apple"]
print(color)

for item in color.items():
    print(item)

for k,v in color.items():
    print(k,v)

