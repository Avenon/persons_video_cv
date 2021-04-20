import streamlink
import cv2

url = 'https://www.youtube.com/watch?v=UZ_-6NDQAxM&t=605s'

streams = streamlink.streams(url)
capture = cv2.VideoCapture(streams["best"].url)

while True:
    ret, frame = capture.read()
    print(frame)
    #cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break