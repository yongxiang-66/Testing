import pyautogui
import cv2
import numpy as np


# Specify resolution
resolution = (1920,1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")


#Specify name of Output file
filename = "Recording.avi"

# Frame rate
fps = 50.0

#VideoWriter object 
out = cv2.VideoWriter(filename,codec,fps,resolution)


#Optional 
#Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:

    #Take screenshot using PyAutoGui
    img = pyautogui.screenshot()

    #Convert the screenshot to a numpy array
    frame = np.array(img)

    #convert the background from Blue,Green,Red to Red , Green , Blue
    frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Write to output file
    out.write(frame)

    #Optional : Display the recording screen 
    cv2.imshow('Live', frame)

    #Stop recording when we press 's
    if cv2.waitKey(1) == ord('s'):
        break

#Release the Video Writter
out.release()

#Destroy window
cv2.destroyAllWindows()

