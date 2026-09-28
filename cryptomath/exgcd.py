
def findExGCD(a: int, b:int):
    """
        Function: caclulates the x and y where ax + by = c
        Returns:
            a = gcd of a and b  
            x0 = x or the coefficent of a
            y0 = y or the coefficent of b
        Mathmatics behind it:
            Uses the extended Euclidean algorithm to find the gcd and the two coefficents
    """

    #set a and b equal to the inputed values 
    #everything else equal to the starting values for extended euclidean
    a = a 
    b = b
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1

    # loop until b = 0
    # set a q equal to the floor of a / b 
    # set a and b equal to b and a mod b at the same time
    # set x0 and x1 to x1 and x0 - q times x1 at the same time
    # set y0 and y1 to y1 and y0 - q times y1 at the same time
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0 , y1 = y1, y0 - q * y1
    # returns gcd, coefficent of a, coefficent of b
    return a, x0 , y0 
#test case 
#print(findExGCD(35, 15))
    