def rotate_angle_by_degrees(initial_angle, rotation):
    # Calculate the new angle
    new_angle = initial_angle + (rotation % 360)
    
    # Attempt to normalize the angle (but with a bug)
    if new_angle >= 360:
        new_angle -= 360
    
    return new_angle

# Example usage:
print(rotate_angle_by_degrees(45, 45))   # Expected: 90, Actual: 90
print(rotate_angle_by_degrees(350, 15))  # Expected: 5, Actual: 5
print(rotate_angle_by_degrees(0, 360))   # Expected: 0, Actual: 0
print(rotate_angle_by_degrees(180, 180)) # Expected: 0, Actual: 0
print(rotate_angle_by_degrees(270, 180)) # Expected: 90, Actual: 90
print(rotate_angle_by_degrees(90, 720))  # Expected: 90, Actual: 90
print(rotate_angle_by_degrees(45, -45))  # Expected: 0, Actual: 0
print(rotate_angle_by_degrees(0, -90))   # Expected: 270, Actual: -90 (bug)
print(rotate_angle_by_degrees(400, 0))   # Expected: 40, Actual: 400 (bug)

