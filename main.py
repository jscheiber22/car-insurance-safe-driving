from time import sleep
import board
import adafruit_adxl34x
import math

i2c = board.I2C()
acc = adafruit_adxl34x.ADXL343(i2c)
#accx, accy, accz = acc.acceleration

max_mph = 60
max_g_force = 0.5

def check_acceleration(accx, accy, accz=0):
        # Convert 0-60 mph in 12 seconds to m/s^2
        car_acceleration_x = max_mph * 0.44704 / 10 
       # car_acceleration_x = 3.5

        # Convert g force to m/s^2
        car_acceleration_y = max_g_force * 9.81

        if accx > car_acceleration_x:
                print("Acceleration in the x direction surpasses the car's 0-60 mph in 12 seconds acceleration. accx is " + str(accx))

        if accy > car_acceleration_y:
                #print("Acceleration in the y direction surpasses 0.5g force.")
                pass


print("")

while True:
	accx, accy, accz = acc.acceleration
	check_acceleration(accx, accy, accz)
	print("x: " + str(round(accx, 3)) + " y: " + str(round(accy, 3)) + " z: " + str(round(accz, 3)), end='\r')
	#print("y: \n" + str(accy), end='\r')
	#print("z: \n" + str(accz), end='\r')
