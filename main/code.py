import time, busio, digitalio, board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import KeyPad
import os
import supervisor

import microcontroller



def file_exists(filename):
    return filename in os.listdir()

# Example:

# make this work automatically with any file that it notices
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
lcd_columns = 16
lcd_rows = 2
lcd_address = 0x27
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

dip= bytearray( [
    0b00000,
0b00111,
0b00101,
0b00101,
0b00001,
0b11111,
0b10001,
0b00000

])

undip= bytearray( [
    0b00000,
0b00111,
0b00001,
0b00001,
0b00001,
0b11111,
0b10001,
0b00000

])

rot= bytearray( [
    0b00000,
0b00111,
0b00101,
0b00101,
0b00001,
0b10001,
0b10001,
0b00000

])

plugin= bytearray( [
    0b11111,
  0b10101,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00100,
  0b00100
    
])

plugout= bytearray( [
    0b00000,
  0b00000,
  0b00000,
  0b11111,
  0b10101,
  0b11111,
  0b11111,
  0b01110
    
])

lcd.create_char(0, dip)
lcd.create_char(1, undip)
lcd.create_char(2, rot)
lcd.create_char(3, plugin)
lcd.create_char(4, plugout)

# Setup STEP and DIR pins
step_pin_dip = digitalio.DigitalInOut(board.GP2)
step_pin_dip.direction = digitalio.Direction.OUTPUT
step_pin_rot = digitalio.DigitalInOut(board.GP6)
step_pin_rot.direction = digitalio.Direction.OUTPUT

dir_pin_dip = digitalio.DigitalInOut(board.GP3)  # Optional direction control
dir_pin_dip.direction = digitalio.Direction.OUTPUT
dir_pin_rot = digitalio.DigitalInOut(board.GP7)
dir_pin_rot.direction = digitalio.Direction.OUTPUT


while KeyPad.getkey() != -999:
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Keypad Input")
    lcd.set_cursor_pos(1,0)
    lcd.print("Interference Err")
    time.sleep(.7)
    lcd.set_backlight(False)
    time.sleep(.3)
    lcd.set_backlight(True)
    time.sleep(.3)
    lcd.set_backlight(False)
    time.sleep(.3)
    lcd.set_backlight(True)
    time.sleep(.3)
    lcd.set_backlight(False)
    time.sleep(.3)
    lcd.set_backlight(True)
    time.sleep(.5)
    
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Please Replug")
    lcd.set_cursor_pos(1,0)
    lcd.print("Device")
    time.sleep(.7)
        

def menu_select():
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("  Select Mode:")
    lcd.set_cursor_pos(1,0)
    lcd.print("Hold A,B,C, or D")
    while True:   
        if KeyPad.getkey() == 10:
            A_menu()
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("  Select Mode:")
            lcd.set_cursor_pos(1,0)
            lcd.print("Hold A,B,C, or D")
        if KeyPad.getkey() == 11:
            B_menu()
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("  Select Mode:")
            lcd.set_cursor_pos(1,0)
            lcd.print("Hold A,B,C, or D")
        if KeyPad.getkey() == 12:
            C_menu()
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("  Select Mode:")
            lcd.set_cursor_pos(1,0)
            lcd.print("Hold A,B,C, or D")
        if KeyPad.getkey() == 13:
            D_menu()
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("  Select Mode:")
            lcd.set_cursor_pos(1,0)
            lcd.print("Hold A,B,C, or D")
class Quit(Exception):
    """Custom Class to handle Quiting"""
    def __init__(self, value):
        self.value = value
def A_menu(): #Preprogrammed Menu
    pass
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Events:")
    lcd.set_cursor_pos(0,15)
    lcd.print("A")
    time.sleep(1)
    
    lcd.set_cursor_pos(0,0)
    lcd.print("Select Program ")
    lcd.set_cursor_pos(1,0)
    
    dip_program=""
    characters =["1","2","3","4","5","6","7","8","9","A","B","C","D","*","#","0"]
    cursor=0
    t=True
    while True:
        t=not t
        x = KeyPad.getkey()
        if x != -999: # A key has been pressed!
            if x == 15:
                if not file_exists(f"p{dip_program}.py"):
                    print("here")
                    lcd.set_cursor_pos(1,0)
                    lcd.print("pgm not found :(")
                    time.sleep(.8)
                    lcd.set_cursor_pos(1,0)
                    lcd.print("                ")
                    lcd.set_cursor_pos(1,0)
                    continue
                else:
                    break
            elif x == 14 and cursor>0:
                lcd.set_cursor_pos(1, cursor-1)
                lcd.print(" ")
                cursor-=1
                lcd.set_cursor_pos(1, cursor)
                dip_program=dip_program[:len(dip_program)-1]
            elif x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
            elif x != 14:
                lcd.set_cursor_pos(1, cursor)
                dip_program+=characters[x-1]
                lcd.print(characters[x-1])
                cursor+=1
            print(f"{dip_program} {cursor}")
            #speed+=characters[x-1]
    eval(f"import p{dip_program}") #This may fix the problem mentioned in the comments of the import (do risk assessment)
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print(f"Running {dip_program}")
    lcd.set_cursor_pos(1,0)
    lcd.print("hold \"*\" to stop")
    
    eval(f"p{dip_program}.main(step_pin_dip, dir_pin_dip, step_pin_rot, dir_pin_rot)")
        
