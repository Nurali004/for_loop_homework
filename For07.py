def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    yigindi=0
    for i in range(N+1):
        if i%2!=0:
            yigindi+=i

    

    return yigindi

N=int(input("sonni kiriting:"))

print(main(N))