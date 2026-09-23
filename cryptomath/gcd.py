def findGCD(a: int, b:int):
    #force positive numbers
    a = abs(a)
    b = abs(b)

    #flip the numbers if b is greater than a
    if a < b:
        temp = a
        a = b
        b = temp
    # use recursion to loop until remainder 0 
    # then return the value of a which is the gcd of the inital two numbers
    if b != 0:
        a = a%b
        return findGCD(a, b)
    else:
        return a

