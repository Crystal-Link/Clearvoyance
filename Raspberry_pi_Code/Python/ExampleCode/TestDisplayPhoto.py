# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
# win.geometry("750x400")
win.attributes('-fullscreen', True)
wwid, whgt = win.winfo_screenwidth(), win.winfo_screenheight()

# Create a canvas
canvas = Canvas(win, width=wwid, height=whgt)
canvas.pack()

# TODO: $HOME_DIR = pwd
rawimg = Image.open("Photos_Slides/piPhoto.jpg")
iwid, ihgt = rawimg.size

ratio = min(wwid/iwid, whgt/ihgt)
iwid = int(iwid * ratio)
ihgt = int(ihgt * ratio)
rawimg = rawimg.resize((iwid, ihgt), Image.ANTIALIAS)

# Load an image in the script
img = ImageTk.PhotoImage(rawimg)

# Add image to the Canvas Items
canvas.create_image(wwid/2, whgt/2, image=img)

# TODO: Close this loop somehow.
win.mainloop()
