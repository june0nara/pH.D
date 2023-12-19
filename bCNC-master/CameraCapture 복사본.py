import numpy as np
import cv2
from datetime import datetime

# Capture from the default camera
cap = cv2.VideoCapture(0)

def main():
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
