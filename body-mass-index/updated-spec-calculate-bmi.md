# ⚖️ Calculate BMI (**B**ody **M**ass **I**ndex)

## Problem statement

Body Mass Index (BMI) is a simple measure that uses your height and weight to work out if your weight is healthy. The BMI is an attempt to quantify the amount of tissue mass (muscle, fat, and bone) in an individual, and then categorize that person as underweight, normal weight, overweight, or obese based on that value. However, it's important to remember that BMI is not a perfect measure because it does not account for body composition. We need a way to calculate a person's BMI given their weight and height.

## Expected behaviour

Let's say we're implementing a function called `calculate_body_mass_index`. We expect `calculate_body_mass_index` to behave in the following way:

```python
calculate_body_mass_index(70, 1.75) # should return approximately 22.86 (for 70 kg and 1.75 m)
calculate_body_mass_index(68, 1.65) # should return approximately 24.98 (for 68 kg and 1.65 m)
calculate_body_mass_index(100, 1.82) # should return approximately 30.19 (for 100 kg and 1.82 m)
```

The function should take two parameters: the person's weight in kilograms and their height in meters. It should return the calculated BMI rounded to two decimal places. The BMI is calculated by dividing the person's weight by the square of their height.
