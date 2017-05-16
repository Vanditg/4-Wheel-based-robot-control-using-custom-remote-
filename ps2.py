import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

x=30 #FORWARD PWM
y=30 #BACKWARD PWM
z=30 #LEFT PWM
a=30 #RIGHT PWM 
b=30 #CLOCK PWM
c=30 #ANTI CLOCK PWM

#PUSH BUTTON INPUTS

GPIO.setup(26,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(38,GPIO.IN)
GPIO.setup(40,GPIO.IN)

#MOTORS

#MOTOR LEFT1

GPIO.setup(31,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)	   #PWM PIN
Left1_pwm=GPIO.PWM(19,100)
GPIO.setup(33,GPIO.OUT)

#MOTOR LEFT2

GPIO.setup(35,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)    #PWM PIN
Left2_pwm=GPIO.PWM(21,100)
GPIO.setup(37,GPIO.OUT)

#MOTOR RIGHT1

GPIO.setup(8,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)    #PWM PIN
Right1_pwm=GPIO.PWM(23,100)
GPIO.setup(10,GPIO.OUT)

#MOTOR RIGHT2

GPIO.setup(12,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)    #PWM PIN
Right2_pwm=GPIO.PWM(29,100)
GPIO.setup(16,GPIO.OUT)

#MOTOR OUTPUTS

GPIO.output(31,0)
GPIO.output(33,0)
GPIO.output(35,0)
GPIO.output(37,0)
GPIO.output(8,0)
GPIO.output(10,0)
GPIO.output(12,0)
GPIO.output(16,0)

#CONDITIONS

while True:
	  up=GPIO.input(26)
	  down=GPIO.input(24)
	  left=GPIO.input(22)
	  right=GPIO.input(18)
	  clock=GPIO.input(38)
	  anticlock=GPIO.input(40)

	  if (up==1):
	  
	       print "FORWARD",up

#motor left1
               GPIO.output(31,0)	
	       GPIO.output(33,1)
	       Left1_pwm.start(x)
#motor left2
               GPIO.output(35,0)
               GPIO.output(37,1)
               Left2_pwm.start(x)  
#motor right1
               GPIO.output(8,1)
               GPIO.output(10,0)
       	       Right1_pwm.start(x)  
#motor right2
               GPIO.output(12,1)
               GPIO.output(16,0)
               Right2_pwm.start(x)  

	  elif (down==1):

	       print "BACKWARD",down

#motor left1
               GPIO.output(31,1)
               GPIO.output(33,0)
               Left1_pwm.start(y)
#motor left2
               GPIO.output(35,1)
               GPIO.output(37,0)
               Left2_pwm.start(y)
#motor right1
               GPIO.output(8,0)
               GPIO.output(10,1)
               Right1_pwm.start(y)
#motor right2
               GPIO.output(12,0)
               GPIO.output(16,1)
               Right2_pwm.start(y)

	  elif (left==1):

               print "LEFT",left

#motor left1
               GPIO.output(31,1)
               GPIO.output(33,0)
               Left1_pwm.start(z)
#motor left2
               GPIO.output(35,0)
               GPIO.output(37,1)
               Left2_pwm.start(z)
#motor right1
               GPIO.output(8,1)
               GPIO.output(10,0)
               Right1_pwm.start(z)
#motor right2
               GPIO.output(12,0)
               GPIO.output(16,1)
               Right2_pwm.start(z)

	  elif (right==1):

               print "RIGHT",right

#motor left1
               GPIO.output(31,0)
               GPIO.output(33,1)
               Left1_pwm.start(a)
#motor left2
               GPIO.output(35,1)
               GPIO.output(37,0)
               Left2_pwm.start(a)
#motor right1
               GPIO.output(8,0)
               GPIO.output(10,1)
               Right1_pwm.start(a)
#motor right2
               GPIO.output(12,1)
               GPIO.output(16,0)
               Right2_pwm.start(a)

	  elif (clock==1):

               print "CLOCKWISE",clock

#motor left1
               GPIO.output(31,0)
               GPIO.output(33,1)
               Left1_pwm.start(b)
#motor left2
               GPIO.output(35,0)
               GPIO.output(37,1)
               Left2_pwm.start(b)
#motor right1
               GPIO.output(8,0)
               GPIO.output(10,1)
               Right1_pwm.start(b)
#motor right2
               GPIO.output(12,0)
               GPIO.output(16,1)
               Right2_pwm.start(b)

	  elif (anticlock==1):

               print "ANTICLOCKWISE",anticlock

#motor left1
               GPIO.output(31,1)
               GPIO.output(33,0)
               Left1_pwm.start(c)
#motor left2
               GPIO.output(35,1)
               GPIO.output(37,0)
               Left2_pwm.start(c)
#motor right1
               GPIO.output(8,1)
               GPIO.output(10,0)
               Right1_pwm.start(c)
#motor right2
               GPIO.output(12,1)
               GPIO.output(16,0)
               Right2_pwm.start(c)

	  elif (anticlock==0 and up==0 and down==0 and left==0 and right==0 and clock==0):

               print "FUCK YOU!"

#motor left1
               GPIO.output(31,1)
               GPIO.output(33,1)
               Left1_pwm.start(0)
#motor left2
               GPIO.output(35,1)
               GPIO.output(37,1)
               Left2_pwm.start(0)
#motor right1
               GPIO.output(8,1)
               GPIO.output(10,1)
               Right1_pwm.start(0)
#motor right2
               GPIO.output(12,1)
               GPIO.output(16,1)
               Right2_pwm.start(0)

