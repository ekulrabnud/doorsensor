import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BCM)

door_pin = 15
GPIO.setup(door_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

doorbell = 1

def on_connect(client,data,flags,rc):
	print "Connected"
	client.subscribe('/master')



client = mqtt.Client("Door")
client.on_connect = on_connect
client.connect('192.168.1.15',1883,10)
#client.loop_start()
print "waiting"
client.publish('/doorbell',"Doorbell Connect")

while True:
#	name = "luke"
#	print name
#	time.sleep(1)
#	client.publish('/door',name)
	if GPIO.input(door_pin)==False:
		print("/doorbell = True")
		doorbell = 1
		client.publish("/doorbell","true")
		time.sleep(1)
	if (GPIO.input(door_pin) and doorbell == 1):
		client.publish("/doorbell","false")
		print("/doorbell = False")
		doorbell = 0
		
