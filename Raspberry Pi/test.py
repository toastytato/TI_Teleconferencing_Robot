import RPi.GPIO as GPIO          
from time import sleep

import time 
import paho.mqtt.client as paho
from paho import mqtt




#Set Up GPIO Ports
in1 = 24
in2 = 23
en = 25
temp1=1

in3 =5
in4 =6
en2 =13

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)


GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en,100)
p2=GPIO.PWM(en2,100)
p.start(50)
p2.start(50)


#Change according to specific ATS
time_between_readings = 1 #in seconds
HIVEMQ_username = "karen"  # Set up in HIVEMQ Cloud Broker Portal, see Setup M>
HIVEMQ_password = "seniordesignteami13" 
HIVEMQ_broker_URL = "f88526ba972442818f936ee5c29a35e8.s2.eu.hivemq.cloud" #Copy>
HIVEMQ_broker_port = 8883 #Same as URL

# setting callbacks for different events to see if it works, print the message >
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
#

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    message = msg.payload.decode("utf-8")
    if(message == "forward"):
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    
    elif(message == "right"):
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
    
    elif(message =="left"):
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    
    
    elif(message == "stop"):
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        print("hi")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        
    elif(message == "slow"):
        p.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        
    elif(message == "medium"):
        p.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        
    elif(message == "fast"):
        p.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        
        
    

# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect
#client.on_subscribe = on_subscribe
# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(HIVEMQ_username, HIVEMQ_password)


# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(HIVEMQ_broker_URL, HIVEMQ_broker_port)
client.subscribe('control')
# setting callbacks, use separate functions like above for better visibility

client.on_message = on_message



client.loop_forever()



