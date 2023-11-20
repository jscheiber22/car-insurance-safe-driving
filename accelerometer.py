from math import sqrt
import board
import adafruit_adxl34x
from time import sleep


class Accelerometer():
    def __init__(self):
        i2c = board.I2C()
        self.acc = adafruit_adxl34x.ADXL343(i2c)

        # Zero the device's data on the x and y axis
        accx_off1, accy_off1, accz = self.acc.acceleration
        sleep(3)
        accx_off2, accy_off2, accz = self.acc.acceleration
        self.accx_offset = (accx_off1 + accx_off2) / 2
        self.accy_offset = (accy_off1 + accy_off2) / 2

    # Returns x-axis acceleration in meters per second squared
    def getAccX(self):
        accx, accy, accz = self.acc.acceleration
        return accx - self.accx_offset
    

    # Returns y-axis acceleration in meters per second squared
    def getAccY(self):
        accx, accy, accz = self.acc.acceleration
        return accy - self.accy_offset
    

    # Returns x-axis acceleration in MPH per second
    def getAccXMPH(self):
        conversion_factor = 2.23693629
        accx, accy, accz = self.acc.acceleration
        return (accx - self.accx_offset) * conversion_factor
    

    # Returns y-axis acceleration in MPH per second
    def getAccYMPH(self):
        conversion_factor = 2.23693629
        accx, accy, accz = self.acc.acceleration
        return (accy - self.accy_offset) * conversion_factor
    

    # Returns total acceleration on the x-y plane in meters per second squared
    def combinedAcceleration(self):
        x = self.getAccX()
        y = self.getAccY()
        combined_acceleration = sqrt((x * x) + (y * y)) # a^2 + b^2 = c^2
        return combined_acceleration
    

    # Returns total acceleration on the x-y plane in MPH per second
    def combinedAccelerationMPH(self):
        x = self.getAccXMPH()
        y = self.getAccYMPH()
        combined_acceleration = sqrt((x * x) + (y * y)) # a^2 + b^2 = c^2
        return combined_acceleration
