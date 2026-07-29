# KeyPad Vers #2
# Tony Goodhew 9th May 2020
# Connections left to right on KeyPad
# 0   1   2   3   4   5   6   7
# D7  D9  D10 D11 A5  A4  A3  A2 on ItsyBitsy
import board
import gc
import time
from digitalio import DigitalInOut, Direction, Pull
gc.collect() # make some room

# Set up LED on pin 13
#led = DigitalInOut(board.D13)
#led.direction = Direction.OUTPUT

# Set up Rows
rows = [] 
for p in [board.GP10, board.GP11, board.GP12, board.GP13]:
    row = DigitalInOut(p)
    row.direction = Direction.OUTPUT
    rows.append(row)
# anodes OFF
for i in range(4):
    rows[i].value = 0

# Set up columns[18, 19, 20, 21]
cols = []
for p in [board.GP18, board.GP19, board.GP20, board.GP21]:
    col = DigitalInOut(p)
    col.direction = Direction.INPUT
    col.pull = Pull.DOWN
    cols.append(col)

def getkey():  # Returns -999 or key value
    values = [1,2,3,10, 4,5,6,11, 7,8,9,12, 14,0,15,13]
    val = -999 # Error value for no key press
    for count in range(10): # Try to get key press 10 times
        for r in range(4):  # Rows, one at a time
            rows[r].value = 1 # row HIGH
            for c in range(4): # Test columns, one at a time
                if cols[c].value == 1: # Is column HIGH?
                    p = r * 4 + c      # Pointer to values list
                    val = values[p]
                    count = 11 # This stops looping
                    #led.value = 1 # Flash LED ON if key pressed
            rows[r].value = 0 # row LOW
    time.sleep(0.2) # Debounce
    #led.value = 0 # LED OFF
    return val

def getvalue(digits): # Number of digits
    result = 0
    count = 0
    while True:
        x = getkey()
        if x != -999 and x < 10: # Check if numeric key pressed
            result = result * 10 + x
            print(result)
            count = count + 1
        if count == digits:
            return result

if __name__ == "__main__":
    print("\nPress any of the keys\n # halts the program")

    characters =["1","2","3","4","5","6","7","8","9","A","B","C","D","*","#","0"]
    running = True
    while running:
        x = getkey()
        if x != -999: # A key has been pressed!
            print(characters[x-1])
            if x == 15:
                running = False
