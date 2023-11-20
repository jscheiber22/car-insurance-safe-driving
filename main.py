from accelerometer import Accelerometer
from audio import Audio
from time import sleep
import math

class CarInsuranceSafeDriving():
	def __init__(self):
		# Definition of accleration limits
		# 0-60 in 6 seconds is 10 mph/s
		self.max_acc = 10 # mph/s

		self.acc = Accelerometer()
		self.alert = Audio()


	def update_acceleration(self):
		return self.acc.combinedAccelerationMPH()


	def check_acceleration(self, acc):
		if acc > self.max_acc:
			print("total acc: " + str(round(acc, 3)), end='\r')
			return False
		else:
			return True
		

if __name__ == "__main__":
	cisd = CarInsuranceSafeDriving()
	safe = True
	dangerous_acceleration_counter = 0

	while True:
		acc = cisd.update_acceleration()
		safe = cisd.check_acceleration(acc)
		if not safe:
			# play alert nonstop if user violated 3 times
			if dangerous_acceleration_counter > 2:
				while True:
					cisd.alert.alert()
					sleep(1)
			else:
				print("not safe :(")
				cisd.alert.alert()
				dangerous_acceleration_counter += 1

