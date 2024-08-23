def print_times_table(n):
    i = 0
    while i < n:  # Changed <= to < as an additional subtle bug
        print(f"{i} x {n} = {i * 5}")  # Preserved the original bug (multiplying by 5 instead of n)
        i += 1

# Example usage:
print("Times table for 3:")
print_times_table(3)
print("\nTimes table for 5:")
print_times_table(5)
print("\nTimes table for 0:")
print_times_table(0)
print("\nTimes table for 10:")
print_times_table(10)