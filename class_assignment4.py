# names = "john"
# names_rep = "sade"

# for j in names:
#     for i in names_rep:
#         print(j, i)

# read_or_write = input("What would you like to do \n R for read W for write: ")
# if read_or_write.lower() == "w":
#     name = input("Please enter your Username: ")
#     password = input("Please enter your password: ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "w")
#     user_detail_file.write(f"{name},{password}")

#     database = open(f"data/{name}_database.txt", "a")

#     data = input("please enter your note: ")
#     database.write(f"{data}\n")
# elif read_or_write.lower() == "r":
#     name = input("Please enter your unsername: ")
#     password_input = input("Please enter your password: ")

#     user_detail_file = open("data/{}_detail.csv".format(name), "r")
#     username, password = user_detail_file.readline().split(",")

#     username_is_correct = username == name
#     password_is_correct = password == password_input

#     if username_is_correct and password_is_correct:
#         database = open(f"data/{name}_database.txt", "r")
#         data = database.read()
#         print(data)
# user_detail_file.close()


# print("password creator")

# name_1 = "kayode"
# name_2 = "card"
# # for i in name_1:
# #     for j in name_2:
# password = name_1 , name_2
# print(password)

# import itertools
# name1 = "k","a","y","g","i","r","l"
# name2 = "t","o","l","a", "b","o","y"
# password = { 'name1' : ['k','a','y','g','i','r','l'],'name2' : ['t','o','l','a', 'b','o','y'] }
# for i in name1:
#     for j in name2:

#          for combo in itertools.product(*[password[k] for k in sorted(password.keys())]):

#             print(''.join(combo), ''.join(combo), ''.join(combo))

# import string
# import random

# first_letter = input ("enter your first name: ")
# second_letter = input ("enter your second name: ")
# pass_lenght =int(input ("how many chars of pass do you want(1-10) : "))

# full_word = first_letter + second_letter
# password = ""
# print(full_word)
# for i in range(pass_lenght):
#     randon_choice = random.randint(0,len(full_word)-1)
#     password = password + full_word[randon_choice]

# # print(full_word,full_word[randon_choice])
# print(f"Here's your new {pass_lenght}char key : ", password)

# first_letter = input ("enter your first name: ")
# second_letter = input ("enter your second name: ")
# pass_lenght =int(input ("how many chars of pass do you want(1-10) : "))

# full_word = first_letter + second_letter
# password = ""
# print(full_word)
# for i in range(pass_lenght):
#     while True:

#         randon_choice = random.randint(0,len(full_word)-1)
#         if full_word[randon_choice] not in password:
#              break
#     password = password + full_word[randon_choice]

# # print(full_word,full_word[randon_choice])
# print(f"Here's your new {pass_lenght}char key : ", password)

# meal1 = input("enter first food: ")
# meal2 = input ("enter second food: ")
# meal3 = input ("enter third food: ")
# menu = meal1 + meal2 + meal3
# mix = input ("ho many food you need:")
# if meal1 not in menu:
#     print(meal2,meal3)
    # else:
# print(meal1,meal2)

# sccattered_list = [1,4,6,3,7,5,2]


# for i in range(sccattered_list)):

#     if sccattered_list

user1 = input ("enter a word:")

mydata = {"key1":user1}
while True:
    print(mydata)

    key1 = input("enter your key: ")
    value = input("enter your value: ")
    mydata[key1] = value

print(mydata["key1"])

