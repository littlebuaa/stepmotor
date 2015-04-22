import RPi.GPIO as GP
import time


GP.setmode(GP.BCM)
#GP.setup(4,   GP.OUT)
GP.setup(12,  GP.OUT)
GP.setup(16,  GP.OUT)
GP.setup(20,  GP.OUT)
GP.setup(21,  GP.OUT)

#GP.output(4,1)

 
def turn():
	GP.output(12,False)
	GP.output(16,False)
	GP.output(20,False)
	GP.output(21,True)
	time.sleep(5)
def stop():
	pass

turn()

