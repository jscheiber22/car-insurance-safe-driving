from accelerometer import Accelerometer
from audio import Audio
from time import sleep

class CarInsuranceSafeDriving():
	def __init__(self):
		# Definition of accleration limits
		# 0-60 in 6 seconds is 10 mph/s
		self.max_acc = 10 # mph/s

		self.acc = Accelerometer()
		self.alert = Audio()

		self.danger_counter = 0


	def update_acceleration(self):
		return self.acc.combinedAccelerationMPH()


	def check_acceleration(self, acc):
		if acc > self.max_acc:
			print("total acc: " + str(round(acc, 3)), end='\r')
			self.danger_counter += 1
			return False
		else:
			return True
		

if __name__ == "__main__":
	cisd = CarInsuranceSafeDriving()
	safe = True
	dangerous_acceleration_counter = 0

	while True:
		try:
			acc = cisd.update_acceleration()
			safe = cisd.check_acceleration(acc)
			if not safe:
				# play alert nonstop if user violated 3 times
				if dangerous_acceleration_counter > 2:
					for i in range(0, 6):
						cisd.alert.alert()
						sleep(0.5)
				else:
					print("not safe :(")
					cisd.alert.alert()
					dangerous_acceleration_counter += 1
		except KeyboardInterrupt:
			print("Total driver errors: {}".format(cisd.danger_counter))
			if cisd.danger_counter > 5:
				print("Bad driver. +$1000/month.")
			elif cisd.danger_counter > 1:
				print("Fine driver. No difference.")
			else:
				print("Excellent driver. -$1/month.")
			exit()

