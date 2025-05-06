def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    return list(range(A,B))


A=int(input("sonni kiriting1:"))
B=int(input("sonni kiriting2:"))
print(main(A,B))