# import datetime
import os
import time
import requests, json
import threading
from pathlib import Path
from helpers import Process_Image

import tkinter as tk
from PIL import ImageTk, Image

alertDict = {
    "Other": "generic.png",
    "Amber Alert": "amber.png",
    "Shooter": "shooter.png",
    "Weather": "weather.png"
}

# Define the image path
this_path = Path(__file__).parent
relative = '../../AlertPhotos'
img_dir_path = (this_path / relative).resolve()

def render_alert(tk_root, alert, win_width, win_height):
    img_name = alertDict[alert["Type"]]
    img_path = os.path.join(img_dir_path, img_name)
    
    image = ImageTk.PhotoImage(Process_Image(img_dir_path, img_name, win_width * 0.65, win_height * 0.65))
    image_label = tk.Label(tk_root, image=image)
    image_label.place(relx=0.5, rely=0.5, anchor="center")
    text_label = tk.Label(tk_root, text="Alert",font=("Arial", 35 * (int(min(win_width / 1280, win_height / 720)))),bg="white",highlightthickness=0, highlightbackground="white")
    text_label.config(text=alert["Description"])
    text_label.place(relx=0.5, rely=0.925, anchor="center")
    tk_root.update()