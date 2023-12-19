#!/usr/bin/env python3

import os
import sys
import runpy
import multiprocessing
import numpy as np
import cv2
from datetime import datetime

# Capture from the default camera
cap = cv2.VideoCapture(0)

def main_bCNC():
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 8):
        print("ERROR: Python3.8 or newer is required to run bCNC!!")
        exit(1)

    print("This is currently broken. Use instead: python -m bCNC")

    bcncpath = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "bCNC/__main__.py")

    print(f"bCNC runpy loader: {bcncpath}")
    runpy.run_path(bcncpath, run_name="__main__")

def main_camera():
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

    while True:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1) & 0xFF

            # if the 's' key is pressed, save the frame
            if key == ord('s'):
                saveFrame(frame)

            # if the 'q' key is pressed, break from the loop
            elif key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def saveFrame(frame):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")  # Gets current time
    filename = f'./saved_{timestamp}.png'
    print(f"Attempting to save frame to {filename}")  # Debug line
    success = cv2.imwrite(filename, frame)  # Saves the frame with the new filename

    if success:
        print("Successfully saved frame.")
    else:
        print("Failed to save frame.")

if __name__ == "__main__":
    # Create and start two processes for each application
    p1 = multiprocessing.Process(target=main_bCNC)
    p2 = multiprocessing.Process(target=main_camera)

    p1.start()
    p2.start()
