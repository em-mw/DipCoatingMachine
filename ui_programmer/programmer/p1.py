import time, busio, digitalio, board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import KeyPad
import os
def main(step_pin_dip, dir_pin_dip, step_pin_rot, dir_pin_rot):
    while True:
        for _ in range(0):
            dir_pin_dip.value = False
            for _ in range(600):
                step_pin_rot.value = True
                time.sleep(0.001)
                step_pin_rot.value = False

        time.sleep(0.0)

        dir_pin_dip.value = False
        for _ in range(600):
            step_pin_dip.value = True
            time.sleep(0.1)
            step_pin_dip.value = False
