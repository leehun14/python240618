#Demostr.py

strA = "파이썬은 강력해"
strB = "python is powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.upper())

data = "<<<  spam and ham  >>>" 
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))

#정규표현식
import re

result = re. search("[0-9]*th", "35th")
print(result)
print(result.group())

# #선택한 블럭 주석처리 : ctrl + /
# result = re. search("[0-9]*th", "35th")
# print(result)
# print(result.group())

result = re. search("\d{4}", "올해는 2024년")
print(result.group())

result = re. search("\d{5}", "우리 동네는 52333")
print(result.group())

result = re. search("apple", "this is apple")
print(result.group())


import re

def is_valid_email(email):
    # 이메일 주소 정규 표현식 패턴
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # 이메일 주소가 정규 표현식 패턴과 일치하는지 확인
    return re.match(email_regex, email) is not None

# 테스트 예제
emails = [
    "test@example.com",
    "user.name@domain.co",
    "user_name@domain.com",
    "username@domain.c",
    "username@domain..com",
    "@example.com",
    "username@.com",
    "username@domain.corporate"
]

for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
