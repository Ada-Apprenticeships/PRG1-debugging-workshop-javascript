# 📐 Is it a valid triangle?

## Problem statement

In geometry, a triangle is a shape with three sides. However, not every combination of three lengths can form a valid triangle. A fundamental rule in triangle construction is that the sum of the lengths of any two sides must be greater than the length of the remaining side. This rule ensures that the triangle can be closed. We need a function that can determine whether three given lengths can form a valid triangle. This function could be useful in various geometric applications, including computer graphics, game development, or mathematical problem-solving.

## Expected behaviour

Let's say we're implementing a function called `is_valid_triangle`. We expect `is_valid_triangle` to behave in the following way:

```python
is_valid_triangle(3, 4, 5)  # should return True
is_valid_triangle(5, 12, 13)  # should return True
is_valid_triangle(1, 1, 1)  # should return True
is_valid_triangle(1, 2, 3)  # should return False
is_valid_triangle(2, 4, 2)  # should return False
is_valid_triangle(7, 3, 2)  # should return False
is_valid_triangle(0, 0, 0)  # should return False
is_valid_triangle(-1, 2, 3)  # should return False
```

The function should take three parameters:

- Three numbers representing the lengths of the sides of a potential triangle

The function should return:

- `True` if the three lengths can form a valid triangle
- `False` if the three lengths cannot form a valid triangle

The function should adhere to the following rules:

- The triangle inequality theorem must be satisfied for all three combinations of sides:
    - a + b > c
    - b + c > a
    - c + a > b
    Where a, b, and c are the lengths of the three sides.
- All side lengths must be positive numbers greater than zero
- The function should work with integer or floating-point numbers
- The function should return False for any invalid inputs (negative numbers or zero)

This function helps reinforce understanding of geometric principles and conditional logic, making it a good exercise for students learning about both mathematics and programming.
