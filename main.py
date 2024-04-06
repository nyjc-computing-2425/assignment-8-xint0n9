def reverse(text):
    """
    take in parameter which is string
    recursive function to reverse the string
    """
    if len(text) == 0:
        return ''
    return reverse(text[1:]) + text[0]


def is_palindrome(text):
    """
    check if text is a palindrome
    """
    if len(text) <= 1:
        return True
    text = text.strip(',.?!():;').upper()
    print(text)
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])
