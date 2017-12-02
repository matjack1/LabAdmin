 #!/usr/bin/env python
import random
import time
import pigpio
import signal
import wiegand
import LabAdminNfcRequest as nfc
#import relay
import sys

RED_PIN=17
GREEN_PIN=27
RELAY1_PIN=2
RELAY2_PIN=3

def callback(bits, code):
	print("bits={} code={}".format(bits, code))
	#rudimental noise filter
	if code>0 and bits<59:
		if nfc.request(code):
			#external door
			pi.write(RELAY1_PIN,1)
			time.sleep(0.1)
			pi.write(RELAY1_PIN,0)

			#GPIO.output(GREEN_PIN,0)
			time.sleep(1)
			#GPIO.output(GREEN_PIN,1)

			#internal door
			pi.write(RELAY2_PIN,1)
			time.sleep(20)
			pi.write(RELAY2_PIN,0)
		else:
			print "no"
			pi.write(RED_PIN,0)
			time.sleep(1)
			pi.write(RED_PIN,1)

logfile=open("logs.txt","wa")
#sys.stdout =logfile
print "starting"

#relayControl = relay.Relay()
pi = pigpio.pi()

pi.set_mode(RED_PIN, pigpio.OUTPUT)
pi.set_mode(GREEN_PIN, pigpio.OUTPUT)
pi.set_mode(RELAY1_PIN, pigpio.OUTPUT)
pi.set_mode(RELAY2_PIN, pigpio.OUTPUT)
pi.write(RED_PIN,1)
pi.write(GREEN_PIN,1)
pi.write(RELAY1_PIN,0)
pi.write(RELAY2_PIN,0)

w = wiegand.decoder(pi, 14, 15, callback)

if __name__=="__main__":
	def endProcess(signalnum=None, handler=None):
		#relayControl.ALLOFF()
		pi.write(RELAY1_PIN,0)
		pi.write(RELAY2_PIN,0)
		w.cancel()
		logfile.close()
		pi.stop()
		sys.exit()

	signal.signal(signal.SIGINT, endProcess)

	while True:
		time.sleep(1000)
