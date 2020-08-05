# def multiply(number):
#     print(number * 3)
# multiply(2)

# name = "adedibu"
    
# def print_name():
#     global name
#     name = "bolu"
#     print(name)

# print_name()
# print(name)

# import requests
# url_to_get= "https://www.jumia.com.ng/"
# # url_to_get= "http://checklight.pythonanywhere.com/streets"
# response_data = ""

# def make_requests(url):
#     global response_data

#     response = requests.get(url)
#     response_data = response
#     print((response))
    
# def check_for_success():
#     if response_data.status_code == 200:
#         print("request is successful")

# def checking_url():
#     try:
#         response_data.json()
#         data = response_data.json()
#         keye = data.keys()
#         print(keye)
#     except:
#         response_data.content
#         print("data is content")


# def json_or_content():

#     try:
#         response_data.json()
#         print("data type is json")
#     except:
#         response_data.content
#         print("Data type is HTML ===== use content")

# make_requests(url_to_get)
# check_for_success()
# checking_url()

# ANAGRAM TESTER
def test_anagram(word, test_word):
    sorted_word = sorted(word.lower())
    sorted_test_word = sorted(test_word.lower())
    if sorted_test_word == sorted_word
        print(test_word, "is an anagram of", word)
            return true
    else:
        print(test_word, "is not an anagram of" word)
            return false
def test_palindrome(word):
    reversed_word = _word[::-1]
    if reversed_word.lower == word.lower():
        print(word, "is a palindrome")

    elif reversed_word.lower() != word.lower
        print(word,"is not an anagram of", word)

# ec = "kay"
# for i in reversed(ec):
#     print(i)
