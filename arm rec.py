def order(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

def is_armstrong(n, order):
    if n == 0:
        return 0
    else:
        return ((n % 10) ** order) + is_armstrong(n // 10, order)

num = int(input("Enter a number: "))
order_num = order(num)

if num == is_armstrong(num, order_num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
