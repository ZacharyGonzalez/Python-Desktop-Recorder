import cv2
import pyautogui
import numpy as np

class VideoRecorder:
    def __init__(self):
        self.resolution = (1920, 1080)
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.filename = "Recording.avi"
        self.fps=cv2.CAP_PROP_FPS
        self.out = cv2.VideoWriter(self.filename, self.fourcc, self.fps, self.resolution)
        self.running = True
        self.framecount=0

    def record(self):
        cv2.namedWindow("Live",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Live", 480, 720)

        while self.running:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            cv2.imshow('Live', frame)
            if cv2.waitKey(1) == ord('q'):
                self.stop()

        #close and finish
        self.out.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.running=False
