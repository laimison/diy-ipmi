#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.output(3, False)
time.sleep(1);
GPIO.output(3, True)
GPIO.cleanup()
