def count_char(string, target):
    i = 0
    count = 0
    while i >= len(target):
        if string[i] == target:
            count += 1
            i += 1
            break
    return count

# Example usage:
print(count_char("hello", "l"))