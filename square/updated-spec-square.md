# 🟥 Square

## Problem statement

In mathematics, squaring a number means multiplying it by itself. This operation is fundamental in many areas of mathematics and has numerous practical applications in fields such as physics, engineering, and computer science. We need a simple function that can calculate the square of any given number. This function should work with both positive and negative numbers, as well as zero, and should be able to handle both integers and floating-point numbers.

## Expected behaviour

Let's say we're implementing a function called `square` to satisfy the problem statement. The function should take one parameter:

A number (integer or floating-point) to be squared

The function should return:

The square of the input number 
 We expect square to behave in the following way:

```python
square(4)  # should return 16
square(-3)  # should return 9
square(0)  # should return 0
square(2.5)  # should return 6.25
square(1000000)  # should return 1000000000000 (1 trillion)
```
