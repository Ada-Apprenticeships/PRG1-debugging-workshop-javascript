# 📜 Text in div

## Problem statement

### Fitting text in a certain space

This problem involves implementing a function that takes two arguments, text and width, and formats the text to fit the width.

Your function should divide the given text into lines using newline characters. It should fit as many words into each line as possible without exceeding the given width or splitting any words between two lines. There should not be a space at the beginning or end of any line. The minimum input for the width is 15. Anything below 15 should return "INVALID INPUT"

## Expected behaviour

Let's say we're implementing a function called `text_in_div`. We expect `text_in_div` to behave in the following way:

```python
text_in_div("This is a sample text that needs to be formatted", 20)
# should return:
# "This is a sample\ntext that needs to\nbe formatted"

text_in_div("Short text", 15)
# should return:
# "Short text"

text_in_div("This is some text", 10)
# should return:
# "INVALID INPUT"

text_in_div("Pneumonoultramicroscopicsilicovolcanoconiosis is a long word", 30)
# should return:
# "Pneumonoultramicroscopicsilicovo\nlcanoconiosis is a long word"
```

The function should adhere to the following rules:
- It should not split words across lines
- It should not have trailing spaces at the end of lines
- It should return "INVALID INPUT" for widths less than 15
- It should handle very long words by placing them on their own line, even if they exceed the specified width
