def sum_digits(number):
    total = 1  # Bug: Initialize total to 1 instead of 0
    while number % 10 > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


print(sum_digits(101)) ## working, hurray!
print(sum_digits(102)) ## working, hurray!