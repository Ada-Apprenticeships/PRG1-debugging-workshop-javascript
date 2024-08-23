# 🧮 Print multiplication table

## Problem statement

Multiplication tables are fundamental tools in mathematics education, helping students learn and memorize basic multiplication facts. These tables show the product of two numbers for a range of values, typically from 1 to 10 or 1 to 12. Creating such a table manually can be time-consuming and error-prone. We need a way to automatically generate a multiplication table for a given number, showing its products with a range of integers.

## Expected behaviour

Let's say we're implementing a function called `print_multiplication_table`. We expect `print_multiplication_table` to behave in the following way:

```python
print_multiplication_table(5)  # should print:
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
...
12 x 5 = 60

print_multiplication_table(3)  # should print:
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
4 x 3 = 12
5 x 3 = 15
...
12 x 3 = 36
```

The function should take two parameters:

1. The number for which the multiplication table is to be generated
2. The upper limit of the range (i.e., how far the table should go)

The function should print each line of the multiplication table to the console, showing the multiplication expression and its result. Each line should be in the format "a x b = c", where 'a' is the number for which the table is being generated, 'b' is the current number in the range, and 'c' is their product.

The function should work for any positive integer inputs, allowing for flexibility in both the number being multiplied and the range of the table.
