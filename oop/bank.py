# print("welcome to Kay's Bank ")
# print("            ________ ")
# print("     |  /  |        )")
# print("     | /   | KAY    )")
# print("           |--------) ")
# print("     |\    | BANK   )")
# print("     |  \  |________)")



# import sys
class Customer:
    
    
    def register(self):
        name = input("please enter your name : ")
        password = input("please input your password : ")

        customer_details = "oop/bank_details.csv"
        file = open(customer_details, "a")
        file.write(f"{name},{password}\n")
        print("Successfully created account \n")


    def login(self):
        name = input("Please enter your name - ")
        password_input = input("Please enter your password - ")

        file_name = "oop/bank_details.csv"
        file = open(file_name, "r")
        data = file.read()

        for line in data.splitlines():
            splitted_line = line.split(",")
            name = splitted_line[0]
            password = splitted_line[1]

            if name == name:
                print("Username was correct ..!!")
                if password_input == password:
                    print("Loggin Successfull..!!")
                    
                    self.logged_user = name
                    break
                else:
                    print("Sorry your password was wrong")

        else :
            print("Username was wrong ..!!")

    # def __init__ (self,name,balance = 0):
    #      if name == self.logged_user:
    
    #         self.name = name
    #         self.balance = balance
    

    def begin(self):

        is_registered = input("Do you have an account (y/n): ")

        if is_registered == "y":

            self.login()

        elif is_registered == "n":

            self.register()
            print("Please Sign In  to continue..\n")
            self.login()

        if option =="d":
            amt = float(input("enter the amount to deposit "))
            self.deposit(amt)

        elif option =="w":
            
            amt = float(input("enter amount to withdraw "))
            self.withdraw(amt)
        elif option =="e":
            print("Thanks for banking with us")
            sys.exit()
        else:
             print("choose a valid option")


Customer().begin()

    
 

# Customer().register()







