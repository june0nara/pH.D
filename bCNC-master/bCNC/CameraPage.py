from __future__ import print_function
import cv2
from CNC import CNC,Block
from ToolsPage import ToolsPage

class CameraPage(ToolsPage):
    __future__ = _("Camera")
    def __init__(self, master):
        ToolsPage.__init__(self, master, "Camera", "Camera")
        self.cap = cv2.VideoCapture(0)  # 0 is the default camera

    def populate(self):
        self.toolsFrame.pack(side=TOP, fill=X)
        # Add your camera related widgets and functionalities here

    def update(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Wait for a key press and close the window if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()

    def execute(self, app):
        pass
