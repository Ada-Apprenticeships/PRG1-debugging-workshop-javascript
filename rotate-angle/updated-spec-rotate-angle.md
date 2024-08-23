## 🔄 Rotate angle 

## Problem statement

In many applications involving geometry, graphics, or physics, we often need to rotate angles. An angle is typically measured in degrees, with a full circle being 360 degrees. When we rotate an angle, we add or subtract degrees, but we need to ensure that the result always falls within the range of 0 to 359 degrees (inclusive). If the rotation results in an angle outside this range, we need to wrap it around, similar to how a clock face wraps around after 12 hours. We need a function that can perform this rotation calculation, handling both positive and negative rotations, and ensuring the result is always a valid angle between 0 and 359 degrees.

## Expected behaviour

Let's say we're implementing a function called `rotate_angle_by_degrees`.

The function should have two parameters:

- The initial angle in degrees (an integer between 0 and 359, inclusive)
- The rotation in degrees (an integer, positive or negative)

The function should return:

The new angle after rotation, as an integer between 0 and 359 (inclusive)

The function should adhere to the following rules:

- The initial angle should always be between 0 and 359 degrees (inclusive)
- The rotation can be any integer (positive, negative, or zero)
- Positive rotations move clockwise, negative rotations move counterclockwise
- The result should always be normalized to fall between 0 and 359 degrees (inclusive)
- Full rotations (multiples of 360 degrees) should result in the same angle as the starting angle

We expect rotate_angle_by_degrees to behave in the following way:
```python
rotate_angle_by_degrees(45, 45)  # should return 90
rotate_angle_by_degrees(350, 15)  # should return 5
rotate_angle_by_degrees(0, 360)  # should return 0
rotate_angle_by_degrees(180, -180)  # should return 0
rotate_angle_by_degrees(270, 180)  # should return 90
rotate_angle_by_degrees(90, -100)  # should return 350
rotate_angle_by_degrees(0, 720)  # should return 0
rotate_angle_by_degrees(45, -405)  # should return 0
```

This function helps reinforce concepts of modular arithmetic, handling edge cases, and working with cyclic number systems. It's a good exercise for understanding how to normalize values within a specific range, which is a common requirement in many programming scenarios.
