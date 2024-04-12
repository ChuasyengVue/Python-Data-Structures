def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

# Turning int into str to manipulate
    num1 = str(num1)
    num2 = str(num2)

# Check if length is the same
    if len(num1) != len(num2):
        return False
    
    count1 = {}
    count2 = {}

    for num in num1:
        count1[num] = count1.get(num, 0) + 1

    for num in num2:
        count2[num] = count2.get(num, 0) + 1

    return count1 == count2


