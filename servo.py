import RPi.GPIO as GPIO
import time

def move(angle=90):
	"Move the servo to the specified angle"
	pulse = int(angle) / 18.0 + 2.5


	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(16,GPIO.OUT)

	p = GPIO.PWM(16,50)
	p.start(pulse)
	time.sleep(1)
	p.stop()
	GPIO.cleanup()

if __name__ == "__main__":
	import sys
	angle = 90
	if len(sys.argv) == 2:
		angle = sys.argv[1]
	move(angle)

#try:
#	while True:
#		p.ChangeDutyCycle(7.5)
#		time.sleep(1)
#		p.ChangeDutyCycle(12.5)
#		time.sleep(1)
#		p.ChangeDutyCycle(2.5)
#		time.sleep(1)
#
#except KeyboardInterrupt:
#	p.stop()
#	GPIO.cleanup()

