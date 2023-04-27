# import datetime
import os
import time
import requests, json
import threading
from pathlib import Path

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

def render_alert(tk_root, alert):
    img_name = alertDict[alert["Type"]]
    img_path = os.path.join(img_dir_path, img_name)
    image = Image.open(img_path)
    
    new_size = (800, 800)
    image = image.resize(new_size)

    
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(tk_root, image=image)
    image_label.place(relx=0.5, rely=0.5, anchor="center")
    text_label = tk.Label(tk_root, text="Alert",font=("Arial", 70),bg="white",highlightthickness=0, highlightbackground="white")
    text_label.config(text=alert["Description"])
    text_label.pack(side="bottom", anchor="center")
    tk_root.update()