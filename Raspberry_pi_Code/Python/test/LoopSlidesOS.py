import os
from tkinter import *
from PIL import Image,ImageTk
import time

photos = []
delay = 2000
dir_path = "C:\\msys64\\home\\Crystal-Link\\git\\Clearvoyance\\Photos_Slides\\" #replace with your own path
#dir_path = "/home/pi/Desktop/Clearvoyance/Clearvoyance/Photos_Slides/" #this is the directy for the pi

photos_name = sorted(os.listdir(dir_path)) # grab the photo names using os and sort them in a list
numPhots = len(photos_name) # get the number of photos in the directory
#print(str(photos_name) + "there are "+ str(numPhots)+" photos") #print what's in the directory


win = Tk() # create tkinter frame
win.attributes('-fullscreen', True) # sets display size
wwid, whgt = win.winfo_screenwidth(), win.winfo_screenheight()

#creates a canvas
canvas= Canvas(win, width=wwid, height=whgt)
canvas.pack()

# processes the image and resizes them as a tkinter photo
def Process_Image(ph):
    rawimg = Image.open( dir_path + ph) #mike's computer
    iwid, ihgt = rawimg.size

    ratio = min(wwid/iwid, whgt/ihgt)
    iwid = int(iwid * ratio)
    ihgt = int(ihgt * ratio)
    rawimg = rawimg.resize((iwid, ihgt), Image.LANCZOS)

    #Load an image in the script
    return ImageTk.PhotoImage(rawimg)

# makes a list of tkinter photo objects to be displayed
for photo in photos_name:
    photos.append(Process_Image(photo))

#displays each photo in the list and loops infinitally
    win.config(cursor="none")
while True:
    for i in range(numPhots):
        canvas.delete("all")
        canvas.create_image(wwid/2, whgt/2, image=photos[i])
        win.update()
        win.after(delay, None)
