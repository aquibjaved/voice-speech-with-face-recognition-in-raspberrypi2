import time,sys,subprocess,os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.OUT,initial=GPIO.LOW)
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
while True:
	input = GPIO.input(25)
	#take a reading
	input = GPIO.input(4)
	#if the last reading was low and this one high, print
	if ((not prev_input) and input):
		print("Button pressed")
		GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)
		execfile('face_rec_rpi.py')
		GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
		time.sleep(2)
	#update previous input
	prev_input = input
	GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
	#slight pause to debounce
	time.sleep(0.05)