import subprocess
import threading
import queue
import sys
import tkinter as tk
import WebServer.store_server
import slideshow
import alertRender

root = tk.Tk() # create tkinter frame
root.attributes('-fullscreen', True) # sets display size

new_upload = threading.Event()
new_store_img = queue.Queue()

t_store_server = threading.Thread(target=WebServer.store_server.store_server)
t_slideshow = threading.Thread(target=lcd_clock)
t_alertRender = threading.Thread(target=lcd_clock)




def lcd_clock_TH():

    try:
        lcd = LCD(address=0x3F, backlight=True)

        DHT_SENSOR = Adafruit_DHT.DHT11
        DHT_PIN = 4

        def gethumid_temp():
            global temperature
            global humidity
            while True:
                humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
                if humidity is not None and temperature is not None:
                    temperature = temperature*(9.0/5.0)+32
                    time.sleep(20)

        def lcd_clock():
            LastTime = 0
            while True:
                now = datetime.now()
                current_time = now.strftime("%I:%M %p")
                if current_time != LastTime:
                    lcd.clear()
                    lcd.text(current_time, 1)
                    try:
                        lcd.text("T="+str(round(temperature, 1)) +
                                " F H=" + str(round(humidity, 1))+"%", 2)
                    except:
                        lcd.text("invalad data!", 2)
                    LastTime = current_time
                time.sleep(.1)
                

        def lcd_backlight_set():
            while True:
                state = input("Enter the light state = ")
                if state == "0":
                    lcd.backlight(False)
                elif state == "1":
                    lcd.backlight(True)from numpy import true_divide
import Adafruit_DHT
import time
import threading
from datetime import datetime
import RPi.GPIO as GPIO
import os
from rpi_lcd import LCD



def lcd_clock_TH():

    try:
        lcd = LCD(address=0x3F, backlight=True)

        DHT_SENSOR = Adafruit_DHT.DHT11
        DHT_PIN = 4

        def gethumid_temp():
            global temperature
            global humidity
            while True:
                humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
                if humidity is not None and temperature is not None:
                    temperature = temperature*(9.0/5.0)+32
                    time.sleep(20)

        def lcd_clock():
            LastTime = 0
            while True:
                now = datetime.now()
                current_time = now.strftime("%I:%M %p")
                if current_time != LastTime:
                    lcd.clear()
                    lcd.text(current_time, 1)
                    try:
                        lcd.text("T="+str(round(temperature, 1)) +
                                " F H=" + str(round(humidity, 1))+"%", 2)
                    except:
                        lcd.text("invalad data!", 2)
                    LastTime = current_time
                time.sleep(.1)
                

        def lcd_backlight_set():
            while True:
                state = input("Enter the light state = ")
                if state == "0":
                    lcd.backlight(False)
                elif state == "1":
                    lcd.backlight(True)
                time.sleep(0.1)

        t1 = threading.Thread(target=gethumid_temp)
        t2 = threading.Thread(target=lcd_clock)
        t3 = threading.Thread(target=lcd_backlight_set)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
    finally:
        lcd.clear()
        lcd.backlight(False)
        


lcd_clock_TH()

                time.sleep(0.1)

        t1 = threading.Thread(target=gethumid_temp)
        t2 = threading.Thread(target=lcd_clock)
        t3 = threading.Thread(target=lcd_backlight_set)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
    finally:
        lcd.clear()
        lcd.backlight(False)
        


lcd_clock_TH()
