import math

def calculate_percentage_change(original, new_amount):
    difference = abs(new_amount - original)
    average = (original - new_amount) / 2
    percentage_change = (average / difference) * 100
    return round(percentage_change, 2)

# Example usage:
print(calculate_percentage_change(50, 40))
print(calculate_percentage_change(100, 120)) 
print(calculate_percentage_change(200, 150)) 
print(calculate_percentage_change(100, 100))
print(calculate_percentage_change(0, 100))