def is_palindrome(text):
    reverse_text = text[::-1]
    if text == reverse_text:
        return True
    else:
        return False

word = input("Enter a word or number\n")

if is_palindrome(word):
    print("palindrome")
else:
    print("not palindrome")


