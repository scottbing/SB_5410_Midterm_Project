from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog
import tkinter.constants
from tkinter.filedialog import askopenfilename
import pyautogui


#Create a PIL.Image object
red_image = PIL.Image.open("flag.png")

#Convert to RGB colorspace
red_image_rgb = red_image.convert("RGB")

#Get color from (x, y) coordinates
rgb_pixel_value = red_image_rgb.getpixel((20,15))

print(rgb_pixel_value)
