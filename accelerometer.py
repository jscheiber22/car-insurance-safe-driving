from math import sqrt
import board
import adafruit_adxl34x
from time import sleep


class Accelerometer():
    def __init__(self):
        i2c = board.I2C()
        self.acc = adafruit_adxl34x.ADXL343(i2c)

        # Zero the device's data on the x and y axis
        print("Starting process of zeroing device...")
        sleep(0.5)
        accx_off1, accy_off1 = self.acc.acceleration[:2]
        for x in range(3,0,-1):
            print(str(x), end='\r')
            sleep(1)
        accx_off2, accy_off2 = self.acc.acceleration[:2]
        self.accx_offset = (accx_off1 + accx_off2) / 2
        self.accy_offset = (accy_off1 + accy_off2) / 2
        print("Zero completed with values: {}, {}.".format(self.accx_offset, self.accy_offset))

    # Returns x-axis acceleration in meters per second squared averaged over 0.5 seconds
    def getAccX(self):
        runningTotal = 0
        for i in range(0, 6):
            runningTotal += self.acc.acceleration[0]
            sleep(0.1)
        accx = runningTotal / 5
        return accx - self.accx_offset
    

    # Returns y-axis acceleration in meters per second squared averaged over 0.5 seconds
    def getAccY(self):
        runningTotal = 0
        for i in range(0, 6):
            runningTotal += self.acc.acceleration[1]
            sleep(0.1)
        accy = runningTotal / 5
        return accy - self.accy_offset
    

    # Returns x-axis acceleration in MPH per second
    def getAccXMPH(self):
        conversion_factor = 2.23693629
        accx = self.getAccX()
        return accx * conversion_factor
    

    # Returns y-axis acceleration in MPH per second
    def getAccYMPH(self):
        conversion_factor = 2.23693629
        accy = self.getAccY()
        return accy * conversion_factor
    

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
