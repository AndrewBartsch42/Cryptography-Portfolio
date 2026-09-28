def findGCD(a: int, b:int):
    """
        Function: Calculates the GCD of a and b
        Returns:
            a = gcd of b and a
        Mathmatics:
            Uses Euclids algorithm by recursion. 
            take any a and b where a > b 
            then set a = to a mod b 
            repeat until b is zero 
            then a will be the gcd of a and b
    
    """
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

