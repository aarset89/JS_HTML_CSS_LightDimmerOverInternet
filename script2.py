import webiopi
import pigpio
import RPi.GPIO as GPIO
import time


GPIO = webiopi.GPIO
#GPIO.setmode(GPIO.BCM)

#pi = pigpio.pi()
hall2 = 14
hall = 8
comedor = 7
habitacion1 = 25
habitacion2 = 24
pasillo = 23
bano1 = 18
bano2 = 11
habitacion_principal = 9
cocina = 10

#pi.set_mode(8, pigpio.OUTPUT)

#pi.set_PWM_range(8, 100)


#pi.hardware_PWM(18, 1000, 0 )

#pi.set_PWM_frequency(8, 1000)
#GPIO.setup(4, GPIO.ALT0)
#GPIO.setclck(8,1000)

#def setup():

GPIO.setFunction(hall, GPIO.PWM)
GPIO.pulseRatio(hall, 0)
GPIO.setFunction(comedor, GPIO.PWM)
GPIO.pulseRatio(comedor, 0)
GPIO.setFunction(habitacion1, GPIO.PWM)
GPIO.pulseRatio(habitacion1, 0)
GPIO.setFunction(habitacion2, GPIO.PWM)
GPIO.pulseRatio(habitacion2, 0)
GPIO.setFunction(pasillo, GPIO.PWM)
GPIO.pulseRatio(pasillo, 0)
#GPIO.setFunction(bano1, GPIO.PWM)
#GPIO.pulseRatio(bano1, 0)
#GPIO.setFunction(bano2, GPIO.PWM)
#GPIO.pulseRatio(bano2, 0)
GPIO.setFunction(habitacion_principal, GPIO.PWM)
GPIO.pulseRatio(habitacion_principal, 0)
GPIO.setFunction(cocina, GPIO.PWM)
GPIO.pulseRatio(cocina, 0)



#return

#GPIO.setFrequency(hall, 1000)
#pi.hardware_PWM(7, 800, 10000




#pi.write(8,1)
#print(pi.read(8))

#pi.set_PWM_frequency(hall, 1000)


