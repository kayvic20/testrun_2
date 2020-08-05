import pymysql.cursors

    # Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='kbank',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

def create_table():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE Table users (id INT(3) PRIMARY KEY NOT NULL AUTO_INCREMENT, NAME VARCHAR(50), password VARCHAR(30),account_no VARCHAR(12), age INT(3), balance int(20));"
            cursor.execute(sql)

            connection.commit()

        
    finally:
        print("Successfully created Database..!!")
        connection.close()

    return True
def add_user(name, age, password, acct_no):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO users (name, age, password, account_no, balance) VALUES('{name}', {age}, '{password}', '{acct_no}', 0);"
            cursor.execute(sql)

        connection.commit()

            
    finally:
        print("Successfully created new user..!!")
        connection.close()

# add_user('haleemah', 12, '1234', '1299887766')
def fetch_user_details(name):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT name, password,balance From users  WHERE name ='{name}';"
            cursor.execute(sql)

        data =cursor.fetchall()
        return data

        connection.commit()

            
    finally:
        print("Successfully fetched..!!")
        connection.close()

def get_balance(name):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"SELECT  balance from users  WHERE name ='{name}';"
            cursor.execute(sql)

        data =cursor.fetchall()
        return data

            
    finally:
        print("Successfully fetched..!!")
        # connection.close()

def alter_balance(name, balance):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users set balance = {balance}  WHERE name ='{name}'"
            cursor.execute(sql)

            connection.commit()

            
    finally:
        print("Successfully updated users  balance..!!")
        connection.close()

def new_balance(name, balance):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users set balance = {balance}  WHERE name ='{name}'"
            cursor.execute(sql)

            connection.commit()

            
    finally:
        print("Successfully updated users  balance..!!")
        connection.close()

def transfer(new_balance, alter_balance):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"UPDATE users set balance = {balance}  WHERE name ='{name}'"
            cursor.execute(sql)

            connection.commit()

            
    finally:
        print("Successfully transferred amount..!!")
        connection.close()
# alter_balance("kayode", 50000)
# # get_balance('kayode')
