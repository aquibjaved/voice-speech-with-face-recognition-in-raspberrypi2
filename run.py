import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 4
buttonPin2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(buttonPin2,GPIO.IN)

while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    os.system("sudo python /home/pi/aquib/face_recog/test.py")
    
  
  elif  (GPIO.input(buttonPin2)):
    os.system("sudo python /home/pi/aquib/face_recog/switch2.py") 