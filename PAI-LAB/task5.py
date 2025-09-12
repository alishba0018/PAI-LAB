def is_palindrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return f"'{text}' is a palindrome."
    else:
        return f"'{text}' is not a palindrome."

print(is_palindrome('maham'))
print(is_palindrome('a nut for a jar of tuna'))
print(is_palindrome('madam'))
print(is_palindrome('hello'))