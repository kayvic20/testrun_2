import math

def upper(b, a, c):
    numerator = (b**2)-4*a*c
    denominator = 2*a
    st = math.sqrt(numerator)
    m = st/denominator


    return m

def positive(m, b):
    k = ((-1 * b) + m)

    return k

def negative(m, b):
    l = ((-1 * b) - m)

    return l

def solve(a,b,c):
    upper_value = upper(b, a, c)
    print("m value", upper_value)
    x1 = positive(upper_value, b)

    x2 = negative(upper_value, b)

    print(x2, x1)

a = 2
b = -5
c = -3
solve (2 , -5, -3)
negative(1.75, -5)
positive(1.75, -3)
# print(negative(a, b))
# print(positive(a, b))
# print(upper(a, b, c))

