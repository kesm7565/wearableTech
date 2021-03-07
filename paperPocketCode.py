# Add your Python code here. E.g.
from microbit import *

inputArray = [0,0] #initializing array
while True:
    if button_a.is_pressed():#when the a button is pressed, push the vale 1 to the array
        inputArray.append(1)
        
    elif button_b.is_pressed():#when the b button is pressed, push the vale 2 to the array
        inputArray.append(2)
        
    if inputArray[len(inputArray) - 1] == 1:#if the most recent value in the array is a 1, turn servo to position 50
        pin0.write_analog(50)
       
        
    elif inputArray[len(inputArray) - 1] == 2:#if the most recent value in the array is a 2, turn servo to position 100
        pin0.write_analog(100)
        
    if len(inputArray) > 3:#if the length of the inputArray becomes greater than 3, delete the first value (minimizing data stored)
        inputArray.pop(0)
