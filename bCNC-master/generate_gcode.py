# Python Script to Generate G-code
increment = 0.7
final_position = 55.0

print("G90")  # Set to Absolute Positioning
print("F50")  # Set the feedrate to 50
print("G01 X0 Y0")  # Move the tool to the starting point (0,0)

position = 0.0
while position < final_position:
    position += increment
    if position > final_position:
        position = final_position
    print(f"G01 X{position:.1f} Y0")  # Move to the new X position with Y remaining at 0
    print("G04 P1")  # Pause for 1 second

