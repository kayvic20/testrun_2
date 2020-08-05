# def kay(name):
#     print(name)

# kay(ade)

# def mult(*a):
#     for i in a:
#         print(2 * i, i)

# mult(2,3,4,5,6,7)

# def jack(*k):
 
#     for i in k:
#         print(i.lower())
        
# jack('MY NAME IS KAY')

# def students(**data):
#     print(data)

# students(ade=23, bolu=12,shade=27, shun=50)

# def market(**mark):
#     for key in mark:
#         print(key,",", mark[key])
#     prices = sum(mark.values())
#     print("total :", prices)

# market( apple=200, mango=250,grape=400)

# def ono(r= "home"):
#     print(r)

# ono()
# def count(*sort):
#     for alphabet in sort:
#         for item in alphabet:
#             print(item)

# count("this is a ball game")


def sort_values(*scattered_list,should_be_ascending = True):
    scattered_list = list(scattered_list)
    for i in range(len(scattered_list)):
        for i in range(len(scattered_list)-1):
            if scattered_list[i] > scattered_list[i+1]:
                scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]
    
    if should_be_ascending:
        print(scattered_list)
    else:
        print(scattered_list[::1])

sort_values(2,3,4,6,2,4,9,67,2,4,12,44, should_be_ascending=False)



