import time, busio, digitalio, board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import KeyPad
import os

import microcontroller



def file_exists(filename):
    return filename in os.listdir()

# Example:
if file_exists("p0.py"):import p0
if file_exists("p1.py"):import p1
if file_exists("p2.py"):import p2
if file_exists("p3.py"):import p3
if file_exists("p4.py"):import p4
if file_exists("p5.py"):import p5
if file_exists("p6.py"):import p6
if file_exists("p7.py"):import p7
if file_exists("p8.py"):import p8
if file_exists("p9.py"):import p9




#Display Functionality
#lcd_columns = 16
#lcd_rows = 2
#lcd_address = 0x27
#i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
#lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


# Setup STEP and DIR pins
step_pin_dip = digitalio.DigitalInOut(board.GP2)
step_pin_dip.direction = digitalio.Direction.OUTPUT
step_pin_rot = digitalio.DigitalInOut(board.GP6)
step_pin_rot.direction = digitalio.Direction.OUTPUT

dir_pin_dip = digitalio.DigitalInOut(board.GP3)  # Optional direction control
dir_pin_dip.direction = digitalio.Direction.OUTPUT
dir_pin_rot = digitalio.DigitalInOut(board.GP7)
dir_pin_rot.direction = digitalio.Direction.OUTPUT




class Quit(Exception):
    """Custom Class to handle Quiting"""
    def __init__(self, value):
        self.value = value
        
def B_menu():

    dip_time=0
    rot_inter=1
    
    # Set direction
    dir_pin_dip.value = True  # True or False for direction
    dir_pin_rot.value = True

    # Motor step settings
    #dip_time=1
    step_delay = (((dip_time)*.00158245)+.000341841)
    print(step_delay)
    if step_delay < .001:
        step_delay = 0.001  # Delay between steps in seconds (adjust for speed)
    #step_delay = .001
    
    microMode = 8
    # full rotation multiplied by the microstep divider
    step_count_dip=600
    step_count_rot = int(200 * microMode/4)

    print("Running For:  B")
    counter=0
    rot_counter = 1
    while KeyPad.getkey() != 14:      
        dir_pin_dip.value=True
        print(counter,"next")
        #for _ in range(step_count_dip):
            #step_pin_dip.value = True
           ## time.sleep(step_delay)
            #step_pin_dip.value = False
            #time.sleep(.005)
        

        # Optional direction change after each full rotation
        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
        #time.sleep(1)  # Wait 1 second before changing direction
        
        for _ in range(step_count_dip):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            time.sleep(.000000001)
        input("dip")
        dir_pin_dip.value = not dir_pin_dip.value
        for _ in range(step_count_dip):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            time.sleep(.000000001)
            
        for _ in range(step_count_rot):
            step_pin_rot.value=True
            time.sleep(step_delay)
            step_pin_rot.value=False
            time.sleep(.000000001)
        
        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
        rot_counter+=1
        counter+=1
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Stopping...")
    time.sleep(.5)
    
B_menu()

