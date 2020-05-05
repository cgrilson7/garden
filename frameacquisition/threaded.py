from threading import Thread
import cv2


class PS3EyeStream:
    '''
    Threaded reading of a single PS3 Eye camera
    '''
    
    def __init__(self, src=0):
        # initialize the stream
        self.stream = cv2.VideoCapture(src)
        # read the first frame
        self.grabbed, self.frame = self.stream.read()
        
        # if the thread should be stopped, this variable should be set to True
        self.stopRequested = False

    def start(self):
        # starts the thread
        Thread(target=self.update, args=()).start()
        return self
    
    def update(self):
        # until the thread is stopped...
        while True:
            if self.stopRequested:
                # stop the thread
                return
            # otherwise, read the next frame
            self.grabbed, self.frame = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopRequested = True


    
