import math

def find_century(year):
    century = math.floor((year - 1) / 100) + 1
    return str(century) + get_ordinal_suffix(century)

def get_ordinal_suffix(n):
    last_digit = n % 10
    
    if last_digit == 1:
        return 'st'
    elif last_digit == 2:
        return 'nd'
    elif last_digit == 3:
        return 'rd'
    else:
        return 'th'

# Example usage:
print(find_century(1900))  # Output: 19th
print(find_century(2000))  # Output: 20th
print(find_century(2001))  # Output: 21st
print(find_century(2100))  # Output: 21st (bug: should be 22nd)
print(find_century(2012))  # Output: 21st (bug: should be 21st)