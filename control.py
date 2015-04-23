import RPi.GPIO as GP
import time

GP.setmode(GP.BCM)
#GP.setup(4,   GP.OUT)
GP.setup(12,  GP.OUT)
GP.setup(16,  GP.OUT)
GP.setup(20,  GP.OUT)
GP.setup(21,  GP.OUT)

def turn(B1, B2, B3, B4):
	GP.output(12,B1)
	GP.output(16,B2)
	GP.output(20,B3)
	GP.output(21,B4)
	time.sleep(0.005)

#GP.output(4,1)
i= 1000
while i> 0:
	turn(False,False,False,True)
	turn(False,False,True,False)
	turn(False,True,False,False)
	turn(True,False,False,False)
	i = i-1

turn(False,False,False,False)
GP.cleanup()