def B_menu(): #Manual Programming Menu
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Custom")
    lcd.set_cursor_pos(0,15)
    lcd.print("B")
    time.sleep(1)
    
    lcd.set_cursor_pos(0,0)
    lcd.print("Dip Speed   ")
    lcd.write(0b0)
    lcd.set_cursor_pos(1,0)
    
    dip_time=""
    characters =["1","2","3","4","5","6","7","8","9","A","B","C","D","*","#","0"]
    cursor=0
    t=True
    while True:
        t=not t
        x = KeyPad.getkey()
        if x != -999: # A key has been pressed!
            if x == 15:
                break
            elif x == 14 and cursor>0:
                lcd.set_cursor_pos(1, cursor-1)
                lcd.print(" ")
                cursor-=1
                lcd.set_cursor_pos(1, cursor)
                dip_time=dip_time[:len(dip_time)-1]
            elif x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
            elif x != 14:
                lcd.set_cursor_pos(1, cursor)
                dip_time+=characters[x-1]
                lcd.print(characters[x-1])
                cursor+=1
            print(f"{dip_time} {cursor}")
            #speed+=characters[x-1]
        else:
            lcd.set_cursor_pos(0,12)
            if t:
                lcd.write(0b0)
            else:
                lcd.write(0b1)
    dip_time=int(dip_time)            

    lcd.set_cursor_pos(0,0)
    lcd.print("Dips Per Rot")
    lcd.write(2)
    lcd.set_cursor_pos(1,0)
    rot_inter=""
    cursor=0
    t=True
    while True:
        t=not t
        x = KeyPad.getkey()
        if x != -999: # A key has been pressed!
            if x == 15:
                break
            elif x == 14 and cursor>0:
                lcd.set_cursor_pos(1, cursor-1)
                lcd.print(" ")
                cursor-=1
                lcd.set_cursor_pos(1, cursor)
                rot_inter=rot_inter[:len(dip_time)-1]
            elif x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
            elif x != 14:
                lcd.set_cursor_pos(1, cursor)
                rot_inter+=characters[x-1]
                lcd.print(characters[x-1])
                cursor+=1
            print(f"{dip_time} {cursor}")
            #speed+=characters[x-1]
        else:
            lcd.set_cursor_pos(0,12)
            if t:
                lcd.write(0)
            else:
                lcd.write(2)
    print(rot_inter)            
    rot_inter=int(rot_inter)

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

    lcd.clear()
    lcd.home()
    lcd.print("Running For:  B")
    rot_counter = 1
    while KeyPad.getkey() != 14:      
        for _ in range(step_count_dip):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            #time.sleep(.005)

        # Optional direction change after each full rotation
        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
        #time.sleep(1)  # Wait 1 second before changing direction
        
        for _ in range(step_count_dip):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            #time.sleep(.005)
            
       
        if rot_counter==rot_inter:
            rot_counter=0
            for _ in range(step_count_rot):
                step_pin_rot.value=True
                time.sleep(step_delay)
                step_pin_rot.value=False
        
        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
        rot_counter+=1
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Stopping...")
    time.sleep(.5)
    

def C_menu():
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Programming")
    lcd.set_cursor_pos(1,0)
    lcd.print("Mode")
    time.sleep(.7)
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Please Reconnect")
    lcd.set_cursor_pos(1,0)
    lcd.print("To Use Device")
    time.sleep(.3)
    lcd. set_cursor_pos(1,14)
    lcd.write(3)
    x = KeyPad.getkey()
    if x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
    time.sleep(.3)
    lcd. set_cursor_pos(1,14)
    lcd.write(4)
    x = KeyPad.getkey()
    if x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
    time.sleep(.3)
    lcd. set_cursor_pos(1,14)
    lcd.write(3)
    x = KeyPad.getkey()
    if x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
    time.sleep(.1)
    lcd. set_cursor_pos(1,14)
    time.sleep(.2)
    lcd. set_cursor_pos(1,14)
    lcd.write(4)
    x = KeyPad.getkey()
    if x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
    time.sleep(.3)
    lcd. set_cursor_pos(1,14)
    lcd.write(3)
    x = KeyPad.getkey()
    if x == 10 or x == 11 or x == 12 or x == 13:
                raise Quit(x)
    lcd.close()
    return 0
    #supervisor.reload()

def D_menu():
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Not Avaibale")
    lcd.set_cursor_pos(1,0)
    lcd.print("     Yet...")
    time.sleep(.7)
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Going to Menu...")
    time.sleep(.5)        
while True:
    try:
        menu_select()
    except Quit as e:
        lcd.clear()
        lcd.home()
        if e.value == 10 or e.value == 11 or e.value == 12 or e.value == 13:
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("Going Back To")
            lcd.set_cursor_pos(1,0)
            lcd.print("Menu")
        time.sleep(.5)
    '''    
    except Exception as e:
        print(f"error occured {e}, restarting...")
        lcd.clear()
        lcd.home()
        lcd.print("error occured,\nrestarting...")
        time.sleep(1)
'''    
lcd.close()



