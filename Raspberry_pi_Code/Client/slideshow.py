import os
from pathlib import Path
import threading
# import queue
from tkinter import *
# from PIL import Image,ImageTk
# import time
import helpers
import time

delay = 2

this_path = Path(__file__).parent
relative = '../../Photos_Slides'
dir_path = (this_path / relative).resolve()

# dir_path = os.path.join("..", "..", "Photos_Slides") # relative directory

new_loaded = threading.Event()

# The slideshow display function
def slideshow_display(gui_control, win_width, win_height, photos): 
    # makes a list of tkinter photo objects to be displayed
    photos_name = sorted(os.listdir(dir_path)) # grab the photo names using os and sort them in a list
    for photo in photos_name:
        photos.append(helpers.Process_Image(dir_path, photo, win_width, win_height))
    
    # displays each photo in the list and loops infinitely
    iterator = 0
    while True:
        num_photos = len(photos)
        print(num_photos)
        if (num_photos > 0):
            if (iterator >= num_photos):
                iterator = 0
            gui_control.put((1, photos[iterator]))
            iterator += 1
            time.sleep(delay)
        else: 
            new_loaded.wait()
            new_loaded.clear()

# Used to listen/update for live uploads during slideshow functionality
def upload_listener(new_img_queue, win_width, win_height, photos):
    while True: 
        new_img = new_img_queue.get(block=True, timeout=None)
        photos.append(helpers.Process_Image(dir_path, new_img, win_width, win_height))
        print('From upload listener, num should now be ' + str(len(photos)))
        new_loaded.set()

# The "main" slideshow function
def slideshow(gui_control, win_width, win_height, new_img_queue, photo_bank):
    # slideshow_display(gui_pipe, win_width, win_height)
    t_slideshow_disp = threading.Thread(target=slideshow_display, args=(gui_control, win_width, win_height, photo_bank))
    t_upload_listener = threading.Thread(target=upload_listener, args=(new_img_queue, win_width, win_height, photo_bank))
    t_slideshow_disp.start()
    t_upload_listener.start()