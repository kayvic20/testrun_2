# def factorial(x):

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#     # return(f"{x} * {factorial(x-1})")

# num = 3
# print ("The factorial of", num, "is", factorial(num))
# # factorial(3)


_list = [3,4,8,22,34,54,60]

def moving_difference(_list, differences = []):
    if len(_list) < 2:
        return differences
    else:
        differences.append(_list[1] -_list[0])

        return moving_difference(_list[1:], differences)

print(moving_difference(_list))







