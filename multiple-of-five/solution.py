def get_last_digit(num):
    return str(num)[-1]

def is_multiple_of_five(n):
    print('The value of n -->', n)
    if get_last_digit(n) == 5 or get_last_digit(n) == 0:
        return True
    else:
        return False

# Example usage:
print(is_multiple_of_five(10))  # True
print(is_multiple_of_five(15))  # True
print(is_multiple_of_five(7))   # False
