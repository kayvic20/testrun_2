import pymysql.cursors

    # Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='application_data',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

def create_table():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "CREATE Table application_ data(id INT(5) PRIMARY KEY NOT NULL AUTO_INCREMENT, customerID VARCHAR(20),loanId VARCHAR(20),appilcation Date DATE ,LoanNumber VARCHAR(20),LoanAmount INT(10),InterestRate DECIMAL (30,2),TermDays INT(10),repaymentDueDate DATE ,repaymentPaidDate DATE )";
            cursor.execute(sql)

            connection.commit()

        
    finally:
        print("Successfully created Database..!!")
        connection.close()

    # return

create_table()