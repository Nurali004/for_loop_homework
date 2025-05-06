def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    result=" "
    for i in range(n):
        result+=f"{i}"

    return result.strip()

print(main(6))