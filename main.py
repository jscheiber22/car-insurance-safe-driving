from accelerometer import Accelerometer
from time import sleep
import math

class CarInsuranceSafeDriving():
	def __init__(self):
		# Definition of accleration limits
		# 0-60 in 9 seconds is 6.667 mph/s
		self.max_acc = 6.667 # mph/s      

		self.acc = Accelerometer()


	def update_acceleration(self):
		return self.acc.combinedAccelerationMPH()


	def check_acceleration(self, acc):
		
		if acc > self.max_acc:
			print("total acc: " + str(round(acc, 3)), end='\r')
			return False
		else:
			return True
		
	# 	check_acceleration(accx, accy, accz)
	# 	print("x: " + str(round(accx, 3)) + " y: " + str(round(accy, 3)) + " z: " + str(round(accz, 3)), end='\r')
	# 	#print("y: \n" + str(accy), end='\r')
	# 	#print("z: \n" + str(accz), end='\r')


if __name__ == "__main__":
	cisd = CarInsuranceSafeDriving()
	safe = True
	while True:
		acc = cisd.update_acceleration()
		safe = cisd.check_acceleration(acc)
		if not safe:
			print("not safe :(")

