def tri_recursion(k):
    print(k)
    if(k > 0):
        x = tri_recursion (k - 3)
        result = k + x
        print( x, result)
    else:
        result = 0
        print(result)
    return result

print("\n\nRecursion example results")
tri_recursion(17)




