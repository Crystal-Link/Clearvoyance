from PIL import Image
import os

# processes the image and resizes them as a tkinter photo
# The larger of the photo's width or height is fit to the input value
def Process_Image(path, filename, width, height):
    rawimg = Image.open( str(path) + os.sep + filename)
    iwid, ihgt = rawimg.size

    ratio = min(width/iwid, height/ihgt)
    iwid = int(iwid * ratio)
    ihgt = int(ihgt * ratio)
    rawimg = rawimg.resize((iwid, ihgt), Image.LANCZOS)

    #Load an image in the script
    return rawimg