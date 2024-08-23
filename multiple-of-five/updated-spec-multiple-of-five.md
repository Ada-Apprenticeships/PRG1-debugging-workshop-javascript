# 🧮 Is multiple of 5?

## Problem statement

In many programming scenarios, we need to determine if a number is divisible by another number without a remainder. A common case is checking if a number is a multiple of 5, which has various applications in mathematics and real-world problems. For example, this could be useful in problems involving currency (where the smallest unit is 5 cents), or in creating patterns or groupings based on multiples of 5. We need a function that can quickly and accurately determine whether a given integer is a multiple of 5.

## Expected behaviour

The function should take one parameter:

- An integer (positive, negative, or zero)

The function should return:

- `True` if the input number is a multiple of 5 (i.e., divisible by 5 without a remainder)
- `False` if the input number is not a multiple of 5

Let's say we're implementing a function called `is_multiple_of_five`. We expect `is_multiple_of_five` to behave in the following way:

```python
is_multiple_of_five(0)  # should return True
is_multiple_of_five(5)  # should return True
is_multiple_of_five(10)  # should return True
is_multiple_of_five(15)  # should return True
is_multiple_of_five(100)  # should return True
is_multiple_of_five(101)  # should return False
is_multiple_of_five(-7)  # should return False
```

The function should work for any integer input, including positive numbers, negative numbers, and zero. It should correctly identify multiples of 5 regardless of whether they are positive or negative.
