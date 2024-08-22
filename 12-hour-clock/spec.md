# 🕥 12 hour clock

## Problem statement

Many countries use a 24-hour clock (also known as "military time") where the hours of the day are numbered from 0 to 23. However, in some countries, particularly English-speaking ones, the 12-hour clock system is more commonly used in everyday life. In this system, the day is divided into two periods: a.m. (ante meridiem, meaning "before midday") and p.m. (post meridiem, meaning "after midday"). We need a way to convert time from the 24-hour format to the 12-hour format.

## Expected behaviour

The function should take a string representing time in 24-hour format (HH:MM) as input and return a string representing the same time in 12-hour format with AM/PM indicator. The function should handle the following cases correctly:

- Midnight (00:00 in 24-hour time) should be converted to 12:00 AM
- Noon (12:00 in 24-hour time) should be converted to 12:00 PM
- Hours from 1:00 to 11:59 should be labeled AM
- Hours from 13:00 to 23:59 should be converted to 1:00 PM to 11:59 PM respectively

Let's say we're implementing a function called `convertTo12HourClock`. We expect `convertTo12HourClock` to behave in the following way:

```js
convertTo12HourClock("14:25") // should return "2:25 PM"
convertTo12HourClock("23:59") // should return "11:59 PM"
convertTo12HourClock("00:00") // should return "12:00 AM"
convertTo12HourClock("12:00") // should return "12:00 PM"
convertTo12HourClock("01:30") // should return "1:30 AM"
convertTo12HourClock("09:45") // should return "9:45 AM"
```


