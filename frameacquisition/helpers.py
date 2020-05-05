import time

class FPS:
    '''
    This class approximates the frames per second of a given camera + processing pipeline.
    '''

    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.numFrames = 0

    def start(self):
        self.startTime = time.time()
        return self

    def stop(self):
        self.endTime = time.time()

    def update(self):
        self.numFrames += 1

    def elapsed(self):
        return self.endTime - self.startTime

    def fps(self):
        return self.numFrames / self.elapsed()
