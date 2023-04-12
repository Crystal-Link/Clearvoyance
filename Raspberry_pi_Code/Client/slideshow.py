import os
import threading
import queue
from tkinter import *
from PIL import Image,ImageTk
import time
import helpers

photos = []
wwid, whgt = 0, 0
delay = 2000
#dir_path = "C:\\Users\\mzipp\\OneDrive\\Desktop\\College\\Stevens\\Fifth Semester\\D8\\Clearvoyance\\Photos_Slides\\" #This is the path for mikes computer
dir_path = "/home/pi/Desktop/Clearvoyance/Clearvoyance/Photos_Slides/" #this is the directy for the pi
dumb_dir_path = "C:\\Users\\Jordan\\Documents\\Clearvoyance\\Photos_Slides\\" # windows is dumb lol

def slideshow(tk_frame, upload_event, new_img_queue):
    t_slideshow_disp = threading.Thread(target=slideshow_display, args=(tk_frame))
    t_upload_listener = threading.Thread(target=upload_listener, args=(upload_event, new_img_queue))
    t_slideshow_disp.start()
    t_upload_listener.start()

# The slideshow display function
def slideshow_display(tk_frame): 
    wwid, whgt = tk_frame.winfo_screenwidth(), tk_frame.winfo_screenheight()
    label = Label(tk_frame)
    tk_frame.config(cursor="none")
    tk_frame.columnconfigure(0, weight=1)
    tk_frame.columnconfigure(1, weight=1)
    tk_frame.columnconfigure(2, weight=1)

    # makes a list of tkinter photo objects to be displayed
    photos = []
    photos_name = sorted(os.listdir(dumb_dir_path)) # grab the photo names using os and sort them in a list
    for photo in photos_name:
        photos.append(helpers.Process_Image(dumb_dir_path, photo, wwid, whgt))
    
    # displays each photo in the list and loops infinitely
    while True:
        for photo in photos:
            label.destroy()
            label = Label(tk_frame, image=photo)
            label.grid(column=1, row=0)
            tk_frame.update()
            tk_frame.after(delay, None)

# Used to listen/update for live uploads during slideshow functionality
def upload_listener(upload_event, new_img_queue):
    while True: 
        upload_event.wait()
        new_img = new_img_queue.get()
        photos.append(helpers.Process_Image(dumb_dir_path, new_img, wwid, whgt))