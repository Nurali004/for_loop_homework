def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    
    Args:
        list1: list – Ismlar ro'yxati
    
    Returns:
        list – Har bir ismdagi faqat birinchi harf katta bo'lgan ro'yxat
    """
    return [name.capitalize() for name in list1]

names = ["alice", "bob", "CHARLIE", "david"]
print(main(names)) 

