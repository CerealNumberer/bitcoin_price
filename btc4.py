import requests, json
import RPi.GPIO as GPIO
from time import sleep

counter = 0

sleep_time = int(input("How long in seconds?: "))

def bprice():
    URL = "https://www.bitstamp.net/api/ticker/"
    try:
        r=requests.get(URL)
        thePrice = "{0:.2f}".format(float(json.loads(r.text)['last']))
        return thePrice
    except requests.ConnectionError:
        print "Could not get the price by itslef"

#first_price = bprice()

#print "Please wait..."
#sleep(sleep_time)
#print "Please wait..."

second_price = bprice()
print second_price

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

try:
    while True:
        sleep(sleep_time)
        third_price = bprice()
        print third_price
        if third_price > second_price:
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(13,GPIO.LOW)
            print "Price is higher!"
        elif third_price == second_price:
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(13,GPIO.HIGH)
            print "Price has not changed"
        elif third_price < second_price:
            GPIO.output(11,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)
            print "Price is lower"
        else:
            print "Other error"
        second_price = third_price
    while counter < 9000000:
        countter += 1
    print "Target reached: %d" % counter
except KeyboardInterrupt:
    print "\n", counter
except:
    print "Other error or exception occurred!"
finally:
    GPIO.cleanup()
