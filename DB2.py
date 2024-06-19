#데이터베이스
import sqlite3

#연결객체 리턴(메모리 작업)
#영구적으로 파일에 저장
con = sqlite3.connect("sample.db")

#구문을 실행할 커서 객체 리턴
cur = con.cursor()

#테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('derick','010-222');")

#입력 파라미터 처리
name = "홍길동"
phonenumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phonenumber))

#여러번 실행
datalist = (("전우치","010-567"), ("이순신", "010-345"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)


#조회를 실행
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row[0], row[1])

#작업을 정상적으로 완료
con.commit()
con.close()

