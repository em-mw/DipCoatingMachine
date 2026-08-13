import time, busio, digitalio, board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import KeyPad
import os
def main(step_pin_dip, dir_pin_dip, step_pin_rot, dir_pin_rot):
    while True:
        dir_pin_dip.value = True
        for _ in range(600):
            step_pin_dip.value = True
            time.sleep(0.0022727272727272726)
            step_pin_dip.value = False

        if KeyPad.getKey() == 14:
            exit()
