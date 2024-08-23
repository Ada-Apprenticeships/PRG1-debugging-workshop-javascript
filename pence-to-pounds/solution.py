def pence_to_pounds(pence):
    pounds = pence / 100
    return f"£{pounds:.2f}"  # Format to two decimal places

# Example usage:
print(pence_to_pounds(199))   # £1.99 (correct)
print(pence_to_pounds(50))    # £0.50 (correct)
print(pence_to_pounds(1000))  # £10.00 (correct)
print(pence_to_pounds(0))     # £0.00 (correct)
print(pence_to_pounds(101))   # £1.01 (correct)
print(pence_to_pounds(-50))   # £-0.50 (bug: should not allow negative values)
print(pence_to_pounds(1.5))   # £0.02 (bug: incorrect handling of float input)

