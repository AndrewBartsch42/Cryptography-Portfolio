def findExGCD(a: int, b:int):
    s = 0
    r = b
    old_s = 1
    old_r = a

    while r != 0:
        quotient = old_r/r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)

    if b != 0:
        bezout_t = (old_r - old_s * a)/b
    else:
        bezout_t = 0

    output = {"coefficent a": old_s, "coefficent b":bezout_t, "gcd":old_r}
    return output


print(findExGCD(5,11))
    