def convert_to_12_hours(time):
    hours = int(time[:2])
    minutes = time[-2:]
    
    if hours > 12:
        return f"{hours - 12:02d}:{minutes} pm"
    else:
        return f"{hours:02d}:{minutes} am"

# Hint: I recommend calling the function with an input of '12:05'


