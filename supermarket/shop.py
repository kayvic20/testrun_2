# file = open("supermarket/users.csv", "r")
# item_file = open("supermarket/items.csv", "r")
# user_name = input("please enter your username:")
# password = input("kindly input your password:")
# for line in file:
#     if line[0] == user_name and line[1] == password:
#         print("login successful")

# customer log in details
# username = input("Please enter your username : ")
# password = input("Please enter your password : ")

# confirm_password = input("Please re-enter your password : ")
# if password == confirm_password:
#     print("successful")
import datetime

logged_in_user = False

while True:

    task = input("\nWelcome to kayode supermarket  \nPlease enter : \n# su for signup\n# si for signin\n# gd to add goods\n# pr to print receipt\n# stats to get stats\n ch to check goods\n> : ")


    if task == "su":
        ############# Sign UP  to supermarket ##############

        firstname = input("Please enter your name : ")
        surname = input("Please enter your surname : ")
        username = input("Please enter your username : ")

        password = input("Please enter your password : ")
        confirm_password = input("Please re-enter your password : ")

        while password != confirm_password:

            print("Sorry you passwords dont match !!\n")
            password = input("Please enter your password : ")
            confirm_password = input("Please re-enter your password : ")


        file = open("supermarket/db.csv", "a")

        file.write(f"{firstname},{surname},{username},{password}\n")
        file.close()

    elif task == "si":
        ############ Sign in ###############

        input_username = input("Please enter your username : ")
        input_password = input("Please enter your password : ")

        file = open("supermarket/db.csv", "r")

        for line in file.readlines():
            saved_username, saved_password = line.replace("\n","").split(",")[2:]
            
            if saved_username.lower() == input_username.lower():
                if input_password == saved_password:
                    print(f"Welcome {saved_username}")
                    logged_in_user = saved_username ## ASSIGN THE USERNAME AS LOGGED IN USER GLOBALLY
                    break
        else:
            print("Sorry you may not have an account, Please sign up.")


    elif task == "pr":
    
      
        goods_item = {} 
        goods_history = [] 
        item_name = input("Item name:\n")   
        quantity = input("Quantity purchased:\n")   
        cost = input("Price per item:\n")
        goods_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
        goods_history.append(goods_item)
        user_input = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
        if user_input == 'q':
            # stop = True
    
            grand_total = 0  

            for index, item in enumerate(goods_history):
                item_total = item['number'] * item['price']
                grand_total = grand_total + item_total
    # print('%d %s  $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
                print(item['number'], item['name'], item['price'], item_total)
                item_total = 0

        print('Grand total: $%.2f' % grand_total)

    elif task == "gd":

        if logged_in_user:
            ############# add goods ##############

            commodity = input("Please enter a commodity : ")
            food = input("Please enter your food : ")
            fruits = input("Please enter your fruits : ")
            chocolate = input("Please enter your type of chocolate : ")
            soap = input("Please enter your soap : ")
            file = open("supermarket/goods.csv", "a")

            file.write(f"{commodity},{food},{fruits},{chocolate}{soap}\n")
            file.close()
        else:

            print("Sorry you need to be logged in first.!!")

 elif task == "ch":

        if logged_in_user:

            ############# check goods ##############
            goods_found = []

            file = open("supermarket/goods.csv", "r")

            for line in file.readlines():
                username, title, body, date = line.split(",")
                
                if logged_in_user == username:

                    goods_found.append({
                                            "title":title,
                                            "body":body
                                        })
            print()
            for index, good in enumerate(goods_found):
                print(index+1, good["title"])
            print()
            selected_option = int(input("Above are your notes pick one \n> "))

            print("\n###########################")
            print(goods_found[selected_option-1]["title"].upper())
            print("###########################\n")
            print(goods_found[selected_option-1]["body"])
            print("\n###########################")
            print("###########################\n")

        else:

            print("Sorry you need to be logged in first.!!")





# codio goods list python
# grocery_item = {} 
# grocery_history = [] 

# stop = False 

# while not stop:
#     item_name = input("Item name:\n")   
#     quantity = input("Quantity purchased:\n")   
#     cost = input("Price per item:\n")
#     grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
#     grocery_history.append(grocery_item)
#     user_input = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
#     if user_input == 'q':
#       stop = True
    
# grand_total = 0  

# for index, item in enumerate(grocery_history):
#     item_total = item['number'] * item['price']
#     grand_total = grand_total + item_total
#     # print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
#     print(item['number'], item['name'], item['price'], item_total)
#     item_total = 0

# print('Grand total: $%.2f' % grand_total)
