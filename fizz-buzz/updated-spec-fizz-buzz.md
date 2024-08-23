# 🌟 Fizz buzz!

## Problem statement

FizzBuzz is a classic programming problem often used in coding interviews. The task is to print a sequence of numbers, but with a twist. For multiples of three, instead of the number, print "Fizz". For multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz". This problem tests a programmer's ability to handle multiple conditions and loop structures, as well as their understanding of divisibility rules.

## Expected behaviour

Let's say we're implementing a function called `fizz_buzz` to satisfy the problem statement.

The function should have one parameter:

- A positive integer n, representing the number of elements in the sequence to process

The function should:

- Print numbers from 1 to n, each on a new line
- For multiples of 3, print "Fizz" instead of the number
- For multiples of 5, print "Buzz" instead of the number
- For multiples of both 3 and 5, print "FizzBuzz" instead of the number

We expect `fizz_buzz` to behave in the following way:

```python
fizz_buzz(15) # should print:
```
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

```python
fizz_buzz(5) # should print:
```
```
1
2
Fizz
4
Buzz
```

Additional considerations:

- The function should work for any positive integer input
- It should handle edge cases, such as when n is less than or equal to 0 (in which case it might not print anything)
- The function doesn't return any value; it only prints to the console
- The order of checking for multiples matters: check for multiples of both 3 and 5 first, then 3, then 5

This function helps reinforce understanding of loops, conditionals, and the modulo operator, making it an excellent exercise for beginners and a quick test for more experienced programmers.
