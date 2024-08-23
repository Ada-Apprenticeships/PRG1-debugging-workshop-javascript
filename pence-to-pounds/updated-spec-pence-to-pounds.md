# 🪙 Pence to pounds

## Problem statement

In the United Kingdom and some other countries, the currency is divided into pounds (£) and pence (p), where 100 pence make up one pound. When dealing with financial calculations or displaying prices, it's often necessary to convert an amount given entirely in pence to its equivalent in pounds and pence. This conversion needs to accurately represent the amount with pounds as the whole number part and pence as the decimal part, formatted correctly as currency.

## Expected behaviour

The function should take one parameter:

- An integer representing the amount in pence

The function should return a string that:

- Starts with the pound symbol (£)
- Shows the number of whole pounds
- Uses a decimal point to separate pounds and pence
- Always shows two decimal places for the p