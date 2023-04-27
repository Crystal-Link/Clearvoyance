# import subprocess
import helpers
import threading
import queue
from PIL import ImageTk
# import sys
import os
from tkinter import *
import WebServer.store_server
import slideshow
import alertCatcher
from alertRender import render_alert

stop_event = threading.Event() # used to signal termination to the threads
#TODO: implement exit into the threads individually

try:
    root = Tk() # create tkinter frame
    root.attributes('-fullscreen', True) # sets display size\
    win_width, win_height = root.winfo_screenwidth(), root.winfo_screenheight()
    print((win_width, win_height))

    stop_event = threading.Event() # used to signal termination to the threads
    #TODO: implement exit into the threads individually
    gui_control = queue.Queue()
    new_store_img = queue.Queue()
    delete_store_img = queue.Queue()
    photo_bank = []
    alert_bank = []

    t_store_server = threading.Thread(target=WebServer.store_server.store_server, args=(new_store_img, delete_store_img))
    t_slideshow = threading.Thread(target=slideshow.slideshow, args=(gui_control, win_width, win_height, new_store_img, delete_store_img, photo_bank))
    t_alertCatcher = threading.Thread(target=alertCatcher.alertCatcher, args=(gui_control, alert_bank))

    t_store_server.start()
    t_slideshow.start()
    t_alertCatcher.start()

    emergency = False
    while True:
        # Wait for gui command
        gui_command = gui_control.get(block=True, timeout=None)
        # Wipe the window
        if not (gui_command[0] == 1 and emergency): 
            for widget in root.winfo_children():
                widget.destroy()
        if gui_command[0] == 1 and not emergency:
            # Got a slideshow command, config the root and display the image.
            root.config(cursor="none")
            root.columnconfigure(0, weight=1)
            root.columnconfigure(1, weight=1)
            root.columnconfigure(2, weight=1)
            input_img = ImageTk.PhotoImage(gui_command[1])
            label = Label(root, image=input_img)
            label.grid(column=1, row=0)
            root.update()
        elif gui_command[0] == 2:
            # Got an emergency alert! Need to render and display it. 
            emergency = True
            root.configure(bg = "white")
            render_alert(root, gui_command[1], win_width, win_height)
        elif gui_command[0] == 3:
            emergency = False

except (KeyboardInterrupt, SystemExit):
    # Clean up and exit gracefully on keyboard interrupt
	stop_event.set()