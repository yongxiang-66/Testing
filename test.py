import pyautogui
import cv2
import numpy as np


# Specify resolution
resoultion = (1920,1080)

# Specify video codec
codec = cv2.VideoWritter_fourcc(*"XVID")

#Specify name of Output file
filename = "Recording.avi"

# Frames rate
fps = 144.0

#VideoWritter object 
out = cv2.VideoWriter(filename,codec,fps,resoultion)

