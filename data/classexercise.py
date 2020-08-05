# print("notepad")

database= {}
firstname = input("please enter your firstname: ")
surname = input("please enter your surname: ")
username = input("please enter your username: ")
password = input("please enter your password: ")
confirm_password = input("please re-enter your password: ")

# database = {
#     "firstname":firstname,
#     "surname":surname,
#     "username":username,
#     "password":password,
# }

file = open("notepad/db.csv", "a")

file.write(f"{firstname},{surname},{username},{password}\n")
file.close()

# sing in
# database= {}
# firstname = input("please enter your firstname: ")
# surname = input("please enter your surname: ")
# username = input("please enter your username: ")
# password = input("please enter your password: ")
# confirm_password = input("please re-enter your password: ")

# # database = {
# #     "firstname":firstname,
# #     "surname":surname,
# #     "username":username,
# #     "password":password,
# # }

# file = open("notepad/db.csv", "a")

# file.write(f"{firstname},{surname},{username},{password}\n")
# file.close()