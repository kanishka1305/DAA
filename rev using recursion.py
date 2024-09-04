def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)
number = 12345
reverse = reverse_number(number)
print(f"The reverse of {number} is: {reverse}")
