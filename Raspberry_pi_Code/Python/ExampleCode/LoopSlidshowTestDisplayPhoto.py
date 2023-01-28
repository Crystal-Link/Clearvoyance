from tkinter import *
from PIL import Image,ImageTk
import time


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
    

    #rawimg = Image.open("/home/pi/Desktop/Clearvoyance/Clearvoyance/Photos_Slides/" + ph) #onpi
    rawimg = Image.open("C:\\Users\\mzipp\\OneDrive\\Desktop\\College\\Stevens\\Fifth Semester\\D8\\Clearvoyance\\Photos_Slides\\" + ph) #mike's computer
    iwid, ihgt = rawimg.size

    ratio = min(wwid/iwid, whgt/ihgt)
    iwid = int(iwid * ratio)
    ihgt = int(ihgt * ratio)
    rawimg = rawimg.resize((iwid, ihgt), Image.ANTIALIAS)

    #Load an image in the script
    return ImageTk.PhotoImage(rawimg)
    
photo1 = Process_Image("photo1.jpg")
photo2 = Process_Image("photo2.jpg")
photo3 = Process_Image("photo3.jpg")

photos = [photo1,photo2,photo3]



while True:
    for i in range(3):
        canvas.delete("all")
        canvas.create_image(wwid/2, whgt/2, image=photos[i])
        win.update()
        win.after(2000, None)

    




