import tkinter as tk
from PIL import ImageTk, Image

# processes the image and resizes them as a tkinter photo
# fits (no-stretch) image within target width/height
def Process_Image(ph, width, height):
    rawimg = Image.open( dir_path + ph) #mike's computer
    iwid, ihgt = rawimg.size

    ratio = min(width/iwid, height/ihgt)
    iwid = int(iwid * ratio)
    ihgt = int(ihgt * ratio)
    rawimg = rawimg.resize((iwid, ihgt), Image.ANTIALIAS)

    #Load an image in the script
    return ImageTk.PhotoImage(rawimg)

root = tk.Tk() # create tkinter frame
root.attributes('-fullscreen', True) # sets display size
# wwid, whgt = root.winfo_screenwidth(), root.winfo_screenheight()

# make a label that contains the image