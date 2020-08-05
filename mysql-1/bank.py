import random
import pymsqlkay
class Bank():

    logged_user = ""
    balance = 0

    def get_new_acct_no(self):

        new_acct = random.choice(range(1,9999999))
        max_chars = 8
        current_acct_chars = len(str(new_acct))

        deficiency = max_chars - current_acct_chars

        if  deficiency:
            new_acct = ("0"*deficiency) + str(new_acct)
        
        return new_acct

    def register(self):
        
        name = input("Please enter your name - ")
        age = int(input("please enter your age - "))
        password = input("Please enter your password - ")
        
        pymsqlkay.add_user(name, age, password, self.get_new_acct_no())

        print("Successfully created account \n")

    def login(self):

        name_input = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        data = pymsqlkay.fetch_user_details(name_input)
        print(data)

        
        if data:
            print("Username was correct ..!!")
            if password_input == data[0]['password']:
                print("Loggin Successfull..!!")
                
                self.logged_user = name_input
                self.balance = data[0]['balance']
              
            else:
                print("Sorry your password was wrong")

        else:
            print("Username was wrong ..!!")

    def read_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            print("###########################")
            print("Name :", name)
            print("Acct :", acct_no)
            print("- - - - - - - - - - - - - - ")
            print("\nBalance :\n", balance)
            print("###########################\n")


    def read_user_data(self):
        
        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(":;")
            name = splitted_line[0]
            title = splitted_line[1]
            body = splitted_line[2]

            if name == self.logged_user:
                print("###########################")
                print("Name :", name)
                print("Title :", title)
                print("- - - - - - - - - - - - - - ")
                print("\nBody :\n", body)
                print("###########################\n")

    def get_balance(self):

        file_name = "oop/bankapp/bank_data.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            acct_no = splitted_line[2]
            balance = splitted_line[3]

            if name == self.logged_user:

                data = {"name":name, "acct_no":acct_no, "balance":balance}
                print(data)
                return data

    def deposit(self, amount, name = "self"):

    

        target_name = name if name != "self" else self.logged_user
        
        original_balance = pymsqlkay.get_balance(target_name)[0]['balance']
        bal = int(original_balance) + amount

        pymsqlkay.alter_balance(target_name,bal)
    

        print("Deposit Successfull...!")
    
    
    def withdraw(self, amount, name ="self"):

        

        target_name = name if name != "self" else self.logged_user
        
        new_balance = pymsqlkay.get_balance(target_name)[0]['balance']
        bal = int(new_balance) - amount

        pymsqlkay.new_balance(target_name,bal)
    

        print("Withdrawal Successfull...!")

          

    def transfer(self, target, amount):

        
        self.withdraw(amount)

        self.deposit(amount, target)
        pymsqlkay.transfer.transaction_log(name=self.logged_user,amount= amount,destination= target,types=3)
        print("Transfer successful...!")


        

bank = Bank()
# amount = input(int("please enter amount"))
# receiver = input("please enter receiver name")
# bank.transfer(30000, "nick")
# bank.withdraw(30000, "nick")
# bank.deposit(30000, "nick")
# bank.get_balance()
bank.deposit(63000)
# bank.get_balance(nick)

# bank.transfer(3000, "haleemah")+