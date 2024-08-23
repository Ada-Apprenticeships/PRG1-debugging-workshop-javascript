# 📆 Find century

## Problem statement

Given a year as a string, we need to find the century for that year.

## Expected behaviour

Let's say we're implementing a function called `find_century`. We expect `find_century` to behave in the following way:

```python
find_century(1066) # should return "11th"
find_century(1900) # should return "19th"
find_century(2000) # should return "20th"
find_century(2001) # should return "21st"
find_century(2100) # should return "21st"
```

The function should take one parameter:
- A string representing a year

The function should return:
- A string representing the century, including the appropriate ordinal suffix (st, nd, rd, or th)

The function should adhere to the following rules:
- The first century spans from the year 1 up to and including the year 100
- The second century spans from the year 101 up to and including the year 200
- The 20th century spans from the year 1901 up to and including the year 2000
- The 21st century began with the year 2001
- The function should handle any valid year input, including years before 1 (BCE) and far into the future
