# 🧮 Count characters

## Problem statement

When working with strings, it's often necessary to count how many times a specific character appears within the text. This operation can be useful in various scenarios, such as analyzing text content, validating input, or solving word puzzles. We need a function that can efficiently count the occurrences of a given character in a string, considering both uppercase and lowercase instances of the character as distinct.

## Expected behaviour

Let's say we're implementing a function called `count_char`. We expect `count_char` to behave in the following way:

```python
count_char("hello", 'l') # should return 2
count_char("Mississippi", 's') # should return 4
count_char("Mississippi", 'p') # should return 2
count_char("Cassandra", 'a') # should return 3
count_char("Cassandra", 'A') # should return 1
count_char("The quick brown fox jumps over the lazy dog", 'o') # should return 4
count_char("", 'a') # should return 0
count_char("No matches here", 'z') # should return 0
```

The function should take two parameters:

1. A string in which to search for the character
2. A single character to search for

The function should return:

- An integer representing the number of times the specified character appears in the string

The function should adhere to the following rules:

- It should be case-sensitive (uppercase and lowercase characters are considered different)
- It should work with any printable character, including letters, numbers, and special characters
- It should handle empty strings correctly
- If the character is not found in the string, it should return 0
- It should count all occurrences of the character, even if they are consecutive
