import sqlite3
import random

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price REAL NOT NULL)''')
        self.connection.commit()

    def insert_product(self, product_id, name, price):
        self.cursor.execute('''INSERT INTO products (id, name, price) VALUES (?, ?, ?)''', (product_id, name, price))
        self.connection.commit()

    def update_product(self, product_id, name=None, price=None):
        if name is not None:
            self.cursor.execute('''UPDATE products SET name = ? WHERE id = ?''', (name, product_id))
        if price is not None:
            self.cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (price, product_id))
        self.connection.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.connection.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return self.cursor.fetchone()

    def select_all_products(self):
        self.cursor.execute('''SELECT * FROM products''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# 샘플 데이터 생성 및 삽입
def generate_sample_data(db):
    for i in range(1, 101):
        product_id = i
        name = f"Product_{i}"
        price = round(random.uniform(10.0, 1000.0), 2)
        db.insert_product(product_id, name, price)

# 데이터베이스 객체 생성
db = ElectronicsDatabase()

# 샘플 데이터 삽입
generate_sample_data(db)

# 예제: 제품 ID가 10인 제품 정보 출력
print("Product with ID 10:", db.select_product(10))

# 예제: 모든 제품 정보 출력
print("All products:", db.select_all_products())

# 예제: 제품 ID가 10인 제품의 이름과 가격 수정
db.update_product(10, name="Updated_Product_10", price=999.99)
print("Updated Product with ID 10:", db.select_product(10))

# 예제: 제품 ID가 10인 제품 삭제
db.delete_product(10)
print("Deleted Product with ID 10:", db.select_product(10))

# 데이터베이스 연결 닫기
db.close()
