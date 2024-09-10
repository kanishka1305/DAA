def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
