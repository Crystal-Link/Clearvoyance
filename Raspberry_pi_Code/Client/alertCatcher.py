# import datetime
import os
import time
import requests, json
import threading
from pathlib import Path

import tkinter as tk
from PIL import ImageTk, Image

complete_url = "http://10.156.0.236//TestAlert.json"
ping_delay = 2
render_delay = 10
emergencyFound = threading.Event()

# The slideshow display function
def alert_send(gui_control, alerts): 
    # sends alerts and and loops infinitely
    iterator = 0
    old_alert = {}
    while True:
        num_alerts = len(alerts)
        if (num_alerts > 0):
            if (iterator >= num_alerts):
                iterator = 0
            if (alerts[iterator] != old_alert):
                print('New alert found, sending.')
                gui_control.put((2, alerts[iterator]))
                old_alert = alerts[iterator]
            iterator += 1
            time.sleep(render_delay)
        else: 
            emergencyFound.wait()
            emergencyFound.clear()

# Used to listen/update for live uploads during slideshow functionality
def server_ping(gui_control, alerts):
    while True: 
        response = requests.get(complete_url).json()['alerts']
        changed = False
        if len(response) != len(alerts):
            changed = True
        else:
            for i in range(0, len(response)):
                if alerts[i]["Type"] != response[i]["Type"] or alerts[i]["Description"] != response[i]["Description"]:
                    changed = True
                    break
        if changed:
            alerts.clear()
            for i in range(0, len(response)):
                alerts.append(response[i])
            if (len(alerts) > 0):
                emergencyFound.set()
            else:
                gui_control.put((3, None))
        time.sleep(ping_delay)


def alertCatcher(gui_control, alert_bank):
    t_alert_send = threading.Thread(target=alert_send, args=(gui_control, alert_bank))
    t_server_ping = threading.Thread(target=server_ping, args=(gui_control, alert_bank))
    t_alert_send.start()
    t_server_ping.start()
