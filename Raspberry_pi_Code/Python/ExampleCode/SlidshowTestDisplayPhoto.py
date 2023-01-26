from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
#win.geometry("750x400")
win.attributes('-fullscreen', True)
wwid, whgt = win.winfo_screenwidth(), win.winfo_screenheight()

#Create a canvas
canvas= Canvas(win, width=wwid, height=whgt)
canvas.pack()

def Process_Image(ph):
    

    rawimg = Image.open("/home/pi/Desktop/Clearvoyance/Clearvoyance/Photos_Slides/" + ph)
    iwid, ihgt = rawimg.size

    ratio = min(wwid/iwid, whgt/ihgt)
    iwid = int(iwid * ratio)
    ihgt = int(ihgt * ratio)
    rawimg = rawimg.resize((iwid, ihgt), Image.ANTIALIAS)

    #Load an image in the script
    return ImageTk.PhotoImage(rawimg)
    

photo1 = Process_Image("piPhoto.jpg")
photo2 = Process_Image("4k")
photo3 = Process_Image("800")

x = 1;

def slides():
    global x
    if x == 4:
        x = 1
    if x == 1:
        canvas.delete("all")
        canvas.create_image(wwid/2, whgt/2, image=photo1)
    elif x == 2:
        canvas.delete("all")
        canvas.create_image(wwid/2, whgt/2, image=photo2)
    elif x == 3:
        canvas.delete("all")
        canvas.create_image(wwid/2, whgt/2, image=photo3)
    x = x + 1
    win.after(5000, slides)
    
slides();

win.mainloop()
