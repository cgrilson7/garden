import cv2
from frameacquisition.threaded import PS3EyeStream
from frameacquisition.helpers import FPS

stream = PS3EyeStream(src='http://192.168.1.53:8081/')
stream.start()

if (stream.stream.isOpened() == False): 
  print("Error opening video stream or file")

fps = FPS().start()
while fps.numFrames < 1000:
# while stream.stream.isOpened():
    frame = stream.read()
    fps.update()
    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
cv2.destroyAllWindows()     
stream.stop()