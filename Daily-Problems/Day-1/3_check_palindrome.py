# Determine whether a string is a palindrome or not.

# A palindrome is a string that is read the same from front to back and back to front.
# For example, noon and racecar are both palindromes.


def is_palindrome(text):
    """
    Return True if text is a palindrome else False.
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('moon')
    False
    """
    return text == text[::-1]


if __name__ == "__main__":
    text = input("Enter text to check palindrome: ")
    print(is_palindrome(text))
