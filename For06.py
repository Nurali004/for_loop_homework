def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    return sum(range(A, B+1))

A=int(input("sonni kiriting1:"))
B=int(input("sonni kiriting2:"))
print(main(A,B))   