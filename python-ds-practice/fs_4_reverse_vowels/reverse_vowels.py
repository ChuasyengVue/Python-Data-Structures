def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """


    vowels = set("aeiou")

    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() not in vowels:
            left += 1
        elif s[right].lower() not in vowels:
            right -= 1
        else :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)