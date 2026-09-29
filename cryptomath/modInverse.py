from exgcd import findExGCD



def findModInv(a:int, m:int):
    """
        Function: mod inverse(x) of a where ax is congruent to 1 mod m 
        Returns:
            x where x satisifies ax = 1 mod m
        Raises:
            exception when g from the extended gcd is equal to 1
        Mathmatics behind it
            Using the extended euclidean algorithm we can find ax + by = c
            findExGCD does this and has documentation in the code on how it works mathmatically
            Mod inverse is just a way to prove that for some a and m 
            ax + my = 1
            ax + my ≡ 1 (mod m)
            remove my as any m times any other number is congruent to 0 mod m 
            ax ≡ 1 mod (m)
            which means that assuming a and m are relatively prime aka the gcd of a and m is 1
            we then take x mod m to find out what the multiplicative inverse of a should be with respect to mod m
            which is where a times x ≡ 1 mod m comes from
    """
    g, x, y = findExGCD(a, m)

    if g != 1:
        raise Exception("No mod inverse")
    else:
        return x % m



#print(findModInv(3, 11))
