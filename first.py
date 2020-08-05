# print("Hello World")


# print 
# print (i)
# print(" count down from 60 to 0")
# for i in range(0,60):
#     print(abs(i-60))

import time
# import winsound

count = 60

for i in reversed(range(count)):
    time.sleep(0.1)
    # print(abs(i-count))
    print(i, abs(i-60))


